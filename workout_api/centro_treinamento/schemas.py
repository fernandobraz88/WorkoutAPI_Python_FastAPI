from contrib.schemas import BaseSchema
from pydantic import Field, PositiveFloat
from typing import Annotated

class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento',example='CT Box Crossfit',max_length=20)]
    endereco: Annotated[str, Field(description='end do centro de treinamento',example='rua, n, bairo ',max_length=60)]
    proprietario: Annotated[str, Field(description='proprietario do centro de treinamento',example='Marcos',max_length=30)]