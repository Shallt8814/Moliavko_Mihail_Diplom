import time
from selenium.webdriver.support.ui import Select

import allure
import pytest_check as check
from selenium.webdriver.common.by import By

from moliavko_m.diplom.locators.locators_stories_page import Stories
from conftest import web_browser


@allure.story("Тест для проверки страницы Stories")
@allure.feature('Тест для проверки txt элементов stories')
def test_txt_elements_stories(web_browser):
    page = Stories(web_browser)
    page.btn_pip_up_cookies.click()
    elements_txt = [
        (page.txt_stories,"Stories"),
        (page.txt_category, "Category"),
        (page.txt_sort_by, "Sort by"),
        (page.exp_card_text, "Post-COP29 reflections: A call to action for Funders"),
    ]
    for elements, elements_text in elements_txt:
        with allure.step("проверка видимости и текста"):
             check.is_true(elements.is_visible())
             check.is_not_none(elements.get_text())
             check.equal(elements.get_text(), elements_text)
    with allure.step("проверка количества карточек"):
         check.equal(page.stories_cards.count(), 12)



@allure.story("Тест для проверки страницы Stories")
@allure.feature('Тест для проверки select элементов stories')
def test_select_elements_stories(web_browser):
    page = Stories(web_browser)
    page.btn_pip_up_cookies.click()
    exp = Select(web_browser.find_element(By.XPATH, '//select[@name="category"]'))
    exp.select_by_visible_text("Blog")
    time.sleep(1)
    exp = Select(web_browser.find_element(By.XPATH, '//select[@name="orderby"]'))
    exp.select_by_visible_text("Author A-Z")
    time.sleep(2)
    with allure.step("проверка видимости и текста"):
         check.is_true(page.searched_element.is_visible())
         check.equal(page.searched_element.get_text(), "Emergency grants help Save the Children support children when they most need it")



@allure.story("Тест для проверки страницы Stories")
@allure.feature('Тест для проверки btn элементов stories')
def test_btn_elements_stories(web_browser):
    page = Stories(web_browser)
    page.btn_pip_up_cookies.click()
    x_coordinate = 0
    y_coordinate = 1700
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(2)
    page.btn_2_page.click()
    time.sleep(2)
    with allure.step("проверка работоспособности кнопки"):
        check.equal(page.searched_pagination_element.get_text(),'"More funding is needed for the just transition to sustainable buildings."')
    x_coordinate = 0
    y_coordinate = 1700
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(2)
    page.btn_1_page.click()
    time.sleep(2)
    with allure.step("проверка работоспособности кнопки"):
         check.equal(page.exp_card_text.get_text(), "Post-COP29 reflections: A call to action for Funders")
    x_coordinate = 0
    y_coordinate = 1700
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(2)
    page.btn_next.click()
    time.sleep(2)
    with allure.step("проверка работоспособности кнопки"):
        check.equal(page.searched_pagination_element.get_text(),'"More funding is needed for the just transition to sustainable buildings."')
    x_coordinate = 0
    y_coordinate = 1700
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(2)
    page.btn_previous.click()
    time.sleep(2)
    with allure.step("проверка работоспособности кнопки"):
         check.equal(page.exp_card_text.get_text(), "Post-COP29 reflections: A call to action for Funders")
    x_coordinate = 0
    y_coordinate = 1500
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(10)



@allure.story("Тест для проверки страницы Stories")
@allure.feature('Тест для проверки exp card элементов stories')
def test_exp_card_elements_stories(web_browser):
    page = Stories(web_browser)
    page.btn_pip_up_cookies.click()
    with allure.step("проверка кнопки карточки на ссылку и кликабельность, титла карточки на текст и видимость"):
         check.is_true(page.exp_card_btn.is_clickable())
         check.equal(page.exp_card_btn.get_attribute("href"), "https://ikeafoundation.org/stories/post-cop29-reflections-a-call-to-action-for-funders/")
         check.is_true(page.exp_card_text.is_visible())
         check.equal(page.exp_card_text.get_text(), "Post-COP29 reflections: A call to action for Funders")



