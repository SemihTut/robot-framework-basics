import requests
from myPytest import myLibrary


def test_get_all_group():
    resp = requests.get(myLibrary.url+"group", headers=myLibrary.headers)
    resBody = resp.json()
    assert resp.status_code == 200
    name = resBody["name"]
    print(name)



