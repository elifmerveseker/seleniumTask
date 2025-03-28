from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def hover_element(self, *locator):
        element = self.driver.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def get_current_url(self):
        return self.driver.current_url

    def wait_element(self, method, message=''):
        return self.wait.until(ec.element_to_be_clickable(method), message)

    def get_text(self, locator):
        return self.wait_element(locator).text

    def verify_element_visibility(self, locator, message=''):
        return self.wait.until(ec.visibility_of_element_located(locator), message)

    def go_to_url(self, url):
        self.driver.get(url)
