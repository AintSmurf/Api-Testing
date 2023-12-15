import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture(scope="class")
def init_driver(request):
    path = os.environ.get('SELPATH')
    if not path:
        raise Exception(f"path must be set please execute the getpath.py."
                        "then copy the path you get in the terminal and set it in the addpath.ps1 ")
    else:
        service = Service(executable_path=path)
        driver = webdriver.Chrome(service=service)
    request.cls.driver = driver
    yield
    driver.quit()

    # supported_browsers = ['Chrome', 'ch','headlesschrome', 'firefox', 'ff'])

