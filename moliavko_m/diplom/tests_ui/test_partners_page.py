import time
import allure
import pytest_check as check

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
        (page.png_partner_03_logo,"204","50")
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
    page.btn_pip_up_cookies.click()
    elements_links_1 = [
        (page.btn_partner_01_grants, "Show grants", "https://ikeafoundation.org/grants?partner=31404#grants-archive"),
        (page.btn_partner_01_articles, "Show articles", "https://ikeafoundation.org/stories/?post_partner=31404"),
        (page.btn_partner_01_site, "http://aglimmerofhope.org/", "http://aglimmerofhope.org/"),
    ]
    page.png_partner_01_logo.right_mouse_click()
    time.sleep(3)
    for elements, elements_text, elements_url in elements_links_1:
        with allure.step("проверка видимости, кликабельности, текста, ссылок"):
             check.is_true(elements.is_visible())
             check.equal(elements.get_text(), elements_text)
             check.equal(elements.get_attribute("href"), elements_url)
             check.is_true(elements.is_clickable())

    elements_links_2 = [
        (page.btn_partner_02_grants, "Show grants", "https://ikeafoundation.org/grants?partner=34464#grants-archive"),
        (page.btn_partner_02_articles, "Show articles", "https://ikeafoundation.org/stories/?post_partner=34464"),
        (page.btn_partner_02_site, "https://bomaproject.org/", "https://bomaproject.org/")
    ]
    x_coordinate = 0
    y_coordinate = 700
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(5)
    page.png_partner_02_logo.right_mouse_click()
    time.sleep(3)
    for elements, elements_text, elements_url in elements_links_2:
        with allure.step("проверка видимости, кликабельности, текста, ссылок"):
             check.is_true(elements.is_visible())
             check.equal(elements.get_text(), elements_text)
             check.equal(elements.get_attribute("href"), elements_url)
             check.is_true(elements.is_clickable())

    elements_links_3 = [
        (page.btn_partner_03_site, "https://www.unicef.org/", "https://www.unicef.org/"),
        (page.btn_partner_03_grants, "Show grants", "https://ikeafoundation.org/grants?partner=31370#grants-archive"),
        (page.btn_partner_03_articles, "Show articles", "https://ikeafoundation.org/stories/?post_partner=31370"),
        (page.btn_partner_03_relises, "Show press releases", "https://ikeafoundation.org/press?related_partner=31370")
    ]
    x_coordinate = 0
    y_coordinate = 7000
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(5)
    page.png_partner_03_logo.right_mouse_click()
    time.sleep(3)
    for elements, elements_text, elements_url in elements_links_3:
        with allure.step("проверка видимости, кликабельности, текста, ссылок"):
             check.is_true(elements.is_visible())
             check.equal(elements.get_text(), elements_text)
             check.equal(elements.get_attribute("href"), elements_url)
             check.is_true(elements.is_clickable())