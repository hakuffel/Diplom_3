from selenium.webdriver.common.by import By


class MainPageLocators:

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    ORDER_FEED_LINK = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']/parent::a")

    INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")
    INGREDIENT_COUNTER = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]//p[contains(@class, 'counter__num')]")
    TARGET_AREA = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")

    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")

    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER_TEXT = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title') and contains(@class, 'text_type_digits-large')]")

    OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
