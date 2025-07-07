# GraphQL Rick and Morty API (Python)

This project is a simple GraphQL wrapper over the [Rick and Morty REST API](https://rickandmortyapi.com/), built using Python, FastAPI, and Strawberry GraphQL.

It serves as a learning project to practice how to build GraphQL servers in Python by exposing part of a REST API as a GraphQL schema.

---

## 🚀 Features

- GraphQL API using Strawberry and FastAPI
- Integration with external Rick and Morty REST API
- Async HTTP requests with `httpx`
- Custom GraphQL types and resolvers
- Automated tests using `pytest` and `httpx`

---

## 🗂️ Project Structure
```bash
graphql-rickandmorty/
│
├── app/
│ ├── graphql/ # GraphQL types, resolvers, and schema
│ │ ├── types.py
│ │ ├── resolvers.py
│ │ └── schema.py
│ ├── services/ # External API integration
│ │ └── rickandmorty_api.py
│ └── main.py # FastAPI entrypoint
├── tests/ # Test suite
│ └── test_character_query.py
├── requirements.txt # Python dependencies
├── README.md
└── .gitignore
```

---

## 🛠️ Installation
### 1. Clone the repository
```bash
git clone https://github.com/yourusername/graphql-rickandmorty.git
cd graphql-rickandmorty
```

### 2. Create virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## ▶️ Running the server
```bash
uvicorn app.main:app --reload
```
Then open your browser at:
```bash
http://localhost:8000/graphql
```

You’ll see a GraphQL playground where you can run queries like:

```graphql
query {
  character(characterId: 1) {
    id
    name
    status
    species
    gender
    origin {
      name
      url
    }
    location {
      name
      url
    }
    image
    episode
  }
}
```

## 🧪 Running tests
Tests are written using pytest and httpx’s ASGI testing client.

1. Run all tests
```bash
PYTHONPATH=. pytest
```
If you're on Windows:
```bash
set PYTHONPATH=.
pytest
```

## 📌 Notes
This project uses httpx.AsyncClient with ASGITransport to test the FastAPI app without starting a real server.

The character query wraps the REST endpoint https://rickandmortyapi.com/api/character/{id} and maps its structure to a GraphQL schema using Strawberry types.

The structure is modular and extensible: you can add queries for episodes, locations, filtering, and pagination.

## 📚 Technologies
Python 3.10+

FastAPI

Strawberry GraphQL

httpx (async HTTP client)

pytest / pytest-asyncio

## 📎 License
MIT License