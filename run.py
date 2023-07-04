import os
import time

import allure
import pytest

if __name__ == '__main__':
    pytest.main(["-sv", "./test_login.py",
                 "--alluredir", "./result"])
    os.system("allure generate ./result -o ./report --clean")
