import pytest
import json
import json
import os

# def env_config(request):
#     environment = request.config.getoption("--environment")
#     if environment == "dev":
#         # 在开发环境中执行测试
#         pass
#     elif environment == "test":
#         # 在测试环境中执行测试
#         pass
#     elif environment == "prod":
#         # 在生产环境中执行测试
#         pass


@pytest.fixture(scope="session")
def env_config(request):
    # 根据命令行参数选择环境配置文件
    env = os.getenv('ENV', 'dev')
    with open(f'config/{env}_config.json', 'r') as config_file:
        config = json.load(config_file)
    return config


@pytest.fixture(scope="session")
def env_request_data(request):
    # 根据命令行参数选择环境request_data文件
    env = os.getenv('ENV', 'dev')
    with open(f'data/{env}_request_test_data.json', 'r') as request_data_file:
        request_data = json.load(request_data_file)
    return request_data


@pytest.fixture (scope="session")
def env_response_data(request):
    # 根据命令行参数选择环境response_data文件
    env = os.getenv('ENV', 'dev')
    with open(f'data/{env}_response_test_data.json', 'r') as response_data_file:
        response_data = json.load(response_data_file)
    return response_data
