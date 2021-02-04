import requests

url = 'https://l9njuzrhf3.execute-api.eu-west-1.amazonaws.com/prod/'
headers = {'x-api-key': 'GwMco9Tpstd5vbzBzlzW9I7hr6E1D7w2zEIrhOra'}


def get_user(number: int):
    return requests.get(url + 'user/' + str(number), headers=headers)


def get_user_or_group_by_id(userOrGroup: str, ids: int):
    return requests.get(url + userOrGroup + '/' + str(ids), headers=headers)


def test_valid_user():
    resp = get_user_or_group_by_id("user", 2)
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
    get_user(5)
    assert get_user(5).status_code == 404
