import requests

url = 'https://l9njuzrhf3.execute-api.eu-west-1.amazonaws.com/prod/'
headers = {'x-api-key': 'GwMco9Tpstd5vbzBzlzW9I7hr6E1D7w2zEIrhOra'}


def test_valid_user():
    resp = requests.get(url + 'user/2', headers=headers)
    assert resp.status_code == 200
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


def test_invalid_id():
    resp = requests.get(url + 'user/5', headers=headers)
    assert resp.status_code == 404