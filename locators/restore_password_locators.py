from selenium.webdriver.common.by import By


class RestorePasswordLocators:

    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")

    PASSWORD_INPUT_HIDDEN = (By.XPATH, "//div[contains(@class, 'input_type_password')]//input")
    PASSWORD_INPUT_VISIBLE = (By.XPATH, "//div[contains(@class, 'input_type_text')]//input")
    TOGGLE_PASSWORD_ICON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")

    RESET_PAGE_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")
