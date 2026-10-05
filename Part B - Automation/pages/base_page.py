from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_elem(self, by, selector):
        return self.wait.until(
            EC.presence_of_element_located((by, selector))
        )

    def wait_for_clickable(self, by, selector):
        return self.wait.until(
            EC.element_to_be_clickable((by, selector))
        )
