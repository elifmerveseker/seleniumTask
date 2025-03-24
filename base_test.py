import unittest
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def init_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return logger


class BaseTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.logger = init_logger()

    def take_screenshot(self, test_status):
        filename = f"test_result_{test_status}.png"
        self.driver.save_screenshot(filename)

    def tearDown(self):
        self.driver.quit()
