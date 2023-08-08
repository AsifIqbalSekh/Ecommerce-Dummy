import pytest
import requests
import json

@pytest.fixture(scope='module')
def Login_User():

    res = requests.post(
        "http://localhost:8080/api/user/login",json={"email": "skasifiqbal786@gmail.com","password":"asif@123"},
    )
    data = res.json()
    try:
        assert data["success"] 
        TOKEN=data["access_token"]
        return TOKEN
    except:
        print('ERROR: ',f"TITLE: {data['title']}",f"MESSAGE: {data['message']}")

@pytest.fixture(scope='module')
def json_data():
    json_file=open('Data.json') 
    data = json.load(json_file)
    return data
    # print(data['user']['post_user'][0])
    

# json_data()