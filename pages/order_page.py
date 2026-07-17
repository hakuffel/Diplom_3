import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Проверить отображение ленты заказов")
    def is_feed_displayed(self):
        return self.is_displayed(OrderPageLocators.ORDER_FEED_LIST)

    @allure.step("Проверить отображение истории заказов")
    def is_history_displayed(self):
        return self.is_displayed(OrderPageLocators.ORDER_HISTORY_LIST)

    @allure.step("Кликнуть по заказу в ленте")
    def click_feed_item(self, index=0):
        self.wait_overlay_gone()
        item = self.wait_all_present(OrderPageLocators.ORDER_FEED_ITEM)[index]
        self.click_with_fallback(item)

    @allure.step("Проверить открытие деталей заказа")
    def is_order_details_visible(self):
        return self.is_displayed(OrderPageLocators.ORDER_DETAILS_MODAL)

    @allure.step("Получить список заказов из ленты")
    def get_feed_items_text(self):
        items = self.wait_all_present(OrderPageLocators.ORDER_FEED_ITEM)
        return [item.text for item in items]

    @allure.step("Получить счетчик 'Выполнено за все время'")
    def get_completed_all_time(self):
        try:
            text = self.wait_until_visible(OrderPageLocators.COMPLETED_ALL_TIME).text
            return int(text)
        except (TimeoutException, ValueError):
            return 0

    @allure.step("Получить счетчик 'Выполнено за сегодня'")
    def get_completed_today(self):
        try:
            text = self.wait_until_visible(OrderPageLocators.COMPLETED_TODAY).text
            return int(text)
        except (TimeoutException, ValueError):
            return 0

    @allure.step("Дождаться увеличения счетчика 'Выполнено за сегодня'")
    def wait_completed_today_increase(self, initial_value, timeout=15):
        def _increased(_):
            return self.get_completed_today() > initial_value

        try:
            WebDriverWait(self.driver, timeout).until(_increased)
        except TimeoutException:
            pass
        return self.get_completed_today()

    @allure.step("Получить номера заказов из раздела 'В работе'")
    def get_orders_in_progress(self):
        try:
            items = self.wait_all_present(OrderPageLocators.ORDERS_IN_PROGRESS)
            return [item.text.strip() for item in items]
        except TimeoutException:
            return []

    @allure.step("Получить номера заказов из раздела 'Готовы'")
    def get_orders_ready(self):
        try:
            items = self.wait_all_present(OrderPageLocators.ORDERS_READY)
            return [item.text.strip() for item in items]
        except TimeoutException:
            return []
