import strawberry
from typing import List


@strawberry.type
class OriginLocation:
    name: str
    url: str


@strawberry.type
class Character:
    id: int
    name: str
    status: str
    species: str
    type: str
    gender: str
    origin: OriginLocation
    location: OriginLocation
    image: str
    episode: List[str]
    url: str
    created: str
