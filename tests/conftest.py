import logging
import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logger = logging.getLogger(__name__)

from Utils import attach

# load_dotenv()
#
# selenoid_login = os.getenv("SELENOID_LOGIN")
# selenoid_pass = os.getenv("SELENOID_PASS")
# selenoid_url = os.getenv("SELENOID_URL")
#
# @pytest.fixture(scope="session", autouse=True)
# def selenoid():
#     options = Options()
#     selenoid_capabilities = {
#         "browserName": "chrome",
#         "browserVersion": "127.0",
#         "selenoid:options": {
#             "enableVNC": True,
#             "enableVideo": True
#         }
#     }
#
#     selenoid_full_url = f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub"
#
#     options.capabilities.update(selenoid_capabilities)
#     driver = webdriver.Remote(
#         command_executor=selenoid_full_url,
#         options=options)
#
#     browser.config.driver = driver
#     yield
#     attach.add_html(browser)
#     attach.add_logs(browser)
#     attach.add_video(browser)
#     attach.add_screenshot(browser)


@pytest.fixture(scope='session', autouse=True)
def browser_manager():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.base_url = "https://mybook.ru/"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()
