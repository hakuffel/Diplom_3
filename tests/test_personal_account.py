import allure
from data import ACCOUNT_URL, ORDER_HISTORY_URL, LOGIN_URL
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestPersonalAccount:

    @allure.title("Переход по клику на 'Личный кабинет'")
    def test_click_personal_account_opens_account_page(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        payload, access_token = registered_user

        main_page.click_personal_account()
        login_page.set_email(payload['email'])
        login_page.set_password(payload['password'])
        login_page.click_login_button()

        main_page.click_personal_account()
        main_page.wait_url_contains('account')

        assert ACCOUNT_URL in main_page.get_current_url()

    @allure.title("Переход в раздел 'История заказов'")
    def test_click_order_history_opens_history_page(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        payload, access_token = registered_user

        main_page.click_personal_account()
        login_page.set_email(payload['email'])
        login_page.set_password(payload['password'])
        login_page.click_login_button()
        main_page.click_personal_account()
        main_page.wait_url_contains('account')
        login_page.click_order_history_link()

        assert ORDER_HISTORY_URL in main_page.get_current_url()

    @allure.title("Выход из аккаунта")
    def test_logout_returns_to_login_page(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        payload, access_token = registered_user

        main_page.click_personal_account()
        login_page.set_email(payload['email'])
        login_page.set_password(payload['password'])
        login_page.click_login_button()
        main_page.click_personal_account()
        login_page.click_logout_button()

        assert LOGIN_URL in main_page.get_current_url()
