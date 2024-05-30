import os
from pathlib import Path
import allure
import pytest
from selene import browser
from appium import webdriver
from selene_in_action.utils import allure as allure_utils
from dotenv import load_dotenv


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="bstack",
        help="Specify the test context"
    )


def pytest_configure(config):
    context = config.getoption('--context')
    current_dir = Path(__file__).parent.parent
    env_file = os.path.join(current_dir, f'.env.{context}')
    load_dotenv(env_file)


@pytest.fixture
def context(request):
    return request.config.getoption('--context')


@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):
    from config import config
    options = config.to_driver_options(context=context)

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            config.remote_url,
            options=options
        )

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

    session_id = browser.driver.session_id

    with allure.step('tear down app session with id:' + session_id):
        browser.quit()

    if context == 'bstack':
        allure_utils.attach_bstack_video(session_id)