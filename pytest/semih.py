import csv
import json
import pytest
import requests

url = 'https://l9njuzrhf3.execute-api.eu-west-1.amazonaws.com/prod/'
headers = {'Content-Type': 'application/json', 'x-api-key': 'GwMco9Tpstd5vbzBzlzW9I7hr6E1D7w2zEIrhOra'}


def test_get_users():
    # Additional headers.
    resp = requests.get(url + 'user', headers=headers)
    resBody = resp.json()
    first_name = resBody["0"]["first_name"]
    last_name = resBody["0"]["last_name"]
    email = resBody["0"]["email"]
    roles = resBody["0"]["roles"]
    created = resBody["0"]["created"]
    groupId = resBody["0"]["group_id"]
    createdBy = resBody["0"]["created_by"]
    isinstance(first_name, str)
    isinstance(last_name, str)
    isinstance(email, str)
    isinstance(roles, list)
    isinstance(created, str)
    isinstance(groupId, int)
    isinstance(createdBy, int)



