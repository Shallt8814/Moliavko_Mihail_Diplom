import pytest
import requests
import pytest_check as check
import allure



@allure.title('Апи тест')
@allure.feature('проверка апи кнопки "report_a_concern"')
@allure.description("проверяем, что кнопка работает, отдает статус код 200")
@allure.link("https://ikeafoundation.org/report-a-concern/", name="Website")
@pytest.mark.parametrize('url', ["https://ikeafoundation.org/report-a-concern/"])
def test_api_report_button(url):
    response = requests.get(f'{url}')
    with allure.step(f'проверка кнопки {url} на статус код'):
        check.equal(response.status_code, 200)



@allure.title('Апи тест')
@allure.feature('проверка апи кнопки "view_case"')
@allure.description("проверяем, что кнопка работает, отдает статус код 200")
@allure.link("https://ikea-foundation.gan-compliance.com/p/api/Case/access?locale=en-US", name="Website")
@pytest.mark.parametrize('url', ["https://ikea-foundation.gan-compliance.com/p/api/Case/access?locale=en-US"])
def test_api_report_case(url):
    headers = {}
    data = {
        "submissionId": "580501184",
        "password": "8656 7876 8147 0822"
    }
    response = requests.request('POST', url, data=data, headers=headers)
    with allure.step(f'проверка кнопки {url} на статус код'):
        check.equal(response.status_code, 200)



@allure.title('Апи тест')
@allure.feature('проверка апи кнопки "visit_out_values"')
@allure.description("проверяем, что кнопка работает, отдает статус код 200")
@allure.link("https://ikeafoundation.org/values/", name="Website")
@pytest.mark.parametrize('url', ["https://ikeafoundation.org/values/"])
def test_api_visit_values_button(url):
    response = requests.get(f'{url}')
    with allure.step(f'проверка кнопки {url} на статус код'):
        check.equal(response.status_code, 200)