import requests
import json
import csv
import pytest
from myPytest import myLibrary

url = 'https://l9njuzrhf3.execute-api.eu-west-1.amazonaws.com/prod/'
headers = {'Content-Type': 'application/json', 'x-api-key': 'GwMco9Tpstd5vbzBzlzW9I7hr6E1D7w2zEIrhOra'}

def test_post_headers_body_json():
    # Body
    payload = {'first_name': 'Setu', 'last_name': 'Timo', 'email': 'test@example.com', 'roles': [0], 'group_id': 1}

    #data=json.dumps(payload)
    # convert dict to json string by json.dumps() for body data.
    resp = requests.post(url+'user', headers=headers, data=json.dumps(payload))

    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body["first_name"] == "Setu"


def read_test_data_from_csv():
    test_data = []
    with open('test_data/test_data_zip_codes.csv', newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        next(data)  # skip header row
        for row in data:
            test_data.append(row)
    return test_data


@pytest.mark.parametrize("first_name, last_name, email, roles, group_id", read_test_data_from_csv())
def test_using_csv_get_location_data_check_place_name(first_name, last_name, email, roles, group_id):
    payload = {'first_name': first_name, 'last_name': last_name, 'email': email, 'roles': [int(roles)], 'group_id': int(group_id)}
    response = requests.post(url+'user', headers=headers, data=json.dumps(payload))
    assert response.status_code == 200
    resp_body = response.json()
    assert resp_body["first_name"] == first_name
