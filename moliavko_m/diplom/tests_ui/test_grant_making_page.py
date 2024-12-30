import time
from selenium.webdriver.support.ui import Select

import allure
import pytest_check as check
from selenium.webdriver.common.by import By

from moliavko_m.diplom.locators.locators_grant_making_page import GrantMaking
from conftest import web_browser


@allure.story("Тест для проверки страницы Grant Making")
@allure.feature('Тест для проверки txt элементов')
def test_txt_elements_grant_making(web_browser):
    page = GrantMaking(web_browser)
    page.btn_pip_up_cookies.click()
    elements_txt = [
        (page.txt_grant_making, "Grant making"),
        (page.txt_this_dataset_includes, "We are committed to being open and transparent about our grants and grant making process. Transparency is closely connected to our values and helps us continue learning with our partners so we can increase our impact. This is essential to help families afford a better everyday life and fight and cope with climate change."),
        (page.txt_this_dataset, "This dataset includes all active grants made by the IKEA Foundation. In addition, all donations made since 2021 to special initiatives, including emergency response programmes, are included. Closed grants are not included."),
        (page.txt_facts, "Facts"),
        (page.txt_india_kenya, "India, Kenya, Uganda, Ethiopia and Indonesia"),
        (page.txt_top_5, "Top 5 countries represented in our grant portfolio"),
        (page.txt_15_programme, "15 programme evaluations"),
        (page.txt_currently_ongoing, "currently ongoing in collaboration with our partners"),
        (page.txt_dataset, "Dataset"),
        (page.txt_our_grants_are, "Our grants are supporting the many people in countries around the world"),
        (page.txt_learnings, "Learnings"),
        (page.txt_learning_how_to_do, "Learning how to do things better is at the heart of our culture. We believe there are always ways to improve, so we can increase our impact for people and the planet."),
        (page.txt_sort_by, "Sort by"),
        (page.txt_x_results_found, "221 results found, showing 4 results")
    ]
    time.sleep(3)
    x_coordinate = 0
    y_coordinate = 1000
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(3)
    x_coordinate = 0
    y_coordinate = 2000
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(3)
    x_coordinate = 0
    y_coordinate = 3250
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(5)
    for elements, elements_text in elements_txt:
        with allure.step("проверка видимости"):
            check.is_true(elements.is_visible())
        with allure.step("проверка совпадения текста"):
            check.equal(elements.get_text(), elements_text)
    with allure.step("проверка количества"):
        check.equal(page.txt_archive_cards.count(), 4)


@allure.story("Тест для проверки страницы Grant Making")
@allure.feature('Тест для проверки кнопок ориентирования по карточкам грантов')
def test_btn_elements_grant_making(web_browser):
    page = GrantMaking(web_browser)
    page.btn_pip_up_cookies.click()
    x_coordinate = 0
    y_coordinate = 2500
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(1)
    page.btn_page.click()
    time.sleep(5)
    x_coordinate = 0
    y_coordinate = 2500
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(3)
    with allure.step("проверка видимости, кликабельности, совпадения текста"):
         check.is_true(page.btn_page.is_visible())
         check.is_true(page.btn_page.is_clickable())
         check.is_true(page.txt_card_thematic_area_latest.get_text(), "Start Network")
    page.btn_next_page.click()
    time.sleep(5)
    x_coordinate = 0
    y_coordinate = 2500
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(3)
    with allure.step("проверка видимости, кликабельности, совпадения текста"):
         check.is_true(page.btn_next_page.is_visible())
         check.is_true(page.btn_next_page.is_clickable())
         check.is_true(page.txt_card_thematic_area_latest.get_text(), "Forcibly displaced people lens investing in the greater Horn of Africa")
    page.btn_previous_page.click()
    time.sleep(5)
    x_coordinate = 0
    y_coordinate = 2500
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(3)
    with allure.step("проверка видимости, кликабельности, совпадения текста"):
         check.is_true(page.btn_previous_page.is_visible())
         check.is_true(page.btn_previous_page.is_clickable())
         check.is_true(page.txt_card_thematic_area_latest.get_text(), "Start Network")


