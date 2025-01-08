import pytest
import requests
import pytest_check as check
import allure



@allure.title('Апи тест')
@allure.feature('проверка апи кнопки "twitter" ')
@allure.description("проверяем, что кнопка работает, отдает статус код 200")
@allure.link("https://twitter.com/IKEAFoundation", name="Website")
@pytest.mark.parametrize('url', ["https://twitter.com/IKEAFoundation"])
def test_api_twitter_button(url):
    response = requests.get(f'{url}')
    with allure.step(f'проверка кнопки {url} на статус код'):
        check.equal(response.status_code, 200)



@allure.title('Апи тест')
@allure.feature('проверка апи кнопки "linkedin" ')
@allure.description("проверяем, что кнопка работает, отдает статус код 200")
@allure.link("https://www.linkedin.com/authwall?trk=bf&trkInfo=AQF-fDaX9SivwQAAAZRGXp_QCCdQ4oBgg5DeTLmhuleKWy-yRx7SNuWZ2X4-Fo0LEwCifybV_9ArVZl7ApG9M_TiHPeJd0SmmmSQt28p6vGnbxgJq3R5mDUPQAwovuKpSXE40s0=&original_referer=&sessionRedirect=https%3A%2F%2Fnl.linkedin.com%2Fcompany%2Fikea-foundation", name="Website")
@pytest.mark.parametrize('url', ["https://www.linkedin.com/authwall?trk=bf&trkInfo=AQF-fDaX9SivwQAAAZRGXp_QCCdQ4oBgg5DeTLmhuleKWy-yRx7SNuWZ2X4-Fo0LEwCifybV_9ArVZl7ApG9M_TiHPeJd0SmmmSQt28p6vGnbxgJq3R5mDUPQAwovuKpSXE40s0=&original_referer=&sessionRedirect=https%3A%2F%2Fnl.linkedin.com%2Fcompany%2Fikea-foundation"])
def test_api_linkedin_button(url):
    response = requests.get(f'{url}')
    with allure.step(f'проверка кнопки {url} на статус код'):
        check.equal(response.status_code, 200)



@allure.title('Апи тест')
@allure.feature('проверка апи кнопки "youtube"')
@allure.description("проверяем, что кнопка работает, отдает статус код 200")
@allure.link("https://www.youtube.com/user/IKEAFoundation/", name="Website")
@pytest.mark.parametrize('url', ["https://www.youtube.com/user/IKEAFoundation/"])
def test_api_youtube_button(url):
    response = requests.get(f'{url}')
    with allure.step(f'проверка кнопки {url} на статус код'):
        check.equal(response.status_code, 200)



@allure.title('Апи тест')
@allure.feature('проверка апи кнопки "instagram"')
@allure.description("проверяем, что кнопка работает, отдает статус код 200")
@allure.link("https://www.instagram.com/ikea_foundation/", name="Website")
@pytest.mark.parametrize('url', ["https://www.instagram.com/ikea_foundation/"])
def test_api_instagram_button(url):
    response = requests.get(f'{url}')
    with allure.step(f'проверка кнопки {url} на статус код'):
        check.equal(response.status_code, 200)



