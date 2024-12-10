import allure
import pytest_check as check

from moliavko_m.diplom.locators.locators_main_page import MainPage
from conftest import web_browser



@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедара')
def test_headers(web_browser):

    page = MainPage(web_browser)

    page.btn_cookies.click()

    elements = [
        (page.btn_headers_services,'Услуги','https://goldenmotors.by/#'),
        (page.btn_headers_news,'Новости','https://goldenmotors.by/news/'),
        (page.btn_headers_automobile,'Автомобили','https://goldenmotors.by/avtomobili/'),
        (page.btn_headers_autowashing,'Автомойка','https://goldenmotors.by/avtomojka/'),
        (page.btn_headers_contacts,'Контакты','https://goldenmotors.by/contacts/'),
        (page.btn_headers_first_number,'+375 (29) 374-66-66',None),
        (page.btn_headers_second_number,'+375 (33) 374-66-66',None),
        (page.btn_headers_third_number,'+375 (44) 783-28-32',None),
        (page.btn_headers_for_clients,'Клиентам','https://goldenmotors.by/blog/'),
        (page.btn_headers_mototech,'Мототехника','https://goldenmotors.by/mototekhnika/'),
        (page.txt_headers_timetxt,'Время работы.',None),
        (page.txt_headers_town,'г. Минск',None),
        (page.txt_headers_full_addres,'ул. Тимирязева, 46/1, 1 этаж',None),
    ]

    for elements, text_element, url_elements in elements:

        #with allure.step("проверка адреса кнопки"):
            #check.equal(page.get_current_url(), url_elements)

        with allure.step('Проверка  на отображение'):
            check.is_true(elements.is_visible())

        with allure.step('Проверка на кликабельность'):
            check.is_true(elements.is_clickable())

        with allure.step('Сверка текста'):
            check.equal(elements.get_text(), text_element)

        with allure.step("проверка адреса кнопки"):
            check.equal(elements.get_attribute('href'), url_elements)

def test_footer(web_browser):

    page = MainPage(web_browser)

    page.btn_cookies.click()

    elements = [
        (page.footer_first_number,'+375 (33) 374-66-66', None),
        (page.footer_second_number,'+375 (29) 374-66-66', None),
        (page.footer_fasebook_icon, '', 'https://www.facebook.com/goldenmotorsby'),
        (page.footer_insta_icon, '', 'https://www.instagram.com/goldenmotors__by/'),
        (page.footer_telegram_icon, '', 'https://tele.click/goldenmotors_by'),
        (page.footer_privacy_policy, 'Политика конфиденциальности', None),
        (page.footer_catalog, 'КАТАЛОГ', None),
        (page.footer_automobile, 'Автомобили', None),
        (page.footer_mototech,'', ''),
        (page.footer_services),
        (page.footer_commission_sell),
        (page.footer_urgent_car_purchase),
        (page.footer_trade_in),
        (page.footer_car_on_credit),
        (page.footer_car_for_leasing),
        (page.footer_car_selection),
        (page.footer_car_made_to_order),
        (page.footer_urgent_car_sale),
        (page.footer_car_wash),
        (page.footer_about_us),
        (page.footer_news),
        (page.footer_blog),
        (page.footer_addres),
        (page.footer_wath_on_map),
        (page.footer_work_time),

    ]

    for elements, text_element, url_element in elements:

        #with allure.step("проверка адреса кнопки"):
            #check.equal(page.get_current_url(), url_elements)

        with allure.step('Проверка  на отображение'):
            check.is_true(elements.is_visible())

        with allure.step('Проверка на кликабельность'):
            check.is_true(elements.is_clickable())

        with allure.step('Сверка текста'):
            check.equal(elements.get_text(), text_element)

        with allure.step("проверка адреса кнопки"):
            check.equal(elements.get_attribute('href'), url_element)



'''@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки наличия блоков')
def test_headers(web_browser):
    """Этот тест проверяет блоки главной страницы на его присутсвие"""

    page = MainPage(web_browser)

    page.btn_pip_up_сookie.click()

    elements_headers = [
        (page.block_main, 'Первый блок или главный')
    ]

    for elements, elements_text in elements_headers:
        with allure.step(f'Проверка "{elements_text}" на отображение'):
            check.is_true(elements.is_visible())


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки текста')
def test_headers(web_browser):
    """Этот тест проверяет текст на наличие и его корректность"""

    page = MainPage(web_browser)

    page.btn_pip_up_сookie.click()

    elements_headers = [
        (page.txt_main_h1, 'Все для онлайн-проектов и их защиты')
    ]

    for elements, elements_text in elements_headers:
        with allure.step(f'Проверка "{elements_text}" на отображение'):
            check.is_true(elements.is_visible())

        with allure.step(f'Сверка текста "{elements_text}"'):
            check.equal(elements.get_text(), elements_text)


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки работоспособности инпута')
def test_input_main(web_browser):
    """Этот тест проверяет работоспособность инпута"""

    page = MainPage(web_browser)

    page.btn_pip_up_сookie.click()

    with allure.step('Проверка на кликабельность'):
        check.is_true(page.input_main_wrapper.is_visible())

    with allure.step('Проверка на отображение'):
        check.is_true(page.input_main_wrapper.is_clickable())

    with allure.step('Проверка плейсхолдера'):
        check.equal(page.input_main_wrapper.get_attribute('placeholder'), 'Введите домены')

    with allure.step('Проверка на ввод текст и роверка результата'):
        text_by_zone = page.text_by_zone.get_text()
        text_tatimati = 'tatimati'

        page.input_main_wrapper.send_keys(text_tatimati)
        page.btn_search_domain.click(1)

        time.sleep(10)
        print(page.group_valid_domain.get_text())
        check.not_equal(page.group_valid_domain.get_text().find(f'{text_tatimati+text_by_zone}'), -1)


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки адреса ссылок')
def test_link_main(web_browser):
    """Этот тест проверяет адрес ссылок в кнопках """

    page = MainPage(web_browser)

    page.btn_pip_up_сookie.click()

    with allure.step('Проверка на кликабельность'):
        check.is_true(page.btn_domain_link.is_clickable())
        check.is_true(page.btn_domain_link.is_visible())
        check.equal(page.btn_domain_link.get_attribute('href'), 'https://hoster.by/service/domains/')


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки колличества плиток в блоке "Подберите свое решение"')
def test_count_box_main(web_browser):
    """Этот тест проверяет количество плиток в блоке "Подберите свое решение" """

    page = MainPage(web_browser)

    page.btn_pip_up_сookie.click()

    with allure.step('Проверка количетва плиток'):
        count = page.btn_count_box
        namber = [(4), (9), (10), (3), (1), (4), (10), (3), (5), (5), (53)]

        for count_elemnts in count:
            count_elemnts.click()
            check.equal(page.count_box.count(), namber)
            '''
