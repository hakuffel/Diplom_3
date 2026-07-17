from selenium.webdriver.common.by import By


class OrderPageLocators:

    ORDER_FEED_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]")
    ORDER_FEED_ITEM = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]")
    ORDER_HISTORY_LIST = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]")

    ORDER_DETAILS_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")

    COMPLETED_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    COMPLETED_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

    ORDERS_IN_PROGRESS = (By.XPATH, "//p[contains(text(), 'В работе')]/following::ul[1]/li")
    ORDERS_READY = (By.XPATH, "//p[contains(text(), 'Готовы')]/following::ul[1]/li")
