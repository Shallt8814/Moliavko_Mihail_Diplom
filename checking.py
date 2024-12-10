import time
from time import sleep

import allure
import pytest_check as check

from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.story('проверка')
@allure.feature('проверка')
def test_check_box():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://goldenmotors.by/")
    driver.find_element(By.XPATH, '//*[@data-cky-tag="accept-button"]').click()

    #driver.find_element(By.XPATH,'')

    driver.find_element(By.XPATH, '(//a[@class="elementor-item has-submenu"])[1]').is_displayed()


    time.sleep(1)
    driver.close()
    driver.quit()