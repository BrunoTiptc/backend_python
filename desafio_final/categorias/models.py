from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column , relationship
from sqlalchemy import String, Integer 


class CategoriaModel(BaseModel):
    __tablename__ = "categorias"
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True )
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates="categoria")
    