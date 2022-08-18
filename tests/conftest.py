import pytest
from selenium import webdriver
from sites.stones import Stones


@pytest.fixture(scope="function")
def driver():
    chrome = webdriver.Chrome()
    yield chrome
    chrome.close()


@pytest.fixture(scope="function")
def stones(driver):
    return Stones(driver)
