
'''
******************************Please go through ReadMe.txt and main.py before run the project**********************************

Select Default Testing Environment As pytest and change directory(cd) to "Test_Requirmrnt_API" from project directory 
where  "test_requirmentAPI.py" resides and Run cmd => "pytest -s test_requirmentAPI.py"
For Html Report Generation Run cmd =>"pytest test_requirmentAPI.py --html=report_test_requirmentAPI.html"

Or You can run test file via Pytest TestRunner

'''

import requests
import pytest
import pprint


# *******************************  User Control Endpoint Test ******************************************** #

########### ADMIN Control: Create User Test ###############


def test_getAll_Order(Login_User):

    res = requests.get(
        "http://localhost:8080/api/order",headers={'Authorization': 'Bearer ' + Login_User}
    )
    data = res.json()
    try:
        assert data["success"] 
        pprint.pprint(data)

    except:
        print('ERROR: ',f"TITLE: {data['title']}",f"MESSAGE: {data['message']}")
       
       
    