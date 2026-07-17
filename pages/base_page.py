from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_until_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_until_present(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_all_present(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def wait_until_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_until_invisible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_url_contains(self, text, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))

    def get_current_url(self):
        return self.driver.current_url

    def is_displayed(self, locator, timeout=5):
        try:
            return self.wait_until_visible(locator, timeout).is_displayed()
        except TimeoutException:
            return False

    def wait_overlay_gone(self, timeout=3):
        try:
            self.wait_until_invisible(MainPageLocators.OVERLAY, timeout)
        except TimeoutException:
            pass

    def click_with_fallback(self, element):
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def click_element(self, locator, timeout=10):
        self.wait_overlay_gone()
        element = self.wait_until_clickable(locator, timeout)
        self.click_with_fallback(element)

    def type_text(self, locator, text, timeout=10):
        self.wait_overlay_gone()
        field = self.wait_until_clickable(locator, timeout)
        field.clear()
        field.send_keys(text)

    def drag_and_drop(self, source_element, target_element):
        script = """
            var source = arguments[0];
            var target = arguments[1];
            var dataTransfer = new DataTransfer();
            source.dispatchEvent(new DragEvent('dragstart', {bubbles: true, cancelable: true, dataTransfer: dataTransfer}));
            target.dispatchEvent(new DragEvent('drop', {bubbles: true, cancelable: true, dataTransfer: dataTransfer}));
            source.dispatchEvent(new DragEvent('dragend', {bubbles: true, cancelable: true, dataTransfer: dataTransfer}));
        """
        self.driver.execute_script(script, source_element, target_element)
