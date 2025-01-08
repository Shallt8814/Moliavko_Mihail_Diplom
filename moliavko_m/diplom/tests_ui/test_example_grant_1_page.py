import time
import allure
import pytest_check as check

from moliavko_m.diplom.locators.locators_example_grant_1_page import ExampleGrant1
from conftest import web_browser



@allure.story("Тест для проверки страницы Example Grant 1")
@allure.feature('Тест для проверки хлебных крошек')
def test_breadcrumbs_example_grant_1(web_browser):
    page = ExampleGrant1(web_browser)
    page.btn_pip_up_cookies.click()
    elements_bar = [
        (page.btn_home,"Home","https://ikeafoundation.org/"),
        (page.btn_grants,"Grants","https://ikeafoundation.org/grants/"),
        (page.txt_current_grant_card,"Non-state climate action integrity: research and stakeholder engagement",None)
    ]
    for elements, elements_text, elements_url in elements_bar:
        with allure.step("проверка видимости, кликабельности, текста, ссылок"):
            check.is_true(elements.is_visible())
            check.equal(elements.get_text(), elements_text)
            check.equal(elements.get_attribute("href"), elements_url)
            check.is_true(elements.is_clickable())



@allure.story("Тест для проверки страницы Example Grant 1")
@allure.feature('Тест для проверки основного текста')
def test_main_text_example_grant_1(web_browser):
    page = ExampleGrant1(web_browser)
    page.btn_pip_up_cookies.click()
    elements_txt = [
        (page.txt_none_state_climate,"Non-state climate action integrity: research and stakeholder engagement"),
        (page.txt_none_state_climate_about,"This three-year project aims to provide an overview of the status, progress, aggregated impact and improvement potential of climate action by non-state actors (businesses, financial institutions, subnational governments). It provides an essential contribution to the overall assessment of climate governance systems essential for guarding overall accountability of subnational and business action.")
    ]
    for elements, elements_text in elements_txt:
        with allure.step("проверка видимости, текста"):
            check.is_true(elements.is_visible())
            check.equal(elements.get_text(), elements_text)



@allure.story("Тест для проверки страницы Example Grant 1")
@allure.feature('Тест для проверки окна прогресс бара')
def test_progress_bar_example_grant_1(web_browser):
    page = ExampleGrant1(web_browser)
    page.btn_pip_up_cookies.click()
    elements_txt = [
        (page.txt_grant_amount,"Grant amount"),
        (page.txt_date_grant_txt, "Date granted"),
        (page.txt_date_grant, "June 2024"),
        (page.txt_total_money, "€ 3.50M"),
        (page.txt_current_money, "€ 1.20M"),
    ]
    for elements, elements_text in elements_txt:
        with allure.step("проверка видимости, текста"):
            check.is_true(elements.is_visible())
            check.equal(elements.get_text(), elements_text)
    with allure.step("проверка видимости и атрибута ширины линии прогресса"):
        check.is_true(page.progress_bar.is_visible())
        check.equal(page.progress_bar.get_attribute("style"), "width: 34.2857%;")



@allure.story("Тест для проверки страницы Example Grant 1")
@allure.feature('Тест для проверки окна партнеров')
def test_partners_example_grant_1(web_browser):
    page = ExampleGrant1(web_browser)
    page.btn_pip_up_cookies.click()
    x_coordinate = 0
    y_coordinate = 700
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(3)
    with allure.step("проверка видимости"):
         check.is_true(page.txt_partner_card.is_visible())
    elements_btn = [
        (page.btn_all_partners_grants,"Show our grants","https://ikeafoundation.org/grants?partner=31570#grants-archive"),
        (page.btn_partner_link,"https://newclimate.org/","https://newclimate.org/")
    ]
    for elements, elements_text, elements_url in elements_btn:
        with allure.step("проверка кликабельности, видимости, текста, ссылок"):
             check.is_true(elements.is_visible())
             check.is_true(elements.is_clickable())
             check.equal(elements.get_text(), elements_text)
             check.equal(elements.get_attribute("href"), elements_url)



@allure.story("Тест для проверки страницы Example Grant 1")
@allure.feature('Тест для проверки возможности поделиться грантов в соц сетях')
def test_share_example_grant_1(web_browser):
    page = ExampleGrant1(web_browser)
    page.btn_pip_up_cookies.click()
    x_coordinate = 0
    y_coordinate = 700
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    with allure.step(""):
        check.is_true(page.txt_share_grant.is_visible())
        check.equal(page.txt_share_grant.get_text(), "Share grant")
    elements_btn = [
        (page.btn_share_on_twitter,"https://twitter.com/intent/tweet?text=https%3A%2F%2Fikeafoundation.org%2Fgrants%2Fnon-state-climate-action-integrity-research-and-stakeholder-engagement"),
        (page.btn_share_on_facebook,"https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fikeafoundation.org%2Fgrants%2Fnon-state-climate-action-integrity-research-and-stakeholder-engagement"),
        (page.btn_share_on_linkedin,"https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fikeafoundation.org%2Fgrants%2Fnon-state-climate-action-integrity-research-and-stakeholder-engagement&title=&summary=&source=")
    ]
    for elements, elements_url in elements_btn:
        with allure.step(""):
            check.is_true(elements.is_visible())
            check.is_true(elements.is_clickable())
            check.equal(elements.get_attribute("href"), elements_url)



@allure.story("Тест для проверки страницы Example Grant 1")
@allure.feature('Тест для проверки карточки человека-партнера')
def test_human_partner_example_grant_1(web_browser):
    page = ExampleGrant1(web_browser)
    page.btn_pip_up_cookies.click()
    x_coordinate = 0
    y_coordinate = 1000
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    elements_txt = [
        (page.txt_related_articles, "Related articles"),
        (page.txt_card_with_men_text,'Niklas Höhne, NewClimate Institute: “A future without fossil fuels is a much brighter future”')
    ]
    for elements, elements_text in elements_txt:
        with allure.step(""):
            check.is_true(elements.is_visible())
            check.equal(elements.get_text(), elements_text)
    with allure.step(""):
         check.is_true(page.btn_human_card_link.is_clickable())
         check.equal(page.btn_human_card_link.get_attribute("href"),"https://ikeafoundation.org/stories/niklas-hohne-newclimate-institute/")



