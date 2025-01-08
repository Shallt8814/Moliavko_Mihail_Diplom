import pytest
import requests
import pytest_check as check
import allure



@allure.title('Апи тест')
@allure.feature('проверка апи кнопки "Learn more about our work"')
@allure.description("проверяем, что кнопка работает, отдает статус код 200")
@allure.link("https://ikeafoundation.org/themes/", name="Website")
@pytest.mark.parametrize('url', ["https://ikeafoundation.org/themes/"])
def test_api1_button(url):
    response = requests.get(f'{url}')
    with allure.step(f'проверка кнопки {url} на статус код'):
         check.equal(response.status_code, 200)



@allure.title('Апи тест')
@allure.feature('проверка апи кнопки "post_card"')
@allure.description("проверяем, что кнопка работает, отдает статус код 200")
@allure.link("https://ikeafoundation.org/stories/post-cop29-reflections-a-call-to-action-for-funders/", name="Website")
@pytest.mark.parametrize('url', ["https://ikeafoundation.org/stories/post-cop29-reflections-a-call-to-action-for-funders/"])
def test_api_2_button(url):
    response = requests.get(f'{url}')
    with allure.step(f'проверка кнопки {url} на статус код'):
         check.equal(response.status_code, 200)



@allure.title('Апи тест')
@allure.feature('проверка апи кнопки "learn more (grants)"')
@allure.description("проверяем, что кнопка работает, отдает статус код 200")
@allure.link("https://ikeafoundation.org/grants/", name="Website")
@pytest.mark.parametrize('url', ["https://ikeafoundation.org/grants/"])
def test_api_3_button(url):
    response = requests.get(f'{url}')
    with allure.step(f'проверка кнопки {url} на статус код'):
         check.equal(response.status_code, 200)



@allure.title('Апи тест')
@allure.feature('проверка апи кнопки "learn more (learnings)"')
@allure.description("проверяем, что кнопка работает, отдает статус код 200")
@allure.link("https://ikeafoundation.org/learnings/", name="Website")
@pytest.mark.parametrize('url', ["https://ikeafoundation.org/learnings/"])
def test_api_4_button(url):
    response = requests.get(f'{url}')
    with allure.step(f'проверка кнопки {url} на статус код'):
         check.equal(response.status_code, 200)



@allure.title('Апи тест')
@allure.feature('проверка апи кнопки "see all partners"')
@allure.description("проверяем, что кнопка работает, отдает статус код 200")
@allure.link("https://ikeafoundation.org/partners/", name="Website")
@pytest.mark.parametrize('url', ["https://ikeafoundation.org/partners/"])
def test_api_5_button(url):
    response = requests.get(f'{url}')
    with allure.step(f'проверка кнопки {url} на статус код'):
         check.equal(response.status_code, 200)



@allure.title('Апи тест')
@allure.feature('проверка апи кнопки "learn more about our work"')
@allure.description("проверяем, что кнопка работает, отдает статус код 200")
@allure.link("https://ikeafoundation.org/themes/", name="Website")
@pytest.mark.parametrize('url', ["https://ikeafoundation.org/themes/"])
def test_api_6_button(url):
    response = requests.get(f'{url}')
    with allure.step(f'проверка кнопки {url} на статус код'):
         check.equal(response.status_code, 200)


