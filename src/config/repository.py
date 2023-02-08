from src.models.person import Person
from src.config.database import db
import uuid


class PersonRepo():

    @staticmethod
    async def retrieve():
        _people = []
        collection = db.people.find()
        async for person in collection:
            _people.append(person)
        return _people

    @staticmethod
    async def retrieve_by_id(id: str):
        return await db.people.find_one({"_id": id})

    @staticmethod
    async def retrieve_by_cpf(cpf: str):
        return await db.people.find_one({"cpf": cpf})

    @staticmethod
    async def insert(person: Person):
        id = str(uuid.uuid4())
        _person = {
            "_id": id,
            "name": person.name,
            'cpf': person.cpf,
            "age": person.age
        }
        await db.people.insert_one(_person)
        return id

    @staticmethod
    async def update(id: str, person: Person):
        _person = await db.people.find_one({"_id": id})
        if _person is None:
            return None
        _person["name"] = person.name
        _person["cpf"] = person.cpf
        _person["age"] = person.age
        await db.people.update_one({"_id": id}, {"$set": dict(_person)})
        return id

    @staticmethod
    async def delete(id: str):
        await db.people.delete_one({"_id": id})
