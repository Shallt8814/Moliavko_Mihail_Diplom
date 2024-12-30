import time
import allure
import pytest_check as check

from selenium.webdriver.common.action_chains import ActionChains
from moliavko_m.diplom.locators.locators_partners_page import Partners
from conftest import web_browser

@allure.story('Проверка страницы Partners')
@allure.feature('Тест для проверки титульного текста')
def test_text_partners(web_browser):
    page = Partners(web_browser)
    page.btn_pip_up_cookies.click()
    element_txt = [
        (page.txt_partners_text,"Partners"),
        (page.txt_partners_text_about,"We build long-term, strategic partnerships with both large and small organisations. Together with our partners, we develop innovative solutions and work to change complex systems, so they benefit the many people and protect our planet.")
    ]
    for elements, elements_text in element_txt:
        with allure.step(""):
             check.is_true(elements.is_visible())
             check.equal(elements.get_text(), elements_text)



@allure.story('Проверка страницы Partners')
@allure.feature('Тест для проверки карточек партнеров')
def test_cards_partners(web_browser):
    page = Partners(web_browser)
    page.btn_pip_up_cookies.click()
    elements_png = [
        (page.png_partner_01_logo,"204","44"),
        (page.png_partner_02_logo,"204","57"),
        (page.png_partner_03_logo,"204","57")
    ]
    x_coordinate = 0
    y_coordinate = 700
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(5)
    x_coordinate = 0
    y_coordinate = 7000
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(7)
    for elements, elements_width, elements_height in elements_png:
        with allure.step(""):
             check.is_true(elements.is_visible())
             check.equal(elements.get_attribute("width"), elements_width)
             check.equal(elements.get_attribute("height"), elements_height)
    with allure.step(""):
         check.equal(page.txt_partners_cards.count(), 181)



@allure.story('Проверка страницы Partners')
@allure.feature('Тест для проверки ссылок в карточках партнеров')
def test_cards_buttons_partners(web_browser):
    page = Partners(web_browser)
    action = ActionChains(web_browser)
    page.btn_pip_up_cookies.click()
    elements_links = [
        (page.btn_partner_01_grants, "", ""),
        (page.btn_partner_01_articles, "", ""),
        (page.btn_partner_01_site, "", ""),
        (page.btn_partner_02_grants, "", ""),
        (page.btn_partner_02_articles, "", ""),
        (page.btn_partner_02_site, "", ""),
        (page.btn_partner_03_site, "", ""),
        (page.btn_partner_03_grants, "", ""),
        (page.btn_partner_03_articles, "", ""),
        (page.btn_partner_03_relises, "", ""),
    ]
    page.png_partner_01_logo.right_mouse_click()
    time.sleep(3)
    x_coordinate = 0
    y_coordinate = 700
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(5)
    page.png_partner_02_logo.right_mouse_click()
    time.sleep(3)
    x_coordinate = 0
    y_coordinate = 7000
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(5)
    page.png_partner_03_logo.right_mouse_click()
    time.sleep(3)


















