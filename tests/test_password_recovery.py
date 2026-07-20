import allure
from data import FORGOT_PASSWORD_URL
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.restore_password_page import RestorePasswordPage
from helpers import generate_password


class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления пароля по кнопке 'Восстановить пароль'")
    def test_click_restore_password_link_opens_restore_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.click_personal_account()
        login_page.click_restore_password_link()

        assert FORGOT_PASSWORD_URL in main_page.get_current_url()

    @allure.title("Ввод почты и клик по кнопке 'Восстановить' открывает форму сброса пароля")
    def test_restore_password_with_email(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        restore_page = RestorePasswordPage(driver)
        payload, access_token = registered_user

        main_page.click_personal_account()
        login_page.click_restore_password_link()
        restore_page.set_email(payload['email'])
        restore_page.click_restore_button()

        assert restore_page.is_reset_page_displayed()

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_toggle_password_visibility_activates_field(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        restore_page = RestorePasswordPage(driver)
        payload, access_token = registered_user

        main_page.click_personal_account()
        login_page.click_restore_password_link()
        restore_page.set_email(payload['email'])
        restore_page.click_restore_button()
        restore_page.set_hidden_password(generate_password())
        restore_page.click_toggle_password_icon()

        assert restore_page.is_password_field_active()
