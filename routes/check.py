
import httpx
from fastapi import APIRouter
import time

router = APIRouter()


@router.get("/check")
def check_site(url: str):
    inicio = time.perf_counter()

    try:
        response = httpx.get(url, timeout=10)
    except httpx.TimeoutException:
        return {
            "success": False,
            "data": {
                "url": url,
                "error": "O site demorou demais para responder",
                "code_status": None,
            },
        }
    except httpx.RequestError:
        return {
            "success": False,
            "data": {
                "url": url,
                "error": "Falha na conexão",
                "code_status": None,
            },
        }

    fim = time.perf_counter()
    duration_ms = (fim - inicio) * 1000

    return {
        "success": True,
        "data": {
            "url": url,
            "status": "online" if response.status_code < 400 else "offline",
            "code_status": response.status_code,
            "response_time_ms": round(duration_ms, 2),
        },
    }
                                                                                                                                                                                                                                                                                                                        