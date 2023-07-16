import pytest
import json
import requests

base_URL = "http://ums.devopsmcfinance.com/umsnode/ums/api/v1"
auth_endpoint = "/auth/login"
AccessToken="/access-token"
login_url = base_URL + auth_endpoint
payload = {"userCode": "M3084","userPass": "M3084","application": ["User Management System"]}
headers = {"Content-Type": "application/json"}
# Perform login and extract the refresh token
response = requests.post(login_url, json=payload, headers=headers)
response_data = response.json()
print(f"Endpoint: {auth_endpoint}")
print(f"Status Code: {response.status_code}")
refreshToken = response_data['data']['refreshToken']
login_url = base_URL +AccessToken
payload = {refreshToken}
response_data = response.json()
accessToken = response_data['data']['accessToken']
print(f"Endpoint: {AccessToken}")
print(f"Status Code: {response.status_code}")

# Test case for fetching APIs
@pytest.mark.parametrize("endpoint", [
    "/master/users",
    "/master/users",
    "/lookup/dashbaoard",
    "/master/application",
    "/master/branch",
    "/master/department/",
    "/master/designation/",
    "/master/department/",
    "/master/department/",
    "/master/product-type",
    "/master/product-type",
    "/master/product",
    "/master/product-type",
    "/master/product",
    "/master/scheme",
    "/master/product",
    "/master/program",
    "/master/product",
    "/master/menuevent",
    "/master/module",
    "/master/application",
    "/master/menu",
    "/master/application",
    "/master/group",
    "/master/role",
    "/master/users-v2",
    "/master/department/",
    "/master/designation",
    "/master/employee",
    "/master/department/",
    "/master/designation",
    "/user-mapping/program-scheme",
    "/master/program",
    "/master/scheme",
    "/user-mapping/branch-application",
    "/master/branch",
    "/master/application",
    "/master/menu",
    "/master/application",
    "/master/module",
    "/master/menuevent",
    "/user-mapping/branch-scheme",
    "/master/branch",
    "/master/scheme",
    "/master/menu",
    "/master/application",
    "/master/module",
    "/master/menuevent",
    "/user-mapping/menu-module-event/menu-modules/103",
    "/user-mapping/menu-module-event/module-events/58",
    "/user-mapping/group-event",
    "/master/group",
    "/master/application",
    "/user-mapping/menu-module-event/menu-event",
    "/user-mapping/role-group",
    "/master/role",
    "/master/group",
    "/user-mapping/user-branch",
    "/master/users",
    "/master/branch",
    "/user-mapping/user-product",
    "/master/users",
    "/master/product",
    "/user-mapping/user-application",
    "/master/users",
    "/master/application",
    "/user-mapping/user-role",
    "/master/users",
    "/master/role"
])
def test_api_request(endpoint):
    full_url = base_URL + endpoint
    headers = {"Authorization": "Bearer " + accessToken}

    try:
        if endpoint == "/lookup/dashbaoard":
            payload = {
                "users_id": 187
            }
            response = requests.post(full_url, json=payload, headers=headers)
        elif endpoint == "/master/department":
            response = requests.delete(full_url, headers=headers)
        else:
            response = requests.get(full_url, headers=headers)

        response.raise_for_status()  # Raise an exception for non-2xx status codes
        response_data = response.json()

        print(f"Endpoint: {endpoint}")
        print(f"Status Code: {response.status_code}")
        # print(f"Response: {response_data}")
        # print()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred for endpoint: {endpoint}")
        print(f"Error message: {str(e)}")
        # print()

    if response.status_code == 200:
        print("This API has been run successfully 😊")
    else:
        print("Not fetched. Please try again.🥲😔😔")

# Execute the tests
if __name__ == '__main__':
    pytest.main()
