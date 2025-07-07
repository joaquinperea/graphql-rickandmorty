import strawberry
from app.graphql.types import Character
from app.graphql.resolvers import resolve_character


@strawberry.type
class Query:
    character: Character = strawberry.field(resolver=resolve_character)

schema = strawberry.Schema(query=Query)
