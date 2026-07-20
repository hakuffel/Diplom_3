import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_page import OrderPage


class TestOrderFeed:

    @allure.title("Клик по заказу в ленте открывает всплывающее окно с деталями")
    def test_click_order_opens_details(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_order_feed_link()
        order_page.click_feed_item(index=0)

        assert order_page.is_order_details_visible()

    @allure.title("Заказы пользователя из истории отображаются в ленте заказов")
    def test_order_from_history_in_feed(self, driver, order_flow):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        order_number = order_flow

        main_page.click_order_feed_link()
        feed_items = order_page.get_feed_items_text()

        assert any(order_number in item for item in feed_items)

    @allure.title("Счетчик 'Выполнено за все время' увеличивается после оформления заказа")
    def test_all_time_counter_increases(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_page = OrderPage(driver)
        payload, access_token = registered_user

        main_page.click_personal_account()
        login_page.set_email(payload['email'])
        login_page.set_password(payload['password'])
        login_page.click_login_button()

        main_page.click_order_feed_link()
        initial_count = order_page.get_completed_all_time()

        main_page.click_constructor_button()
        main_page.add_ingredient(index=0)
        main_page.add_ingredient(index=2)
        main_page.add_ingredient(index=6)
        main_page.click_order_button()
        main_page.close_modal()

        main_page.click_order_feed_link()
        updated_count = order_page.get_completed_all_time()

        assert updated_count > initial_count

    @allure.title("Счетчик 'Выполнено за сегодня' увеличивается после оформления заказа")
    def test_today_counter_increases(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_page = OrderPage(driver)
        payload, access_token = registered_user

        main_page.click_personal_account()
        login_page.set_email(payload['email'])
        login_page.set_password(payload['password'])
        login_page.click_login_button()

        main_page.click_order_feed_link()
        initial_count = order_page.get_completed_today()

        main_page.click_constructor_button()
        main_page.add_ingredient(index=0)
        main_page.add_ingredient(index=2)
        main_page.add_ingredient(index=6)
        main_page.click_order_button()
        main_page.close_modal()

        main_page.click_order_feed_link()
        updated_count = order_page.wait_completed_today_increase(initial_count)

        assert updated_count > initial_count

    @allure.title("Номер оформленного заказа появляется в ленте заказов")
    def test_order_appears_in_progress(self, driver, order_flow):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        order_number = order_flow

        main_page.click_order_feed_link()

        in_progress_numbers = order_page.get_orders_in_progress()
        ready_numbers = order_page.get_orders_ready()
        all_numbers = in_progress_numbers + ready_numbers

        assert any(num.lstrip('0') == order_number.lstrip('0') for num in all_numbers)
