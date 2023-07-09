import json
import requests
import pytest

base_URL = "http://ums.devopsmcfinance.com/umsnode/ums/api/v1"
auth_endpoint = "/auth/login"

login_url = base_URL + auth_endpoint
payload = {
    "userCode": "M3084",
    "userPass": "M3084",
    "application": ["User Management System"]
}
headers = {"Content-Type": "application/json"}

# Perform login and extract the refresh token
response = requests.post(login_url, json=payload, headers=headers)
response_data = response.json()
refresh_token = response_data['data']['accessToken']

ENDPOINT_LIST = [
]

for endpoint in ENDPOINT_LIST:
    full_url = base_URL + endpoint
    headers = {"Authorization": "Bearer " + refresh_token}

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
        print()

    except requests.exceptions.RequestException as e:
        print(f"Error occurred for endpoint: {endpoint}")
        print(f"Error message: {str(e)}")