@allure.story("Тест для проверки страницы Grant Making")
@allure.feature('Тест для проверки даун дроп меню датасета')
def test_dataset_grant_making(web_browser):
    page = GrantMaking(web_browser)
    page.btn_pip_up_cookies.click()
    x_coordinate = 0
    y_coordinate = 1500
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(2)
    with allure.step("1 вариант"):
        exp = Select(web_browser.find_element(By.XPATH, '/html/body/main/article/form/div[2]/div[1]/fieldset[1]/select'))
        exp.select_by_visible_text("Agricultural Livelihoods")
        time.sleep(1)
        exp = Select(web_browser.find_element(By.XPATH, '/html/body/main/article/form/div[2]/div[1]/fieldset[2]/select'))
        exp.select_by_visible_text("2022")
        time.sleep(1)
        exp = Select(web_browser.find_element(By.XPATH, '/html/body/main/article/form/div[2]/div[1]/fieldset[3]/select'))
        exp.select_by_visible_text("A Glimmer of Hope Foundation")
        time.sleep(3)
        with allure.step("проверка видимости, совпадения титла первой карточки, выводимого результата поиска"):
            check.is_true(page.txt_card_thematic_area_latest.is_visible())
            check.equal(page.txt_card_thematic_area_latest.get_text(), "Developing a circular food system in Debub Sodo, Ethiopia")
            check.equal(page.txt_x_results_found.get_text(),"1 results found, showing 1 results")
    with allure.step("2 вариант"):
        exp = Select(web_browser.find_element(By.XPATH, '/html/body/main/article/form/div[2]/div[1]/fieldset[1]/select'))
        exp.select_by_visible_text("Agricultural Livelihoods")
        time.sleep(1)
        exp = Select(web_browser.find_element(By.XPATH, '/html/body/main/article/form/div[2]/div[1]/fieldset[2]/select'))
        exp.select_by_visible_text("2018")
        time.sleep(1)
        exp = Select(web_browser.find_element(By.XPATH, '/html/body/main/article/form/div[2]/div[1]/fieldset[3]/select'))
        exp.select_by_visible_text("A Glimmer of Hope Foundation")
        time.sleep(3)
        with allure.step("проверка видимости, совпадения титла первой карточки, выводимого результата поиска"):
            check.is_true(page.txt_no_posts.is_visible())
            check.equal(page.txt_no_posts.get_text(), "No posts have been found.")
            check.equal(page.txt_x_results_found.get_text(), "0 results found, showing 0 results")
    with allure.step("3 вариант"):
        exp = Select(web_browser.find_element(By.XPATH, '/html/body/main/article/form/div[2]/div[1]/fieldset[1]/select'))
        exp.select_by_visible_text("Renewable Energy")
        time.sleep(1)
        exp = Select(web_browser.find_element(By.XPATH, '/html/body/main/article/form/div[2]/div[1]/fieldset[2]/select'))
        exp.select_by_visible_text("2023")
        time.sleep(1)
        exp = Select(web_browser.find_element(By.XPATH, '/html/body/main/article/form/div[2]/div[1]/fieldset[3]/select'))
        exp.select_by_visible_text("Sustain Plus")
        time.sleep(3)
        with allure.step("проверка видимости, совпадения титла первой карточки, выводимого результата поиска"):
            check.is_true(page.txt_card_thematic_area_latest.is_visible())
            check.equal(page.txt_card_thematic_area_latest.get_text(), "Strengthening Capability of Sustain Plus")
            check.equal(page.txt_x_results_found.get_text(), "1 results found, showing 1 results")
    with allure.step("4 вариант"):
        exp = Select(web_browser.find_element(By.XPATH, '/html/body/main/article/form/div[1]/div[1]/div/fieldset/select'))
        exp.select_by_visible_text("Oldest")
        time.sleep(1)
        exp = Select(web_browser.find_element(By.XPATH, '/html/body/main/article/form/div[2]/div[1]/fieldset[1]/select'))
        exp.select_by_visible_text("Renewable Energy")
        time.sleep(1)
        exp = Select(web_browser.find_element(By.XPATH, '/html/body/main/article/form/div[2]/div[1]/fieldset[2]/select'))
        exp.select_by_visible_text("Year")
        time.sleep(1)
        exp = Select(web_browser.find_element(By.XPATH, '/html/body/main/article/form/div[2]/div[1]/fieldset[3]/select'))
        exp.select_by_visible_text("Sustain Plus")
        time.sleep(3)
        with allure.step("проверка видимости, совпадения титла первой карточки, выводимого результата поиска"):
            check.is_true(page.txt_card_thematic_area_latest.is_visible())
            check.equal(page.txt_card_thematic_area_latest.get_text(), "Sustain Plus Platform")
            check.equal(page.txt_x_results_found.get_text(), "2 results found, showing 2 results")
    with allure.step("5 вариант"):
        exp = Select(web_browser.find_element(By.XPATH, '/html/body/main/article/form/div[1]/div[1]/div/fieldset/select'))
        exp.select_by_visible_text("Title A-Z")
        time.sleep(1)
        exp = Select(web_browser.find_element(By.XPATH, '/html/body/main/article/form/div[2]/div[1]/fieldset[1]/select'))
        exp.select_by_visible_text("Thematic Area")
        time.sleep(1)
        exp = Select(web_browser.find_element(By.XPATH, '/html/body/main/article/form/div[2]/div[1]/fieldset[2]/select'))
        exp.select_by_visible_text("Year")
        time.sleep(1)
        exp = Select(web_browser.find_element(By.XPATH, '/html/body/main/article/form/div[2]/div[1]/fieldset[3]/select'))
        exp.select_by_visible_text("All partners")
        time.sleep(3)
        with allure.step("проверка видимости, совпадения титла первой карточки, выводимого результата поиска"):
            check.is_true(page.txt_card_thematic_area_latest.is_visible())
            check.equal(page.txt_card_thematic_area_latest.get_text(), "#LetThemWork")
            check.equal(page.txt_card_thematic_area_latest_2.get_text(), "1000 Landscapes for 1 Billion People")
            check.equal(page.txt_x_results_found.get_text(), "221 results found, showing 4 results")



