import time

import allure
import pytest_check as check
from selenium.webdriver.common.by import By

from moliavko_m.diplom.locators.locators_themes_page import ThemesPage
from conftest import web_browser

@allure.story('Проверка страницы Themes Page')
@allure.feature('Тест для проверки титульного текста')
def test_themes_text(web_browser):
    page = ThemesPage(web_browser)
    page.btn_pip_up_cookies.click()
    elements_themes = [
        (page.txt_themes_text, "Themes"),
        (page.txt_themes_text_about,"Families need both financial stability and a healthy environment if they and their children are to thrive. That is why our commitments to help families improve their wealth and protect the planet go hand in hand."),
        (page.txt_themes_people, "People"),
        (page.txt_themes_planet, "Planet"),
    ]
    for elements, elements_text in elements_themes:
        with allure.step("проверка видимости"):
            check.is_true(elements.is_visible())
        with allure.step("проверка текста"):
            check.equal(elements.get_text(), elements_text)
    elements_themes_not_none = [
        page.txt_people_text_about,
        page.txt_planet_text_about
    ]
    for elements in elements_themes_not_none:
        with allure.step("проверка элемент не пустой"):
            check.is_not_none(elements)
    with allure.step("проверка картинки на размеры и видимость"):
        check.is_true(page.png_themes_people.is_visible())
        check.equal(page.png_themes_people.get_attribute("width"),"496")
        check.equal(page.png_themes_people.get_attribute("height"),"257")
    with allure.step("проверка картинки на размеры и видимость"):
        check.is_true(page.png_themes_planet.is_visible())
        check.equal(page.png_themes_planet.get_attribute("width"),"457")
        check.equal(page.png_themes_planet.get_attribute("height"),"257")
    element = web_browser.find_element(By.XPATH, '//div[@class="wp-block-columns is-layout-flex wp-container-core-columns-is-layout-1 wp-block-columns-is-layout-flex"]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(2)
    with allure.step("проверка текста и отображения"):
        check.is_true(page.txt_thematics_areas.is_visible())
        check.equal(page.txt_thematics_areas.get_text(), "Thematic Areas")


@allure.story('Проверка страницы Themes Page')
@allure.feature('Тест для проверки текста в кнопках в Thematic Areas')
def test_themes_links(web_browser):
    page = ThemesPage(web_browser)
    page.btn_pip_up_cookies.click()
    element = web_browser.find_element(By.XPATH, '(//h2[@class="border-header"])[2]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(2)
    elements_of_links = [
        (page.txt_thematic_areas_people, "People",None),
        (page.txt_renewable_energy, "Renewable Energy",None),
        (page.txt_renewable_energy_about, "We are committed to powering communities with renewable energy.",None),
        (page.txt_employment, "Employment & Entrepreneurship",None),
        (page.txt_employment_about, "We are committed to championing green entrepreneurs who provide employment and meaningful livelihoods for people living in poverty.",None),
        (page.txt_agricultural, "Agricultural Livelihoods",None),
        (page.txt_agricultural_about, "We are committed to helping people build a better life from planet-positive agriculture in East Africa and India.",None),
        (page.txt_refugee, "Refugee Livelihoods",None),
        (page.txt_refugee_about, "We are committed to helping refugees achieve economic self-reliance and sustainable livelihoods.",None),
        (page.txt_planet, "Planet",None),
        (page.txt_governance, "Governance and Society",None),
        (page.txt_governance_about, "We are committed to helping citizens, the media and civil society achieve ambitious climate goals.",None),
        (page.txt_real_economy, "Real Economy",None),
        (page.txt_real_economy_about, "We are committed to accelerating the corporate transition needed to meet the 1.5°C global warming threshold.",None),
        (page.btn_renewable_energy,"","https://ikeafoundation.org/themes/renewable-energy/"),
        (page.btn_employment,"","https://ikeafoundation.org/themes/employment-entrepreneurship/"),
        (page.btn_agricultural,"","https://ikeafoundation.org/themes/agricultural-livelihoods/"),
        (page.btn_refugee,"","https://ikeafoundation.org/themes/refugee-livelihoods/"),
        (page.btn_governance,"","https://ikeafoundation.org/themes/governance-and-society/"),
        (page.btn_real_economy,"","https://ikeafoundation.org/themes/real-economy/"),
    ]
    for elements, elements_text, elements_url in elements_of_links:
        with allure.step("проверка видимости"):
            check.is_true(elements.is_visible())
        with allure.step("проверка текста"):
            check.equal(elements.get_text(), elements_text)
        with allure.step("проверка ссылок"):
            check.equal(elements.get_attribute("href"), elements_url)
        with allure.step("проверка кликабельности"):
            check.is_true(elements.is_clickable())
    element = web_browser.find_element(By.XPATH, '(//div[@class="vo-block-rows alignfull"])[3]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(2)
    elements_of_links_2 = [
        (page.txt_special_initiatives, "Special Initiatives and Emergency Response",None),
        (page.txt_read_more, "Read more",None),
        (page.txt_read_more_about, "We are committed to responding to emergencies and helping displaced people rebuild their lives.",None),
        (page.btn_read_more, "", "https://ikeafoundation.org/themes/special-initiatives-emergency-response/")
    ]
    for elements, elements_text, elements_url in elements_of_links_2:
        with allure.step("проверка видимости"):
            check.is_true(elements.is_visible())
        with allure.step("проверка текста"):
            check.equal(elements.get_text(), elements_text)
        with allure.step("проверка ссылок"):
            check.equal(elements.get_attribute("href"), elements_url)
        with allure.step("проверка кликабельности"):
            check.is_true(elements.is_clickable())
    with allure.step("проверка количества кнопок, ссылок"):
        check.equal(page.txt_many_links.count(), 7)