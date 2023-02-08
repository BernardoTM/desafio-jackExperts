def personEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "cpf": item["cpf"],
        "age": item["age"]
    }


def peopleEntity(entity) -> list:
    return [personEntity(item) for item in entity]
