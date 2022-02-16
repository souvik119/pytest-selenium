import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
from pathlib import Path

folder_path = str(Path(__file__).parents[0].parents[0])

@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome(os.path.join(folder_path, 'drivers', 'chromedriver'))
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


@pytest.mark.usefixtures("chrome_driver_init")
class BasicLoginTest:
    pass

class TestSiteLogin(BasicLoginTest):
    def test_demo_site_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        assert 'OrangeHRM' == self.driver.title