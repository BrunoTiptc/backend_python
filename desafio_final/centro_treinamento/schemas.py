from typing import Annotated
from pydantic import  Field
from desafio_final.contrib.schemas import BaseSchema



class CentroTreinamento(BaseSchema):
    nome: Annotade[str, Field(description="Nome do centro de treinamento", example="CT King", max_length=20)]
    endereco: Annotade[str, Field(description="Endereco do centro de treinamento", example="Rua X, Q02", max_length=60)]
    proprietario: Annotade[str, Field(description="Proprietario do centro de treinamento", example="Marcos", max_length=30)]
    