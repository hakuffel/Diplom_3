import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from data import BASE_URL, API_BASE_URL, REGISTER_ENDPOINT, USER_ENDPOINT
from helpers import generate_email, generate_password, generate_name
from pages.main_page import MainPage
from pages.login_page import LoginPage


@pytest.fixture(scope='session')
def chrome_driver_path():
    return ChromeDriverManager().install()


@pytest.fixture(scope='session')
def firefox_driver_path():
    return GeckoDriverManager().install()


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request, chrome_driver_path, firefox_driver_path):
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        service = ChromeService(chrome_driver_path)
        browser = webdriver.Chrome(service=service, options=options)
    else:
        options = webdriver.FirefoxOptions()
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        service = FirefoxService(firefox_driver_path)
        browser = webdriver.Firefox(service=service, options=options)

    browser.get(BASE_URL)
    yield browser
    browser.quit()


@pytest.fixture
def registered_user():
    payload = {
        'email': generate_email(),
        'password': generate_password(),
        'name': generate_name()
    }
    response = requests.post(f'{API_BASE_URL}{REGISTER_ENDPOINT}', json=payload, timeout=10)
    access_token = response.json().get('accessToken')

    yield payload, access_token

    if access_token:
        requests.delete(
            f'{API_BASE_URL}{USER_ENDPOINT}',
            headers={'Authorization': access_token},
            timeout=10
        )


@pytest.fixture
def order_flow(driver, registered_user):

    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    payload, access_token = registered_user

    main_page.click_personal_account()
    login_page.set_email(payload['email'])
    login_page.set_password(payload['password'])
    login_page.click_login_button()

    main_page.add_ingredient(index=0)
    main_page.add_ingredient(index=2)
    main_page.add_ingredient(index=6)
    main_page.click_order_button()
    order_number = main_page.get_order_number()
    main_page.close_modal()

    return order_number
