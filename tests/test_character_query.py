import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_get_character_by_id():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        query = """
        query {
          character(characterId: 1) {
            id
            name
            status
            species
            type
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
            url
            created
          }
        }
        """
        response = await ac.post("/graphql", json={"query": query})
        data = response.json()

        assert response.status_code == 200
        assert "errors" not in data
        character = data["data"]["character"]
        assert character["id"] == 1
        assert character["name"] == "Rick Sanchez"
        assert character["origin"]["name"] != ""
