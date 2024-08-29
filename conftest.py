import os
from selenium import webdriver
import pytest
import logging as Logger
from backend.src.utilities.dbUtility import DBUtility

@pytest.fixture(scope="class")
def init_driver(request):
    Logger.info("initializing the driver ....")
    driver = webdriver.Chrome()
    driver.maximize_window()
    assert driver is not None, "Failed to initialize the driver"
    request.cls.driver = driver
    yield
    driver.quit()

def tear_down():
    Logger.info("closing db connections")
    DBUtility.close_connection()

def pytest_sessionfinish(session, exitstatus):
    tear_down()