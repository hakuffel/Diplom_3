import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_page import OrderPage


class TestMainPage:

    @allure.title("Переход по клику на 'Конструктор'")
    def test_click_constructor_opens_constructor(self, driver):
        main_page = MainPage(driver)

        main_page.click_order_feed_link()
        main_page.click_constructor_button()

        assert main_page.is_constructor_displayed()

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_click_order_feed_opens_feed(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_order_feed_link()

        assert order_page.is_feed_displayed()

    @allure.title("Клик на ингредиент открывает всплывающее окно с деталями")
    def test_click_ingredient_opens_modal(self, driver):
        main_page = MainPage(driver)

        main_page.click_ingredient(index=0)

        assert main_page.is_ingredient_modal_visible()

    @allure.title("Всплывающее окно с деталями ингредиента закрывается кликом по крестику")
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)

        main_page.click_ingredient(index=0)
        main_page.close_modal()

        assert main_page.is_modal_closed()

    @allure.title("Каунтер ингредиента увеличивается при добавлении в заказ")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)

        initial_count = main_page.get_ingredient_counter(index=0)
        main_page.add_ingredient(index=0)

        assert main_page.get_ingredient_counter(index=0) > initial_count

    @allure.title("Авторизованный пользователь может оформить заказ")
    def test_logged_user_can_place_order(self, driver, registered_user):
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

        assert main_page.is_order_modal_visible()
