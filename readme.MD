# PingChecker

API REST desenvolvida com Python, FastAPI e HTTPX para consultar a disponibilidade de um endereço web, identificar o código de status HTTP e medir o tempo de resposta.

## Funcionalidades

- Verifica um endereço informado por URL.
- Retorna o código de status HTTP.
- Mede o tempo de resposta em milissegundos.
- Trata falhas de conexão e timeout.
- Retorna os resultados em JSON.
- Disponibiliza documentação interativa pelo Swagger UI.

## Tecnologias

- Python
- FastAPI
- HTTPX
- Uvicorn

## Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/nunogues/apicheck.git
cd apicheck
```

### 2. Crie um ambiente virtual (recomendado)

```bash
python -m venv .venv
```

Ative-o:

```bash
# Windows
.venv\\Scripts\\activate

# Linux / macOS
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Inicie o servidor

```bash
uvicorn main:app --reload
```

A API ficará disponível em `http://127.0.0.1:8000`.

Documentação interativa: `http://127.0.0.1:8000/docs`.

## Endpoint

### `GET /check`

Consulta um endereço web.

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `url` | string | Endereço completo a consultar, incluindo `https://` |

Exemplo:

```http
GET /check?url=https://example.com
```

Exemplo de resposta (valores ilustrativos):

```json
{
  "success": true,
  "data": {
    "url": "https://example.com",
    "status": "online",
    "code_status": 200,
    "response_time_ms": 135.42
  }
}
```

Se ocorrer timeout ou falha de conexão, a API retorna `success: false` e uma mensagem de erro em `data`.

## Estrutura do projeto

```text
apicheck/
├── main.py
├── requirements.txt
└── routes/
    ├── __init__.py
    ├── check.py
    └── health.py
```

## Observação de segurança

O endpoint recebe uma URL e faz uma requisição para ela. Antes de disponibilizar esta API publicamente, implemente validação de URLs e controles contra acesso a endereços internos ou privados (SSRF), além de limites de uso.

## Objetivo

Projeto de aprendizado sobre desenvolvimento de APIs REST, requisições HTTP, tratamento de erros e organização de aplicações com FastAPI.