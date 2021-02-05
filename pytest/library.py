import requests
import string
import random

url = 'https://l9njuzrhf3.execute-api.eu-west-1.amazonaws.com/prod/'
headers = {'Content-Type': 'application/json', 'x-api-key': 'GwMco9Tpstd5vbzBzlzW9I7hr6E1D7w2zEIrhOra'}


def get_user_or_group_by_id(userOrGroup: str, ids: int):
    return requests.get(url + userOrGroup + '/' + str(ids), headers=headers)


def test_get_all_group():
    resp = get_user_or_group_by_id("group", 2)
    resBody = resp.json()
    assert resp.status_code == 200
    assert resBody["name"] == "Denis's Group"


def name_generator(chars=string.ascii_uppercase):
    size = random_int()
    return ''.join(random.choice(chars) for _ in range(size))


def random_int():
    return random.randint(2, 53)


def email_generator(y):
    return ''.join(random.choice(string.ascii_letters) for _ in range(y)) + "@gmail.com"


def roles_generator():
    return random.randint(0, 5)


print(roles_generator())
