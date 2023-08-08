import requests

import pprint


def dtest_post_user(json_data):
    res = requests.post(
        "http://localhost:8080/api/user", json=json_data["user"]["post_user"][2]
    )
    data = res.json()
    try:
        assert data["success"]
        pprint.pprint(data)

    except:
        print("ERROR: ", f"TITLE: {data['title']}", f"MESSAGE: {data['message']}")


def test_getAll_User(Login_User):
    res = requests.get(
        "http://localhost:8080/api/user",
        headers={"Authorization": "Bearer " + Login_User},
    )
    data = res.json()
    try:
        assert data["success"]
        pprint.pprint(data)

    except:
        print("ERROR: ", f"TITLE: {data['title']}", f"MESSAGE: {data['message']}")


def dtest_update_admin(Login_User,json_data):
    id=json_data['user']['id']
    res = requests.put(
        "http://localhost:8080/api/user/promoteToAdmin",
        headers={"Authorization": "Bearer " + Login_User},params={'id':id}
    )
    data = res.json()
    try:
        assert data["success"]
        pprint.pprint(data)

    except:
        print("ERROR: ", f"TITLE: {data['title']}", f"MESSAGE: {data['message']}")
