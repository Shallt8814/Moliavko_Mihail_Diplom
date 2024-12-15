import time
import pytest_check as check
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_check_box():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://ikeafoundation.org/")


    driver.close()
    driver.quit()