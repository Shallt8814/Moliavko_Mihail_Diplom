import time


import allure
import pytest_check as check
from selenium.webdriver.common.by import By

from moliavko_m.diplom.locators.locators_the_way_we_work_page import TheWayWeWorkPage
from conftest import web_browser



@allure.story("Тест для проверки страницы The way we work")
@allure.feature('Тест для проверки пнг элементов')
def test_png_elements(web_browser):
    page = TheWayWeWorkPage(web_browser)
    page.btn_pip_up_cookies.click()
    element = web_browser.find_element(By.XPATH,'//div[@class="wp-block-columns has-2-columns is-layout-flex wp-container-core-columns-is-layout-2 wp-block-columns-is-layout-flex"]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(10)
    element = web_browser.find_element(By.XPATH,'//div[@class="wp-block-columns has-2-columns is-layout-flex wp-container-core-columns-is-layout-3 wp-block-columns-is-layout-flex"]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(10)
    elements_png = [
        page.png_1,
        page.png_2,
        page.png_3,
        page.png_4
    ]
    for elements in elements_png:
        with allure.step("проверка на видимость"):
            check.is_true(elements.is_visible())



@allure.story('Тест для проверки страницы The way we work')
@allure.feature('Тест для проверки текста')
def test_txt_elements(web_browser):
    page = TheWayWeWorkPage(web_browser)
    page.btn_pip_up_cookies.click()
    element = web_browser.find_element(By.XPATH,'//div[@class="wp-block-columns has-2-columns is-layout-flex wp-container-core-columns-is-layout-2 wp-block-columns-is-layout-flex"]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(10)
    element = web_browser.find_element(By.XPATH,'//div[@class="wp-block-columns has-2-columns is-layout-flex wp-container-core-columns-is-layout-3 wp-block-columns-is-layout-flex"]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(10)
    elements_txt_page = [
        page.txt_under_1_png,
        page.txt_under_2_png,
        page.txt_under_3_png,
        page.txt_under_4_png,
        page.txt_1_block_text_1,
        page.txt_1_block_text_2,
        page.txt_1_block_text_3,
        page.txt_1_block_text_4,
        page.txt_1_block_text_5,
        page.txt_1_block_text_6,
        page.txt_1_block_text_7,
        page.txt_1_block_text_8,
        page.txt_1_block_text_9,
        page.txt_1_block_text_10,
        page.txt_1_block_text_11,
        page.txt_1_block_text_12,
        page.txt_2_block_text_1,
        page.txt_2_block_text_2,
        page.txt_2_block_text_3,
        page.txt_2_block_text_4,
        page.txt_3_block_text_1,
        page.txt_3_block_text_2,
        page.txt_3_block_text_3,
        page.txt_4_block_text_1,
        page.txt_4_block_text_2,
        page.txt_4_block_text_3,
        page.txt_4_block_text_4
    ]
    for elements in elements_txt_page:
        with allure.step("проверка на видимость"):
            check.is_true(elements.is_visible())
        with allure.step("проверка элементы не пустые"):
            check.is_not_none(elements)