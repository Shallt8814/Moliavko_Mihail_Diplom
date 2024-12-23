import time


import allure
import pytest_check as check


from moliavko_m.diplom.locators.locators_our_funding_and_governance_page import OurFundingAndGovernance
from conftest import web_browser



@allure.story('Тест для проверки Our Funding And Governance')
@allure.feature('Тест для проверки Our Funding And Governance')
def test_text_elements_our_funding_and_governance(web_browser):
    page = OurFundingAndGovernance(web_browser)
    page.btn_pip_up_cookies.click()
    time.sleep(3)
    x_coordinate = 0
    y_coordinate = 1000
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(3)
    elements_txt = [
        page.txt_funding,
        page.txt_the_ikea_foundation,
        page.txt_ingka_foundation,
        page.txt_imas_foundation,
        page.txt_ikea_foundation,
        page.txt_governance,
        page.txt_the_ikea_foundation_board,
    ]
    for elements in elements_txt:
        with allure.step("проверка видимости "):
            check.is_true(elements.is_visible())
        with allure.step("проверка элементы не пустые"):
            check.is_not_none(elements)
    elements_name = [
        (page.txt_anders_moberg, "Anders Moberg"),
        (page.txt_jonas_kamprad, "Jonas Kamprad"),
        (page.txt_krister_mattson, "Krister Mattsson"),
        (page.txt_peter_kamprad, "Peter Kamprad"),
        (page.txt_chairperson, "Johan Kuylenstierna (chairperson)"),
    ]
    x_coordinate = 0
    y_coordinate = 1700
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(3)
    for elements, elements_text in elements_name:
        with allure.step("проверка видимости"):
            check.is_true(elements.is_visible())
        with allure.step("проверка совпадения текста"):
            check.equal(elements.get_text(), elements_text)



@allure.story('Тест для проверки Our Funding And Governance')
@allure.feature('Тест для проверки Our Funding And Governance')
def test_png_elements_our_funding_and_governance(web_browser):
    page = OurFundingAndGovernance(web_browser)
    page.btn_pip_up_cookies.click()
    x_coordinate = 0
    y_coordinate = 1700
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(3)
    elements_png = [
        (page.png_anders_moberg, "304", "406"),
        (page.png_johan_kuylenstierna, "304", "406"),
        (page.png_jonas_kamprad, "304", "405"),
        (page.png_krister_mattson, "304", "406"),
        (page.png_peter_kamprad, "304", "406")
    ]
    for elements, elements_width, elements_height in elements_png:
        with allure.step("проверка видимости"):
             check.is_true(elements.is_visible())
        with allure.step("проверка размера картинок"):
             check.equal(elements.get_attribute("width"), elements_width)
             check.equal(elements.get_attribute("height"), elements_height)