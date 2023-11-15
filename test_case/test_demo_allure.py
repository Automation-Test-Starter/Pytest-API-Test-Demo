import requests


<<<<<<< HEAD:test_case/test_demo.py
class TestPytestDemo:
=======
@allure.title("Test example get endpoint")
@allure.description("Test the example get API endpoint")
def test_get_example_endpoint_allure(env_config, env_request_data, env_response_data):
    host = env_config["host"]
    get_api = env_config["getAPI"]
    get_api_request_data = env_request_data["getAPI"]
    print("make the request")
    get_api_response_data = env_response_data["getAPI"]
    # Your test code here
    response = requests.get(host+get_api)
    print("verify the response status code")
    assert response.status_code == 200
    print("verify the response data")
    assert response.json() == get_api_response_data
>>>>>>> bb894ee (update demo):test_case/test_demo_allure.py

    def test_get_demo(self):
        base_url = "https://jsonplaceholder.typicode.com"
        # 发起请求
        response = requests.get(f"{base_url}/posts/1")
        # 断言
        assert response.status_code == 200
        assert response.json()['userId'] == 1
        assert response.json()['id'] == 1

<<<<<<< HEAD:test_case/test_demo.py
    def test_post_demo(self):
        base_url = "https://jsonplaceholder.typicode.com"
        requests_data = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        # 发起请求
        response = requests.post(f"{base_url}/posts", requests_data)
        # 断言
        assert response.status_code == 201
        assert response.json()['userId'] == '1'
        assert response.json()['id'] == 101
=======
@allure.title("Test example POST endpoint")
@allure.description("Test the example POST API endpoint")
def test_post_example_endpoint_allure(env_config, env_request_data, env_response_data):
    host = env_config["host"]
    post_api = env_config["postAPI"]
    post_api_request_data = env_request_data["postAPI"]
    print("make the request")
    post_api_response_data = env_response_data["postAPI"]
    # Your test code here
    response = requests.post(host+post_api, json=post_api_request_data)
    print("verify the response status code")
    assert response.status_code == 201
    print("verify the response data")
    assert response.json() == post_api_response_data
>>>>>>> bb894ee (update demo):test_case/test_demo_allure.py
