from contrib.schemas import BaseSchema
from pydantic import Field, PositiveFloat
from typing import Annotated

class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Nome da Categoria', example='Scales', max_length=10)]