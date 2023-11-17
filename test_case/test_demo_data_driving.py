import requests
import json

# get config file from config.json
with open("config/config.json", "r") as json_file:
    config = json.load(json_file)

# get request_data from data folder
with open('data/request_data.json', 'r') as json_file:
    request_data = json.load(json_file)

# get response_data from data folder
with open('data/response_data.json', 'r') as json_file:
    response_data = json.load(json_file)


class TestPytestDataDrivingDemo:

    def test_get_demo_data_driving(self):
        host = config.get("host")
        get_api = config.get("getAPI")
        get_api_response_data = response_data.get("getAPI")
        # send request
        response = requests.get(host+get_api)
        # assert
        assert response.status_code == 200
        assert response.json() == get_api_response_data

    def test_post_demo_data_driving(self):
        host = config.get("host")
        post_api = config.get("postAPI")
        post_api_request_data = request_data.get("postAPI")
        post_api_response_data = response_data.get("postAPI")
        # send request
        response = requests.post(host + post_api, post_api_request_data)
        # assert
        assert response.status_code == 201
        assert response.json() == post_api_response_data
