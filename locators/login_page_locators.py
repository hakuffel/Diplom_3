from selenium.webdriver.common.by import By


class LoginPageLocators:

    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history']")
    PROFILE_LINK = (By.XPATH, "//a[@href='/account/profile']")
