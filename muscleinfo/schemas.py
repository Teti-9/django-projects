from ninja import Schema
from typing import Optional

class ExercicioSchema(Schema):
    id: int
    nome: str
    musculo: str
    musculo_residual: str
    series: int
    infos: str

class ExercicioSchemaNoID(Schema):
    nome: str
    musculo: str
    musculo_residual: str
    series: int
    infos: str

class ExercicioSchemaEdit(Schema):
    nome: Optional[str] = None
    musculo: Optional[str] = None
    musculo_residual: Optional[str] = None
    series: Optional[int] = None
    infos: Optional[str] = None