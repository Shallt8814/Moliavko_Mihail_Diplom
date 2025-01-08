import pytest
import requests
import pytest_check as check
import allure



@allure.title('Апи тест')
@allure.feature('проверка апи кнопки "logo button"')
@allure.description("проверяем, что кнопка работает, отдает статус код 200")
@allure.link("https://ikeafoundation.org/", name="Website")
@pytest.mark.parametrize('url', ["https://ikeafoundation.org/"])
def test_api_7_button(url):
    response = requests.get(f'{url}')
    with allure.step(f'проверка кнопки {url} на статус код'):
         check.equal(response.status_code, 200)
































