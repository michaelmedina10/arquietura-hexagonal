from pydantic import BaseModel


class UserModel(BaseModel):
    nome: str
    sobrenome: str
    telefone: str
