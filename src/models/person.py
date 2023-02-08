from pydantic import BaseModel, validator
from src.util.cpf import cpf_validate


class Person(BaseModel):
    name: str
    cpf: str
    age: int

    @validator('cpf')
    def cpf_validator(cls, cpf):
        if not cpf_validate(cpf):
            raise ValueError('invalid cpf')
        return cpf