@allure.story("Тест для проверки страницы Grant Making")
@allure.feature('Тест для проверки кнопки лёрн мор информайшын')
def test_dataset_grant_making(web_browser):
    page = GrantMaking(web_browser)
    page.btn_pip_up_cookies.click()
    elements_btn = [
        (page.btn_learn_more, "Learn more", "https://ikeafoundation.org/learnings/")
    ]
    page.btn_learn_more.scroll_to_element()
    time.sleep(1)
    for elements, elements_text, elements_url in elements_btn:
        with allure.step("проверка видимости, текста, сслыки"):
            check.is_true(elements.is_visible())
            check.equal(elements.get_text(), elements_text)
            check.equal(elements.get_attribute("href"), elements_url)



@allure.story("Тест для проверки страницы Grant Making")
@allure.feature('Тест для проверки кнопки лёрн мор информайшын')
def test_btl_lear_more_grant_making(web_browser):
    page = GrantMaking(web_browser)
    page.btn_pip_up_cookies.click()
    x_coordinate = 0
    y_coordinate = 1500
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(2)
    page.input_search_for_a_keyword.send_keys("Scaling standardized climate and sustainability disclosure")
    time.sleep(2)
    with allure.step("проверка видимости, совпадения текста результата по запросу"):
        check.equal(page.txt_card_thematic_area_latest.get_text(), "Scaling standardized climate and sustainability disclosure")
        check.is_true(page.txt_card_thematic_area_latest.is_visible())
        check.equal(page.txt_x_results_found.get_text(), "1 results found, showing 1 results")
    page.input_search_for_a_keyword.send_keys("hfjkggjthryturyir")
    time.sleep(2)
    with allure.step("проверка видимости результата по запросу"):
        check.is_true(page.txt_no_posts.is_visible())



@allure.story("Тест для проверки страницы Grant Making")
@allure.feature('Тест для проверки карточек грантов')
def test_btn_learn_more_grant_making(web_browser):
    page = GrantMaking(web_browser)
    page.btn_pip_up_cookies.click()
    x_coordinate = 0
    y_coordinate = 1500
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(2)
    elements_btn = [
        (page.btn_card_href,"","https://ikeafoundation.org/grants/non-state-climate-action-integrity-research-and-stakeholder-engagement/"),
        (page.btn_little_card_href,"Read more","https://ikeafoundation.org/grants/non-state-climate-action-integrity-research-and-stakeholder-engagement/")
    ]
    for elements, elements_text, elements_url in elements_btn:
        check.is_true(elements.is_visible())
        check.equal(elements.get_text(), elements_text)
        check.equal(elements.get_attribute("href"), elements_url)
        check.is_true(elements.is_clickable())