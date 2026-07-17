import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Ввести email")
    def set_email(self, email):
        self.type_text(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step("Ввести пароль")
    def set_password(self, password):
        self.type_text(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Кликнуть по кнопке 'Войти'")
    def click_login_button(self, timeout=15):
        current_url = self.driver.current_url
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
        WebDriverWait(self.driver, timeout).until(lambda d: d.current_url != current_url)

    @allure.step("Кликнуть по ссылке 'Восстановить пароль'")
    def click_restore_password_link(self):
        self.click_element(LoginPageLocators.RESTORE_PASSWORD_LINK)

    @allure.step("Кликнуть по ссылке 'История заказов'")
    def click_order_history_link(self):
        self.click_element(LoginPageLocators.ORDER_HISTORY_LINK)

    @allure.step("Кликнуть по кнопке 'Выход'")
    def click_logout_button(self, timeout=15):
        self.click_element(LoginPageLocators.LOGOUT_BUTTON)
        WebDriverWait(self.driver, timeout).until(EC.url_contains('login'))

    @allure.step("Проверить открытие личного кабинета")
    def is_profile_displayed(self):
        return self.is_displayed(LoginPageLocators.PROFILE_LINK)
