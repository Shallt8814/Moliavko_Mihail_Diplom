import time

import allure
import pytest_check as check

from moliavko_m.diplom.locators.locators_automobile_page import AutomobilePage
from conftest import web_browser



@allure.story('Тест для проверки страницы с автомобилями')
@allure.feature('Тест для проверки подбора автомобиля')
def test_searching(web_browser):

    page = AutomobilePage(web_browser)
    page.btn_cookies.click()

    with allure.step("click buttons"):
        page.execute_script("""document.querySelector('[data-label="BMW"]').click""")
        page.search_model_auto.click()
        page.execute_script("""document.querySelector('[data-label="X5"]').click""")
        page.search_type_korobka.click()
        page.execute_script("""document.querySelector('[data-label="автоматическая"]').click""")
        page.search_type_motor.click()
        page.execute_script("""document.querySelector('[data-label="бензиновый"]').click""")
        page.search_type_privod.click()
        page.execute_script("""document.querySelector('[data-label="полный"]').click""")
        page.search_type_kuzova.click()
        page.execute_script("""document.querySelector('[data-label="внедорожник"]').click""")

    time.sleep(2)

    with allure.step("проверка найден ли автомобиль"):
        check.is_true(page.block_with_car.is_visible())

