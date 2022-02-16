from selenium import webdriver
import os
from pathlib import Path
import time

folder_path = str(Path(__file__).parents[0])

def test_my_very_first_test():
    driver = webdriver.Chrome(os.path.join(folder_path, 'chromedriver'))
    driver.get("http://www.google.com")
    time.sleep(3)