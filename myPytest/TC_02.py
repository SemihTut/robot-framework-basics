import random

from myPytest import myLibrary

url = 'https://l9njuzrhf3.execute-api.eu-west-1.amazonaws.com/prod/'
headers = {'x-api-key': 'GwMco9Tpstd5vbzBzlzW9I7hr6E1D7w2zEIrhOra'}


def test_valid_id_for_user():
    resp = myLibrary.get_user(random.randint(0, 4))
    resBody = resp.json()
    first_name = resBody["first_name"]
    last_name = resBody["last_name"]
    email = resBody["email"]
    roles = resBody["roles"]
    created = resBody["created"]
    groupId = resBody["group_id"]
    createdBy = resBody["created_by"]
    isinstance(first_name, str)
    isinstance(last_name, str)
    isinstance(email, str)
    isinstance(roles, list)
    isinstance(created, str)
    isinstance(groupId, int)
    isinstance(createdBy, int)
    assert resp.status_code == 200


def test_invalid_id_for_user():
    response = myLibrary.get_user(random.randint(4, 50))
    assert response.status_code == 404
