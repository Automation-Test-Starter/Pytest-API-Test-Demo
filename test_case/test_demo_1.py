import requests


class TestPytestDemo:

    def test_get_demo(self):
        base_url = "https://jsonplaceholder.typicode.com"
        # 发起请求
        response = requests.get(f"{base_url}/posts/1")
        # 断言
        assert response.status_code == 200
        assert response.json()['userId'] == 1
        assert response.json()['id'] == 1

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