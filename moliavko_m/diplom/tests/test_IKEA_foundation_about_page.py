import time


import allure
import pytest_check as check
from selenium.webdriver.common.by import By

from moliavko_m.diplom.locators.locators_IKEA_foundation_about_page import IkeaFoundationAboutPage
from conftest import web_browser

@allure.story('Проверка страницы о Ikea Foundation')
@allure.feature('Тест для проверки титульного текста')
def test_headers(web_browser):
    page = IkeaFoundationAboutPage(web_browser)
    page.btn_pip_up_сookies.click()
    elements_main = [
        (page.txt_main_text,"A better everyday life"),
        (page.txt_main_our_vision,"Our vision is to create a better everyday life for the many people.")
    ]
    for elements, elements_text in elements_main:
        with allure.step("проверка на видимость"):
            check.is_true(elements.is_visible())
        with allure.step("проверка совпадения теста"):
            check.equal(elements.get_text(), elements_text)



@allure.story('Проверка страницы о Ikea Foundation')
@allure.feature('Тест для проверки текста о компании и титульного фото')
def test_txt_company(web_browser):
    page = IkeaFoundationAboutPage(web_browser)
    page.btn_pip_up_сookies.click()
    element = web_browser.find_element(By.XPATH, '(//img[@decoding="async"])[1]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(2)
    elements_about = [
        page.txt_african_people_discription,
        page.txt_about_ikea_foundation
    ]
    for elements in elements_about:
        with allure.step("проверка на видимость"):
            check.is_true(elements.is_visible())
        with allure.step("проверка что элементы не пустые"):
            check.is_not_none(elements)
    with allure.step("проверка картинки на размеры и видимость"):
        check.is_true(page.img_african_people.is_visible())
        check.equal(page.img_african_people.get_attribute("width"),'1024')
        check.equal(page.img_african_people.get_attribute("height"),'683')

@allure.story('Проверка страницы о Ikea Foundation')
@allure.feature('Тест для проверки блока фактов')
def test_grants(web_browser):
    page = IkeaFoundationAboutPage(web_browser)
    page.btn_pip_up_сookies.click()
    element = web_browser.find_element(By.XPATH, '(//p[@class="vo-block-paragraph has-black-color has-text-color"])[1]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(2)
    with allure.step("проверка количества элементов"):
        check.equal(page.txt_3_fact.count(), 3)
    elements_fact_blocks = [
        (page.txt_facts,"Facts"),
        (page.txt_147_partners, "147 partners"),
        (page.txt_support_during_2022, "supported during 2022"),
        (page.txt_n_billion, "€1.8 billion"),
        (page.txt_granted_by_ikea, "granted by the IKEA Foundation since our founding"),
        (page.txt_1_billion, "€1 billion"),
        (page.txt_pledged_to_reduce, "pledged to reduce global emissions between 2021 and 2025"),
    ]
    for elements, elements_text in elements_fact_blocks:
        with allure.step("проверка на видимость"):
            check.is_true(elements.is_visible())
        with allure.step("проверка на совпадение текста"):
            check.equal(elements.get_text(), elements_text)



@allure.story('Проверка страницы о Ikea Foundation')
@allure.feature('Тест для проверки блока фактов')
def test_text_ingvar(web_browser):
    page = IkeaFoundationAboutPage(web_browser)
    page.btn_pip_up_сookies.click()
    element = web_browser.find_element(By.XPATH, '//div[@class="wp-block-media-text has-media-on-the-right is-stacked-on-mobile is-vertically-aligned-top"]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(3)
    with allure.step("проверка на видимость и элемент не пустой"):
        check.is_true(page.txt_ingvars_vision_about.is_visible())
        check.is_not_none(page.txt_ingvars_vision_about)
    with allure.step("проверка картинки на размеры и видимость"):
        check.is_true(page.txt_ingvars_photo.is_visible())
        check.equal(page.txt_ingvars_photo.get_attribute("width"), "390")
        check.equal(page.txt_ingvars_photo.get_attribute("height"), "390")
    elements_button = [
        (page.btn_learn_about_history,"Learn more about our history","https://ikeafoundation.org/our-history/"),
        (page.btn_ingvard_story,"here","https://about.ikea.com/en/about-us/history-of-ikea/from-child-entrepreneur-to-ikea-founder")
    ]
    for elements, elements_text, elements_url in elements_button:
        with allure.step("проверка на кликабельность"):
            check.is_true(elements.is_clickable())
        with allure.step("проверка на видимость"):
            check.is_true(elements.is_visible())
        with allure.step("проверка на совпадение текста"):
            check.equal(elements.get_text(), elements_text)
        with allure.step("проверка совпадения ссылок"):
            check.equal(elements.get_attribute("href"), elements_url)

@allure.story('Тест для проверки главной страницы')
@allure.feature('Проверка Our focus, Our grants, Our learnings')
def test_focus(web_browser):
    page = IkeaFoundationAboutPage(web_browser)
    page.btn_pip_up_сookies.click()
    element = web_browser.find_element(By.XPATH, '//div[@class="focus grid "]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(2)
    element_text = [
        (page.txt_our_focus_people, "People"),
        (page.txt_our_focus_people_text,"We’re committed to helping families living in poverty and people who have been forced to flee their homes to build sustainable livelihoods. We see great opportunities in regenerative agriculture, green enterprise and the productive use of renewable energy."),
        (page.txt_our_focus_planet, "Planet"),
        (page.txt_our_focus_planet_text,"We’re committed to bold climate action to drastically reduce greenhouse gas emissions and to helping vulnerable communities adapt to the impacts of climate change."),
        ]
    for elements, elements_text in element_text:
        with allure.step("проверка видимости"):
            check.is_true(elements.is_visible())
        with allure.step("проверка текста"):
            check.equal(elements.get_text(), elements_text)
    with allure.step("проверка двух кнопок на ссылки, кликабельность, текст, видимость"):
        check.is_true(page.btn_our_focus_more_button.is_visible())
        check.equal(page.btn_our_focus_more_button.get_text(), "Learn more about our work")
        check.equal(page.btn_our_focus_more_button.get_attribute("href"), "https://ikeafoundation.org/themes/")
        check.is_true(page.btn_our_focus_more_button.is_clickable())









    #element = web_browser.find_element(By.XPATH, '(//div[@class="slider__track"])[2]')
    #web_browser.execute_script("arguments[0].scrollIntoView(true);", element)