import httpx

BASE_URL = "https://rickandmortyapi.com/api"


async def get_character_by_id(character_id: int) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/character/{character_id}")
        response.raise_for_status
        return response.json()
