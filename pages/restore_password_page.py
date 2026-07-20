import allure
from locators.restore_password_locators import RestorePasswordLocators
from pages.base_page import BasePage


class RestorePasswordPage(BasePage):

    @allure.step("Ввести email для восстановления пароля")
    def set_email(self, email):
        self.type_text(RestorePasswordLocators.EMAIL_INPUT, email)

    @allure.step("Кликнуть по кнопке 'Восстановить'")
    def click_restore_button(self):
        self.click_element(RestorePasswordLocators.RESTORE_BUTTON)

    @allure.step("Проверить открытие страницы восстановления пароля")
    def is_reset_page_displayed(self):
        return self.is_displayed(RestorePasswordLocators.RESET_PAGE_TITLE)

    @allure.step("Ввести пароль в скрытое поле")
    def set_hidden_password(self, password):
        self.type_text(RestorePasswordLocators.PASSWORD_INPUT_HIDDEN, password)

    @allure.step("Кликнуть по иконке показать/скрыть пароль")
    def click_toggle_password_icon(self):
        self.click_element(RestorePasswordLocators.TOGGLE_PASSWORD_ICON)

    @allure.step("Проверить активность поля пароля")
    def is_password_field_active(self):
        return self.is_displayed(RestorePasswordLocators.PASSWORD_INPUT_VISIBLE)
