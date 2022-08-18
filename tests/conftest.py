import pytest
from selenium import webdriver
from sites.stones import Stones
import argparse


def pytest_emoji_passed(config):
    return " ", "PASSED  "


def pytest_emoji_failed(config):
    return " ", "FAILED  "


def pytest_addoption(parser):
    parser.addoption(
        "--local",
        default=False,
        action=argparse.BooleanOptionalAction,
        help="Test will be run locally",
    )
    parser.addoption(
        "--browser",
        default="chrome",
        help="Browser to use",
        choices=["chrome", "firefox", "edge"],
    )


@pytest.fixture(scope="function")
def driver(request):
    web_driver = None
    # Chrome
    if request.config.option.browser == "chrome":
        if request.config.option.local:
            web_driver = webdriver.Chrome()
        else:
            options = webdriver.ChromeOptions()
            web_driver = webdriver.Remote(
                command_executor="http://localhost:4444/wd/hub",
                options=options,
            )
    # Firefox
    elif request.config.option.browser == "firefox":
        if request.config.option.local:
            web_driver = webdriver.Firefox()
        else:
            options = webdriver.FirefoxOptions()
            web_driver = webdriver.Remote(
                command_executor="http://localhost:4444/wd/hub",
                options=options,
            )
    # Edge
    elif request.config.option.browser == "edge":
        if request.config.option.local:
            web_driver = webdriver.Edge()
        else:
            options = webdriver.EdgeOptions()
            web_driver = webdriver.Remote(
                command_executor="http://localhost:4444/wd/hub",
                options=options,
            )

    yield web_driver
    web_driver.quit()


@pytest.fixture(scope="function")
def stones(driver):
    return Stones(driver)
