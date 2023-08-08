import requests

import pprint


def dtest_post_categories(Login_User, json_data):
    res = requests.post(
        "http://localhost:8080/api/category", json=json_data["category"]["post_category"][0],
         headers={"Authorization": "Bearer " + Login_User},
    )
    data = res.json()
    try:
        assert data["success"]
        pprint.pprint(data)

    except:
        print("ERROR: ", f"TITLE: {data['title']}", f"MESSAGE: {data['message']}")


def test_getAll_category():
    
    res = requests.get(
        "http://localhost:8080/api/category"
    )
    data = res.json()
    try:
        assert data["success"]
        pprint.pprint(data)

    except:
        print("ERROR: ", f"TITLE: {data['title']}", f"MESSAGE: {data['message']}")


