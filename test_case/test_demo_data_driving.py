import requests
import json

# 从配置文件夹获取测试配置
with open("config/config.json", "r") as json_file:
    config = json.load(json_file)

# 从测试数据文件夹获取接口请求数据
with open('data/request_data.json', 'r') as json_file:
    request_data = json.load(json_file)

# 从测试数据文件夹获取接口响应数据
with open('data/response_data.json', 'r') as json_file:
    response_data = json.load(json_file)


class TestPytestDemo:

    def test_get_demo(self):
        host = config.get("host")
        get_api = config.get("getAPI")
        get_api_response_data = response_data.get("getAPI")
        # 发起请求
        response = requests.get(host+get_api)
        # 断言
        assert response.status_code == 200
        assert response.json() == get_api_response_data

    def test_post_demo(self):
        host = config.get("host")
        post_api = config.get("postAPI")
        post_api_request_data = request_data.get("postAPI")
        post_api_response_data = response_data.get("postAPI")
        # 发起请求
        response = requests.post(host + post_api, post_api_request_data)
        # 断言
        assert response.status_code == 201
        assert response.json() == post_api_response_data
