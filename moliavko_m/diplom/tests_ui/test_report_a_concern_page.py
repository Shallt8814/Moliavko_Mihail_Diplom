import time
import allure
import pytest_check as check

from moliavko_m.diplom.locators.locators_report_a_concern_page import ReportAConcern
from conftest import web_browser

@allure.story('Проверка страницы Report A Concern')
@allure.feature('Тест для проверки титульного текста')
def test_text_concern(web_browser):
    page = ReportAConcern(web_browser)
    page.btn_pip_up_cookies.click()
    elements_txt = [
        (page.txt_main_text,"Report a concern"),
        (page.txt_main_text_about, "This is the IKEA Foundation Trust Line, a platform to report concerns about the work of the IKEA Foundation or our partners.\n\nYou can, for example, use this if you have concerns related to an organisation that we provide funding to.\n\nPlease click on the scenario below that applies to you."),
        (page.txt_ikea_foundation, "IKEA Foundation"),
        (page.txt_ikea, "IKEA")
    ]
    for elements, elements_text in elements_txt:
        with allure.step(""):
             check.is_true(elements.is_visible())
             check.equal(elements.get_text(), elements_text)



@allure.story('Проверка страницы Report A Concern')
@allure.feature('Тест для проверки титульного текста')
def test_btn_concern(web_browser):
    page = ReportAConcern(web_browser)
    page.btn_pip_up_cookies.click()
    elements_btn = [
        (page.btn_1, "I would like to raise a concern about a partner organisation of the IKEA Foundation","https://ikea-foundation.gan-compliance.com/p/Case"),
        (page.btn_2, "I would like to raise a concern about an IKEA Foundation member of staff", "https://ikea-foundation.gan-compliance.com/p/Case"),
        (page.btn_3, "I’m an IKEA Foundation co-worker and would like to raise a concern", "https://ikeafoundation.org/report-a-concern-ikea-foundation-coworker/"),
        (page.btn_4, "I’m an IKEA co-worker and would like to raise a concern", "https://ikeafoundation.org/report-a-concern-ikea-coworker/"),
        (page.btn_5, "I’m an IKEA customer and would like to raise a concern", "https://ikeafoundation.org/report-a-concern-ikea-customer/"),
        (page.btn_6, "I would like to raise a concern about the IKEA supply chain", "https://ikeafoundation.org/report-a-concern-ikea-supply-chain/"),
    ]
    for elements, elements_text, elements_url in elements_btn:
        with allure.step("проверка видимости, кликабельности, текста, ссылок"):
             check.is_true(elements.is_visible())
             check.is_true(elements.is_clickable())
             check.equal(elements.get_text(), elements_text)
             check.equal(elements.get_attribute("href"), elements_url)
    with allure.step("проверка количества"):
         check.equal(page.many_btn.count(), 6)
