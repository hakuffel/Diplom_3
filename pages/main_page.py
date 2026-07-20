import allure
from selenium.common.exceptions import TimeoutException
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Кликнуть по кнопке 'Конструктор'")
    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть по ссылке 'Лента Заказов'")
    def click_order_feed_link(self):
        self.click_element(MainPageLocators.ORDER_FEED_LINK)

    @allure.step("Кликнуть по кнопке 'Личный Кабинет'")
    def click_personal_account(self):
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Проверить отображение конструктора")
    def is_constructor_displayed(self):
        return self.is_displayed(MainPageLocators.TARGET_AREA)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self, index=0):
        self.wait_overlay_gone()
        ingredient = self.wait_all_present(MainPageLocators.INGREDIENT)[index]
        self.click_with_fallback(ingredient)

    @allure.step("Проверить видимость окна с деталями ингредиента")
    def is_ingredient_modal_visible(self):
        return self.is_displayed(MainPageLocators.MODAL_WINDOW)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click_element(MainPageLocators.CLOSE_MODAL_BUTTON)

    @allure.step("Проверить, что модальное окно закрыто")
    def is_modal_closed(self):
        try:
            self.wait_until_invisible(MainPageLocators.MODAL_WINDOW, timeout=5)
            return True
        except TimeoutException:
            return False

    @allure.step("Получить значение каунтера ингредиента")
    def get_ingredient_counter(self, index=0):
        try:
            counters = self.wait_all_present(MainPageLocators.INGREDIENT_COUNTER)
            return int(counters[index].text.strip())
        except (TimeoutException, ValueError, IndexError):
            return 0

    @allure.step("Добавить ингредиент в заказ")
    def add_ingredient(self, index=0):
        self.wait_overlay_gone()
        ingredient = self.wait_all_present(MainPageLocators.INGREDIENT)[index]
        target = self.wait_until_present(MainPageLocators.TARGET_AREA)
        self.drag_and_drop(ingredient, target)

    @allure.step("Нажать кнопку 'Оформить заказ'")
    def click_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)

    @allure.step("Проверить видимость окна с номером заказа")
    def is_order_modal_visible(self):
        return self.is_displayed(MainPageLocators.MODAL_WINDOW)

    @allure.step("Получить номер заказа из модального окна")
    def get_order_number(self, timeout=15):
        try:
            def _order_ready(_driver):
                text = self.get_element_text(MainPageLocators.ORDER_NUMBER_TEXT)
                return text.isdigit() and text != '9999'

            self.wait_for_condition(_order_ready, timeout)
            return self.get_element_text(MainPageLocators.ORDER_NUMBER_TEXT)
        except TimeoutException:
            return ''
