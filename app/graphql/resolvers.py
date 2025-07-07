from app.services.rickandmorty_api import get_character_by_id
from app.graphql.types import Character, OriginLocation


async def resolve_character(character_id: int) -> Character:
    data = await get_character_by_id(character_id)
    return Character(
        id=data["id"],
        name=data["name"],
        status=data["status"],
        species=data["species"],
        type=data["type"],
        gender=data["gender"],
        origin=OriginLocation(**data["origin"]),
        location=OriginLocation(**data["location"]),
        image=data["image"],
        episode=data["episode"],
        url=data["url"],
        created=data["created"]
    )
