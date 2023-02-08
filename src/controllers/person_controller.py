from fastapi import APIRouter, HTTPException

from src.models.person import Person
from src.config.repository import PersonRepo
from src.schemas.people import peopleEntity, personEntity

person = APIRouter()


@person.get('/people/')
async def get_all_people():
    """
        Get all the people.
    """
    _peopleList = await PersonRepo.retrieve()
    return peopleEntity(_peopleList)


@person.get('/person/{id}')
async def get_by_id(id: str):
    """
        Get a person by id.
    """
    if len(id.strip()) == 0:
        raise HTTPException(status_code=400, detail="The id is empty")
    _person = await PersonRepo.retrieve_by_id(id)
    return personEntity(_person)


@person.get('/person/')
async def get_by_cpf(cpf: str):
    """
        Get a person by cpf.
    """
    try:
        _person = await PersonRepo.retrieve_by_cpf(cpf)
        return personEntity(_person)
    except Exception as e:
        raise HTTPException(status_code=404, detail="Not Found")


@person.post('/person/', status_code=201)
async def create(person: Person):
    """
        Add a person.
    """
    id = await PersonRepo.insert(person)
    _person = await PersonRepo.retrieve_by_id(id)
    return personEntity(_person)


@person.put('/person/{id}')
async def update(id: str, person: Person):
    """
        Update a person.
    """
    id = await PersonRepo.update(id, person)
    if id is None:
        raise HTTPException(status_code=400, detail="The name is empty")
    _person = await PersonRepo.retrieve_by_id(id)
    return personEntity(_person)


@person.delete('/person/{id}')
async def delete(id: str):
    """
        Delete a person by id.
    """
    await PersonRepo.delete(id)
