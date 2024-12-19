import time


import allure
import pytest_check as check

from moliavko_m.diplom.locators.locators_our_values_page import OurValues
from conftest import web_browser



@allure.story("Тест для проверки страницы Our Values")
@allure.feature('Тест для проверки txt элементов')
def test_txt_elements_our_values(web_browser):
    page = OurValues(web_browser)
    page.btn_pip_up_cookies.click()
    elements_txt = [
        (page.txt_values,"Values"),
        (page.txt_at_the_ikea_foundation, "At the IKEA Foundation our values are at the heart of everything we do."),
        (page.txt_our_values, "Our values"),
        (page.txt_togetherness, "Togetherness"),
        (page.txt_caring_for, "Caring for people and planet "),
        (page.txt_cost_bla_bla, "Cost-consciousness "),
        (page.txt_simplicity, "Simplicity "),
        (page.txt_renew, "Renew and improve"),
        (page.txt_different, "Different with a meaning"),
        (page.txt_give, "Give and take responsibility "),
        (page.txt_lead, "Lead by example"),
        (page.txt_our_framework, "Our Ethical Framework"),
        (page.txt_the_work_of_ikea, "The work of the IKEA Foundation is built on a solid foundation of honesty, openness, trust and fairness. Our ethics are set out in detail in the IKEA Foundation Ethical Framework. "),
        (page.txt_we_do_not, "We do not tolerate misconduct. We want all our stakeholders — including our partners and their employees — to feel encouraged and empowered to come forward and raise any concerns they may have relating to misconduct."),
        (page.txt_if_you_suspect, "If you suspect any misconduct in our own activities or activities we fund, we ask you to please come forward, in good faith, to raise your concern. We will treat the matter in the strictest confidence and protect the identities of the people involved."),
        (page.txt_what_is_misconduct, "What is misconduct?"),
        (page.txt_misconduct_is, "Misconduct is any unethical or unlawful behaviour, any criminal act, any violation of the IKEA Foundation Ethical Framework or a combination of these. For example, cases of corruption, bribery, harassment and fraud fall under this definition."),
        (page.txt_how_can_i_rise, "How can I raise a concern about misconduct?"),
        (page.txt_the_ikea_foundation, "The IKEA Foundation has set up a Trust Line to enable people to report any concerns about misconduct related to our work or the activities we fund. Our main priority is to identify and appropriately address any serious issue."),
        (page.txt_this_trust, "This Trust Line is powered by the SpeakUp® system, an integrated phone/web tool to report misconduct. Our Trust Line allows for 24/7 confidential reporting and meets all data protection regulations."),
        (page.txt_we_will, "We will not tolerate negative effects or repercussions when you raise a concern in good faith, and you will not be put at a disadvantage."),
        (page.txt_photo_text,"Commonland and the IKEA Foundation are working together to restore a 2,000-hectare degraded landscape in central India. ©Remijn/India/2019")
    ]
    for elements, elements_text in elements_txt:
        with allure.step("проверка видимости"):
            check.is_true(elements.is_visible())
        with allure.step("проверка текста"):
            check.equal(elements.get_text(), elements_text)



@allure.story("Тест для проверки страницы Our Values")
@allure.feature('Тест для проверки png элементов')
def test_png_elements_our_values(web_browser):
    page = OurValues(web_browser)
    page.btn_pip_up_cookies.click()
    elements_png = [
        (page.png_photo, "496", "331")
    ]
    for elements, elements_width, elements_height in elements_png:
        with allure.step("проверка видимости"):
            check.is_true(elements.is_visible())
        with allure.step("проверка размеров фото"):
            check.equal(elements.get_attribute("width"), elements_width)
            check.equal(elements.get_attribute("height"), elements_height)

@allure.story("Тест для проверки страницы Our Values")
@allure.feature('Тест для проверки links элементов')
def test_links_elements_our_values(web_browser):
    page = OurValues(web_browser)
    page.btn_pip_up_cookies.click()
    time.sleep(2)
    x_coordinate = 0
    y_coordinate = 1000
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(2)
    elements_links = [
        (page.btn_ikea_framework, "IKEA Foundation Ethical Framework", "https://ikeafoundation.org/wp-content/uploads/2022/12/IF_Ethical_Framework_July22_02-1.pdf"),
        (page.btn_report_a_concern, "Report a concern to the Trust Line", "https://ikeafoundation.org/report-a-concern/")
    ]
    for elements, elements_text, elements_url in elements_links:
        with allure.step("проверка видимости"):
            check.is_true(elements.is_visible())
        with allure.step("проверка текста"):
            check.equal(elements.get_text(), elements_text)
        with allure.step("проверка ссылок"):
            check.equal(elements.get_attribute("href"), elements_url)