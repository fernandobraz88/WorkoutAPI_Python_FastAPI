from contrib.schemas import BaseSchema
from pydantic import Field, PositiveFloat
from typing import Annotated
 
class Atleta(BaseSchema):
    nome : Annotated[str, Field(descrition='Nome do atleta',example='João', max_length=50)]
    cpf : Annotated[str, Field(descrition='CPF do atleta',example='21548798780', max_length=11)]
    idade : Annotated[int, Field(descrition='idade do atleta',example='18')]
    peso : Annotated[PositiveFloat, Field(descrition='peso do atleta',example='75.5')]
    altura : Annotated[PositiveFloat, Field(descrition='Altura do atleta',example='1.70')]
    sexo : Annotated[str, Field(descrition='Sexo do atleta',example='M', max_length=1)]