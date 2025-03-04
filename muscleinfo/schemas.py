from ninja import Schema
from typing import Optional, Union
from pydantic import field_serializer
from datetime import datetime

class ExercicioSchema(Schema):
    id: Union[int, str]
    nome: str
    musculo: str
    musculo_residual: str
    series: int
    carga: int
    repeticoes: float
    infos: str
    data: Union[datetime, str]

    @field_serializer('data')
    def serialize_data(self, value: Union[datetime, str]) -> str:
        if isinstance(value, datetime):
            return value.strftime('%d/%m/%Y')
        elif isinstance(value, str):
            return value

class ExercicioSchemaNoID(Schema):
    nome: str
    musculo: str
    musculo_residual: str
    series: int
    carga: int
    repeticoes: float
    infos: str

class ExercicioSchemaEdit(Schema):
    nome: Optional[str] = None
    musculo: Optional[str] = None
    musculo_residual: Optional[str] = None
    series: Optional[int] = None
    carga: Optional[int] = None
    repeticoes: Optional[float] = None
    infos: Optional[str] = None