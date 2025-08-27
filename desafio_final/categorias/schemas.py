from typing import Annotated
from pydantic import  Field
from desafio_final.contrib.schemas import BaseSchema



class Categoria(BaseSchema):
    nome: Annotade[str, Field(description="Nome da categoria", example="Scale", max_length=10)]
    