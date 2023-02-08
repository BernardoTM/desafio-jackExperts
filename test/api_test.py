import requests


ENDPIONT = "http://127.0.0.1:8000"


def test_create_perso():
    body = {
        "name": "Bernardo",
        "cpf": "19276745300",
        "age": "23"
    }
    response = requests.post(ENDPIONT + "/person", json=body)
    assert response.status_code == 201
    assert response.json()["name"] == "Bernardo"

    id = response.json()["id"]
    requests.delete(ENDPIONT + f"/person/{id}")


def test_get_person_by_id():
    body = {
        "name": "Bernardo",
        "cpf": "87481774315",
        "age": "23"
    }
    response_creat = requests.post(ENDPIONT + "/person", json=body)
    id = response_creat.json()["id"]
    response = requests.get(ENDPIONT + f"/person/{id}")
    assert response.status_code == 200
    assert response.json()["cpf"] == "87481774315"

    requests.delete(ENDPIONT + f"/person/{id}")


def test_get_person_by_cpf():
    body = {
        "name": "Bernardo",
        "cpf": "86519365327",
        "age": "23"
    }
    response_creat = requests.post(ENDPIONT + "/person", json=body)
    id = response_creat.json()["id"]
    response = requests.get(ENDPIONT + f"/person/?cpf={body['cpf']}")
    assert response.status_code == 200
    assert response.json()["age"] == 23

    requests.delete(ENDPIONT + f"/person/{id}")


def test_change_person():
    body = {
        "name": "Bernardo",
        "cpf": "86519365327",
        "age": "23"
    }
    response_creat = requests.post(ENDPIONT + "/person", json=body)
    id = response_creat.json()["id"]
    new_body = {
        "name": "João",
        "cpf": "86519365327",
        "age": "25"
    }
    response = requests.put(ENDPIONT + f"/person/{id}", json=new_body)
    assert response.status_code == 200
    assert response.json()["name"] == "João"

    requests.delete(ENDPIONT + f"/person/{id}")


def test_delete_person():
    body = {
        "name": "Bernardo",
        "cpf": "47257267880",
        "age": "23"
    }
    response_creat = requests.post(ENDPIONT + "/person", json=body)
    id = response_creat.json()["id"]
    response = requests.delete(ENDPIONT + f"/person/{id}")
    assert response.status_code == 200
