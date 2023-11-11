

## 项目目录结构
    
```text
Pytest-allure-demo/
    ├── tests/                  # 存放测试用例文件
    │   ├── test_login.py       # 示例测试用例文件
    │   ├── test_order.py       # 示例测试用例文件
    │   └── ...
    ├── data/                   # 存放测试数据文件（如 JSON、CSV 等）
    │   ├── dev_test_data.json      # 开发环境测试数据文件
    │   ├── prod_test_data.json      # 生产环境测试数据文件
    │   ├── ...
    ├── config/
    │   ├── dev_config.json  # 开发环境配置文件
    │   ├── prod_config.json  # 生产环境配置文件
    │   ├── ...
    ├── conftest.py             # Pytest 的全局配置文件
    ├── pytest.ini              # Pytest 配置文件
    ├── requirements.txt        # 项目依赖项文件
    └── allure-report/          # 存放 Allure 报告
```