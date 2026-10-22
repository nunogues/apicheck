# PingChecker 🚀

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python" alt="Python 3.11+" />
  <img src="https://img.shields.io/badge/FastAPI-0.110%2B-009688?style=for-the-badge&logo=fastapi" alt="FastAPI" />
  <img src="https://img.shields.io/badge/HTTPX-Async-5A67D8?style=for-the-badge&logo=httpx" alt="HTTPX" />
</p>

Uma API REST desenvolvida com Python e FastAPI para verificar a disponibilidade de sites, consultar códigos de status HTTP e medir o tempo de resposta.

## ✨ Funcionalidades

- 🌐 Verificação de sites por URL
- 📡 Consulta do código de status HTTP
- ⏱️ Medição do tempo de resposta em milissegundos
- 🛡️ Tratamento de erros de conexão e timeout
- 📄 Respostas em formato JSON
- 📚 Documentação interativa com Swagger UI

## 🛠️ Tecnologias

- Python
- FastAPI
- HTTPX
- Uvicorn

## ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/pingchecker.git
```

Entre na pasta do projeto:

```bash
cd pingchecker
```

Instale as dependências:

```bash
pip install fastapi httpx uvicorn
```

## ▶️ Executando a API

Inicie o servidor com:

```bash
python -m uvicorn main:app --reload
```

A API estará disponível em:

```text
http://127.0.0.1:8000
```

## 📌 Endpoint disponível

### GET /check

Verifica um site e retorna informações sobre sua resposta HTTP.

#### Parâmetros de consulta

| Parâmetro | Tipo | Descrição |
|----------|------|-----------|
| `url` | `string` | URL do site que será verificado |

#### Exemplo de requisição

```http
GET /check?url=https://example.com
```

#### Exemplo de resposta

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

> Os valores são ilustrativos e podem variar conforme o site e a conexão.

## ⚠️ Tratamento de erros

A API também trata situações como:

- Falha de conexão com o site
- Tempo limite de resposta excedido

### Exemplo de resposta de erro

```json
{
  "success": false,
  "data": {
    "url": "https://example.com",
    "error": "O site demorou demais para responder",
    "code_status": null
  }
}
```

## 📚 Documentação interativa

Com o servidor em execução, acesse:

```text
http://127.0.0.1:8000/docs
```

Nessa página, você pode testar os endpoints diretamente pelo navegador.

## 🗂️ Estrutura do projeto

```text
pingchecker/
├── main.py
└── routes/
    ├── __init__.py
    ├── health.py
    └── check.py
```

## 🎯 Objetivo

O PingChecker é um projeto de aprendizado voltado ao desenvolvimento de APIs REST, ao consumo de serviços HTTP, ao tratamento de erros e à organização de aplicações Python.

## 📌 Status do projeto

Em desenvolvimento 🚧

Novas funcionalidades e melhorias poderão ser adicionadas conforme a evolução do projeto.

---

<p align="center">
  <strong>Desenvolvido com Python 🐍</strong>
</p>