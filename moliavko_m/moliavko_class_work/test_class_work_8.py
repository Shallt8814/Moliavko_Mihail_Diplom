import time
import allure
import pytest_check as check

from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.story('проверка сайта')
@allure.feature('проверка чекбоксов')
def test_check_box():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.drom.ru/")

    driver.close()
    driver.quit()