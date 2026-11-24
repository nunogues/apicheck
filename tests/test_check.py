import httpx
from types import SimpleNamespace

from routes import check as check_route


def test_check_site_returns_online_and_response_time(monkeypatch):
    monkeypatch.setattr(
        check_route.httpx,
        "get",
        lambda url, timeout: SimpleNamespace(status_code=200),
    )

    result = check_route.check_site("https://example.com")

    assert result["success"] is True
    assert result["data"]["status"] == "online"
    assert result["data"]["code_status"] == 200
    assert result["data"]["response_time_ms"] >= 0


def test_check_site_marks_http_error_as_offline(monkeypatch):
    monkeypatch.setattr(
        check_route.httpx,
        "get",
        lambda url, timeout: SimpleNamespace(status_code=503),
    )

    result = check_route.check_site("https://example.com")

    assert result["success"] is True
    assert result["data"]["status"] == "offline"
    assert result["data"]["code_status"] == 503


def test_check_site_handles_timeout(monkeypatch):
    def raise_timeout(url, timeout):
        raise httpx.TimeoutException("request timed out")

    monkeypatch.setattr(check_route.httpx, "get", raise_timeout)

    result = check_route.check_site("https://example.com")

    assert result["success"] is False
    assert result["data"]["code_status"] is None
    assert "demorou demais" in result["data"]["error"]


def test_check_site_handles_connection_error(monkeypatch):
    def raise_connection_error(url, timeout):
        raise httpx.RequestError("connection failed")

    monkeypatch.setattr(check_route.httpx, "get", raise_connection_error)

    result = check_route.check_site("https://example.com")

    assert result["success"] is False
    assert result["data"]["code_status"] is None
    assert result["data"]["error"] == "Falha na conexão"
