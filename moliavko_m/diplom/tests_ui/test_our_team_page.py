import time


import allure
import pytest_check as check

from moliavko_m.diplom.locators.locators_our_team_page import OurTeam
from conftest import web_browser



@allure.story("Тест для проверки страницы Our Team")
@allure.feature('Тест для проверки txt элементов')
def test_txt_elements_our_team(web_browser):
    page = OurTeam(web_browser)
    page.btn_pip_up_cookies.click()
    time.sleep(3)
    x_coordinate = 0
    y_coordinate = 1000
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(3)
    x_coordinate = 0
    y_coordinate = 1700
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(3)
    x_coordinate = 0
    y_coordinate = 2200
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(3)
    elements_txt = [
        (page.txt_meet_our_team, "Meet our team"),
        (page.txt_meet_our_team_about, "We are a dynamic, creative and diverse team made up of individuals from more than 14 different countries and working with partners from all over the world. We believe that the diversity of our team, united by a single organisational culture and common set of values, enables us to successfully pursue our vision to create a better everyday life for the many people."),
        (page.txt_leadership,"Leadership"),
        (page.txt_Programmes,"Programmes"),
        (page.txt_Operations, "Operations"),
        (page.txt_jessika_anderen ,"Jessica Anderen"),
        (page.txt_Chief_Executive_Officer, "Chief Executive Officer"),
        (page.txt_Marilia_Bezerra, "Marilia Bezerra"),
        (page.txt_Chief_Programmes_Officer, "Chief Programmes Officer"),
        (page.txt_Stelios_Kyriakakis, "Stelios Kyriakakis"),
        (page.txt_Chief_Operating_Officer, "Chief Operating Officer"),
        (page.txt_Amanda_Coady, "Amanda Coady"),
        (page.txt_Chief_of_Staff, "Chief of Staff"),
        (page.txt_Christa_Berends, "Christa Berends"),
        (page.txt_Chief_People_Officer, "Chief People Officer"),
        (page.txt_Elizabeth_McKeon, "Elizabeth McKeon"),
        (page.txt_Programmes_Director_Planet, "Programmes Director – Planet"),
        (page.txt_Haileselassie_Medhin, "Haileselassie Medhin"),
        (page.txt_Programmes_Director_People, "Programmes Director – People"),
        (page.txt_Feike_Derksen, "Feike Derksen"),
        (page.txt_General_Counsel, "General Counsel"),
        (page.txt_Jordi_Johannisse, "Jordi Johannisse"),
        (page.txt_Head_of_Finance, "Head of Finance"),
        (page.txt_Ulrika_Carlsson, "Ulrika Carlsson"),
        (page.txt_Head_of_Grant_Operations, "Head of Grant Operations"),
    ]
    time.sleep(5)
    for elements, elements_text in elements_txt:
        with allure.step("проверка на видимость"):
            check.is_true(elements.is_visible())
        with allure.step("проверка на совпадения текста"):
            check.equal(elements.get_text(), elements_text)


@allure.story("Тест для проверки страницы Our Team")
@allure.feature('Тест для проверки пнг элементов')
def test_png_elements_our_team(web_browser):
    page = OurTeam(web_browser)
    page.btn_pip_up_cookies.click()
    time.sleep(3)
    x_coordinate = 0
    y_coordinate = 1000
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(3)
    x_coordinate = 0
    y_coordinate = 1700
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(3)
    x_coordinate = 0
    y_coordinate = 2200
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(3)
    elements_png = [
        (page.png_jessika_anderen, "265", "424"),
        (page.png_Marilia_Bezerra, "264", "423"),
        (page.png_Stelios_Kyriakakis, "265", "424"),
        (page.png_Amanda_Coady, "259", "415"),
        (page.png_Christa_Berends, "259", "415"),
        (page.png_Elizabeth_McKeon, "236", "378"),
        (page.png_Haileselassie_Medhin, "236", "378"),
        (page.png_Feike_Derksen, "235", "376"),
        (page.png_Jordi_Johannisse, "235", "376"),
        (page.png_Ulrika_Carlsson, "238", "381"),
    ]
    for elements, elements_width, elements_height in elements_png:
        with allure.step("проверка размеров фото"):
            check.equal(elements.get_attribute("height"), elements_height)
            check.equal(elements.get_attribute("width"), elements_width)
        with allure.step("проверка на видимость"):
            check.is_true(elements.is_visible())
        with allure.step("проверка количества"):
            check.equal(page.png_many_png.count(), 10)


    #element = web_browser.find_element(By.XPATH,'//div[@class="wp-block-columns has-2-columns is-layout-flex wp-container-core-columns-is-layout-2 wp-block-columns-is-layout-flex"]')
    #web_browser.execute_script("arguments[0].scrollIntoView(true);", element)