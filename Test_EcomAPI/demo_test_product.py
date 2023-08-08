import requests

import pprint


def test_post_product(Login_User, json_data):
    res = requests.post(
        "http://localhost:8080/api/product",
        headers={"Authorization": "Bearer " + Login_User},
        json=json_data["product"]["post_product"][3],
    )
    data = res.json()
    try:
        assert data["success"]
        pprint.pprint(data)

    except:
        print("ERROR: ", f"TITLE: {data['title']}", f"MESSAGE: {data['message']}")


def test_getAll_product():
    res = requests.get("http://localhost:8080/api/product")
    data = res.json()
    try:
        assert data["success"]
        pprint.pprint(data)

    except:
        print("ERROR: ", f"TITLE: {data['title']}", f"MESSAGE: {data['message']}")
