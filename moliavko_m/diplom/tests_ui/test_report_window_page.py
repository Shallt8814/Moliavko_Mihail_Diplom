import time
import allure
import pytest_check as check

from moliavko_m.diplom.locators.locators_report_window_page import ReportWindow
from conftest import web_browser

@allure.story('Проверка страницы Report Window')
@allure.feature('Тест для проверки титульного текста')
def test_text_report_window(web_browser):
    page = ReportWindow(web_browser)
    elements_txt = [
        (page.txt_main_text, "Welcome to the Foundations’ Trust Line Platform"),
        (page.txt_main_text_about, " This platform provides a safe and confidential environment to report serious concerns about misconduct, unlawful activities and/ or unethical behaviour, relevant to the IKEA Foundation/ IMAS Foundation/ INGKA Foundation.\n\nWhen reporting a concern, please make sure to note down your Case ID and Password. "),
        (page.txt_contact_info, " Alternatively, reports can be made over the phone through a hotline.\n\nPlease contact:\nNetherlands 📞 (+31) 0800 0221142\nIndia 📞 000 800 050 3894 "),
        (page.txt_or, "OR"),
        (page.txt_call_us, "Call us"),
        (page.txt_powered_by, "Powered by GAN integrity Inc."),
    ]
    for elements, elements_text in elements_txt:
        with allure.step(""):
             check.is_true(elements.is_visible)
             check.equal(elements.get_text(), elements_text)



@allure.story('Проверка страницы Report Window')
@allure.feature('Тест для проверки logo')
def test_logo_report_window(web_browser):
    page = ReportWindow(web_browser)
    with allure.step(""):
         check.is_true(page.logo.is_visible())
         check.equal(page.logo.get_attribute("width"), "128")
         check.equal(page.logo.get_attribute("height"), "40")



@allure.story('Проверка страницы Report Window')
@allure.feature('Тест для проверки кнопок')
def test_btn_report_window(web_browser):
    page = ReportWindow(web_browser)
    elements_btn = [
        (page.btn_create_report,"REPORT A CONCERN", ""),
        (page.btn_view_case, "VIEW CASE", ""),
        (page.btn_powered_by, "Privacy Notice · Imprint", "https://ganintegrity.com/privacy-notice/"),
    ]
    for elements, elements_text, elements_url in elements_btn:
        with allure.step(""):
             check.is_true(elements.is_clickable())
             check.is_true(elements.is_visible())
             check.equal(elements.get_text(), elements_text)

### !!! ПОЗИТИВНОЕ И НЕГАТИВНОЕ ТЕСТИРОВАНИЕ ПОЛЕЙ ВВОДА - МАНУАЛЬНОЕ !!! ###






