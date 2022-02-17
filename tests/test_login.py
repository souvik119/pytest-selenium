import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from pathlib import Path
import time

folder_path = str(Path(__file__).parents[0].parents[0])

@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome(os.path.join(folder_path, 'drivers', 'chromedriver'))
    request.cls.driver = chrome_driver
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield
    chrome_driver.close()


@pytest.mark.usefixtures("chrome_driver_init")
class BasicLoginTest:
    pass

class TestSiteLogin(BasicLoginTest):
    def test_demo_site_title(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        assert 'OrangeHRM' == self.driver.title

    def test_valid_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
        self.driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
        self.driver.find_element(By.ID, 'btnLogin').click()
        time.sleep(3)
        self.driver.find_element(By.ID, 'welcome').click()
        self.driver.find_element(By.LINK_TEXT, 'Logout').click()
        time.sleep(3)

    def test_invalid_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
        self.driver.find_element(By.ID, 'txtPassword').send_keys('xdwfe12')
        self.driver.find_element(By.ID, 'btnLogin').click()
        time.sleep(2)
        assert self.driver.find_element(By.ID, 'spanMessage').text == 'Invalid credentials'

    def test_forgot_password_link(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.LINK_TEXT, 'Forgot your password?').click()
        time.sleep(2)
        self.driver.find_element(By.ID, 'btnCancel').click()
        time.sleep(2)