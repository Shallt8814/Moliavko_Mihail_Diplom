import time


import allure
import pytest_check as check
from selenium.webdriver.common.by import By

from moliavko_m.diplom.locators.locators_header_and_footer import HeaderFooter
from moliavko_m.diplom.locators.locators_main_page import MainPage
from conftest import web_browser



@allure.story('Тест для проверки хедара')
@allure.feature('Тест для проверки хедeра')
def test_headers(web_browser):
    page = HeaderFooter(web_browser)
    page.btn_pip_up_cookies.click()
    elements_headers = [
        (page.btn_button_in_header,None),
        (page.btn_logo_button_header, "https://ikeafoundation.org/"),
        (page.btn_button_searching,None),

    ]
    for elements, elements_url in elements_headers:
        with allure.step(f'Проверка на отображение'):
            check.is_true(elements.is_visible())
        with allure.step(f'Проверка на кликабельность'):
            check.is_true(elements.is_clickable())
        with allure.step(f'проверка "{elements_url}" на совпадение ссылок'):
            check.equal(elements.get_attribute("href"), elements_url)

    elements_headers = [
        (page.btn_menu_about_us_header_foundation,"The Foundation","https://ikeafoundation.org/about"),
        (page.btn_menu_about_us_header_themes,"Our themes","https://ikeafoundation.org/themes"),
        (page.btn_menu_about_us_header_way_we_work,"The way we work","https://ikeafoundation.org/about/the-way-we-work"),
        (page.btn_menu_about_us_header_team,"Our team","https://ikeafoundation.org/team"),
        (page.btn_menu_about_us_header_values,"Our values","https://ikeafoundation.org/about/values"),
        (page.btn_menu_about_us_header_funding,"Our funding and governance","https://ikeafoundation.org/our-funding-and-governance"),
        (page.btn_grand_making_header,"Grant making","https://ikeafoundation.org/grants/"),
        (page.btn_learnings_header,"Learnings","https://ikeafoundation.org/learnings"),
        (page.btn_partners_header,"Partners","https://ikeafoundation.org/partners"),
        (page.btn_press_header,"Press","https://ikeafoundation.org/press"),
        (page.btn_stories_header,"Stories","https://ikeafoundation.org/stories/"),
    ]
    page.btn_button_in_header.click()
    page.btn_about_us_header.click()
    for elements, elements_text, elements_url in elements_headers:
        with allure.step(f'Проверка на отображение'):
            check.is_true(elements.is_visible())
        with allure.step(f'Проверка на кликабельность'):
            check.is_true(elements.is_clickable())
        with allure.step(f'проверка "{elements_url}" на совпадение ссылок'):
            check.equal(elements.get_attribute("href"), elements_url)
        with allure.step('проверка на совпадение текста'):
            check.equal(elements.get_text(), elements_text)



@allure.story('Тест для проверки футера')
@allure.feature('Тест для проверки футера')
def test_headers_3(web_browser):
    page = HeaderFooter(web_browser)
    page.btn_pip_up_cookies.click()
    elements_headers = [
        (page.btn_FAQ_footer,"FAQ","https://ikeafoundation.org/faq/"),
        (page.btn_vacancies_footer,"Vacancies","https://ikeafoundation.org/vacancies/"),
        (page.btn_privacy_policy_footer,"Privacy Policy","https://ikeafoundation.org/privacy-policy/"),
        (page.btn_ANBI_footer,"ANBI","https://ikeafoundation.org/anbi-documents/"),
        (page.btn_documents_footer,"Documents","https://ikeafoundation.org/documents/"),
        (page.btn_footer_link,"Visit our values page to learn more", "https://ikeafoundation.org/values/"),
        (page.btn_twitter_footer,"","https://twitter.com/IKEAFoundation"),
        (page.btn_linkedin_footer,"","https://nl.linkedin.com/company/ikea-foundation"),
        (page.btn_youtube_footer,"","https://www.youtube.com/user/IKEAFoundation/"),
        (page.btn_instagram_footer,"","https://www.instagram.com/ikea_foundation/"),
    ]
    for elements, elements_text, elements_url in elements_headers:
        with allure.step('Проверка на отображение'):
            check.is_true(elements.is_visible())
        with allure.step('Проверка на кликабельность'):
            check.is_true(elements.is_clickable())
        with allure.step(f'проверка "{elements_url}" на совпадение ссылок'):
            check.equal(elements.get_attribute("href"), elements_url)
        with allure.step('проверка на совпадение текста'):
            check.equal(elements.get_text(), elements_text)



@allure.story('Тест для проверки футера')
@allure.feature('Тест для проверки поиска по сайту')
def test_headers_5(web_browser):
    page = HeaderFooter(web_browser)
    page.btn_pip_up_cookies.click()
    with allure.step("нажать на кнопку поиска"):
        page.btn_button_searching.click()
        with allure.step("ввести данные, нажать на поиск"):
            page.btn_search_input.send_keys('IKEA foundation week 2023')
            page.btn_confirm_search.click()
    with allure.step("проверка поиска"):
        check.is_true(page.txt_foundation_week_2023.is_visible())



@allure.story('Тест для проверки футера')
@allure.feature('проверка количества элементов')
def test_footer_blocks(web_browser):
    page = HeaderFooter(web_browser)
    page.btn_pip_up_cookies.click()
    with allure.step("проверка количества элемента"):
        check.equal(page.social_media_footer_blocks.count(), 4)

@allure.story('Тест для проверки главной страницы')
@allure.feature('Проверка основного презентабельного текста и текста грантов')
def test_main_presentable_text(web_browser):
    page = MainPage(web_browser)
    page.btn_pip_up_cookies.click()
    elements_main = [
        (page.txt_hero_text,"Our vision is to create a better everyday life for the many people."),
        (page.txt_hero_mission,"Our mission"),
        (page.txt_hero_mission_about,"To improve the lives of vulnerable children by enabling their families to create sustainable livelihoods, and fight and cope with climate change.")
    ]
    for elements, elements_text in elements_main:
        with allure.step("проверка видимости элементов"):
            check.is_true(elements.is_visible())
        with allure.step("проверка совпадения текста"):
            check.equal(elements.get_text(), elements_text)
###проверка текста грантов
    page.txt_ikea_grand.scroll_to_element()
    elements_main = [
        (page.txt_ikea_grand,"The IKEA Foundation has granted €2 billion for people and the planet so far."),
        (page.txt_ikea_grand_ikea_foundation,"IKEA Foundation"),
        (page.txt_ikea_grand_money,"€2 billion"),
        (page.txt_ikea_grand_people,"people"),
        (page.txt_ikea_grand_planet,"planet")
    ]
    for elements, elements_text in elements_main:
        with allure.step("проверка совпадения текста"):
            check.equal(elements.get_text(), elements_text)
        with allure.step("проверка совпадения текста"):
            check.is_true(elements.is_visible())



@allure.story('Тест для проверки главной страницы')
@allure.feature('Проверка Our focus, Our grants, Our learnings')
def test_main_activities_text(web_browser):
    page = MainPage(web_browser)
    page.btn_pip_up_cookies.click()
    element_text = [
        (page.txt_our_focus_people,"People"),
        (page.txt_our_focus_people_text,"We’re committed to helping families living in poverty and people who have been forced to flee their homes to build sustainable livelihoods. We see great opportunities in regenerative agriculture, green enterprise and the productive use of renewable energy."),
        (page.txt_our_focus_planet,"Planet"),
        (page.txt_our_focus_planet_text,"We are committed to taking bold climate action. Our mission is clear: drastically reduce greenhouse gas emissions to mitigate global temperature rise to 1.5°C and support vulnerable communities in adapting to the inevitable impacts of climate change. In the foreseeable future, our top priority is emission reduction, as we believe it is the most urgent step toward securing a sustainable future for all."),
    ]
    element = web_browser.find_element(By.XPATH,'//div[@class="focus grid "]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(2)
    for elements, elements_text in element_text:
        with allure.step("проверка видимости"):
            check.is_true(elements.is_visible())
        with allure.step("проверка текста"):
            check.equal(elements.get_text(), elements_text)
    elementos_txt = [
        (page.txt_our_grands_text,"Find out about the partners we fund and the amount, duration and scope of our grants."),
        (page.txt_our_learnings_text,"Learning how to do things better is at the heart of our culture. We believe there are always ways to improve, so we can increase our impact for people and the planet.")
    ]
    element = web_browser.find_element(By.XPATH,'//div[@class="wp-block-columns is-style-border-bottom is-layout-flex wp-container-core-columns-is-layout-1 wp-block-columns-is-layout-flex"]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(2)
    for elements, elements_text in elementos_txt:
        with allure.step("проверка на видимость"):
            check.is_true(elements.is_visible)
        with allure.step("проверка совпадения текста"):
            check.equal(elements.get_text(), elements_text)




@allure.story('Тест для проверки главной страницы')
@allure.feature('Проверка кнопок Our focus, Our grants, Our learnings')
def test_main_activities_buttons(web_browser):
    page = MainPage(web_browser)
    page.btn_pip_up_cookies.click()
    element_button = [
        (page.btn_our_focus_more_button,"","https://ikeafoundation.org/focus"),
        (page.btn_our_grands_more_buttons,"Learn more","https://ikeafoundation.org/grants/"),
        (page.btn_our_learnings_more_button,"Learn more","https://ikeafoundation.org/learnings/"),
    ]

    element = web_browser.find_element(By.XPATH, '//div[@class="entry__inner padded container has-parent-"]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(3)
    with allure.step("проверка на видимость"):
        check.is_true(page.btn_our_focus_more_button.is_visible())
    page.btn_our_focus_more_button.click()
    web_browser.back()
    time.sleep(3)
    with allure.step("проверка на видимость"):
        check.is_true(page.btn_our_grands_more_buttons.is_visible())
    page.btn_our_grands_more_buttons.click()
    web_browser.back()
    time.sleep(3)
    with allure.step("проверка на видимость"):
        check.is_true(page.btn_our_learnings_more_button.is_visible())
    page.btn_our_learnings_more_button.click()
    web_browser.back()
    time.sleep(3)
    for elements, elements_text, elements_url in element_button:
        with allure.step("проверка совпадения текста"):
            check.equal(elements.get_text(), elements_text)
        with allure.step("проверка совпадения ссылок"):
            check.equal(elements.get_attribute("href"), elements_url)



@allure.story('Тест для проверки главной страницы')
@allure.feature('Проверка наличия и отображения цитат основателя и кнопок ориентирования')
def test_main_citates(web_browser):
    page = MainPage(web_browser)
    page.btn_pip_up_cookies.click()
    element = web_browser.find_element(By.XPATH,'//div[@class="slider__track"]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(2)
    with allure.step("проверка слайда на отображения, текст, кликабельность"):
        check.is_true(page.txt_1_slide_citate_text.is_visible())
        check.is_true(page.txt_1_slide_autor.is_visible())
        check.equal(page.txt_1_slide_citate_text.get_text(), "No method is more effective than the good example.")
        check.equal(page.txt_1_slide_autor.get_text(), "Ingvar Kamprad")
    page.btn_slider_right_button.click()
    page.btn_slider_left_button.click()
    page.btn_slider_right_button.click()
    with allure.step("проверка слайда на отображения, текст, кликабельность"):
        check.is_true(page.txt_2_slide_citate_text.is_visible())
        check.is_true(page.txt_2_slide_autor.is_visible())
        check.equal(page.txt_2_slide_citate_text.get_text(), "Development is not always the same thing as progress.")
        check.equal(page.txt_2_slide_autor.get_text(), "Ingvar Kamprad")
    page.btn_slider_right_button.click()
    with allure.step("проверка слайда на отображения, текст, кликабельность"):
        check.is_true(page.txt_3_slide_citate_text.is_visible())
        check.is_true(page.txt_3_slide_autor.is_visible())
        check.equal(page.txt_3_slide_citate_text.get_text(), "By always asking why we are doing this or that, we can find new paths.")
        check.equal(page.txt_3_slide_autor.get_text(), "Ingvar Kamprad")
    page.btn_slider_right_button.click()
    with allure.step("проверка слайда на отображения, текст, кликабельность"):
        check.is_true(page.txt_4_slide_citate_text.is_visible())
        check.is_true(page.txt_4_slide_autor.is_visible())
        check.equal(page.txt_4_slide_citate_text.get_text(), "The fear of making mistakes is the root of bureaucracy and the enemy of development.")
        check.equal(page.txt_4_slide_autor.get_text(), "Ingvar Kamprad")
    page.btn_slider_right_button.click()
    with allure.step("проверка слайда на отображения, текст, кликабельность"):
        check.is_true(page.txt_5_slide_citate_text.is_visible())
        check.is_true(page.txt_5_slide_autor.is_visible())
        check.equal(page.txt_5_slide_citate_text.get_text(), "Time is your most important resource.")
        check.equal(page.txt_5_slide_autor.get_text(), "Ingvar Kamprad")
    page.btn_slider_right_button.click()
    with allure.step("проверка слайда на отображения, текст, кликабельность"):
        check.is_true(page.txt_6_slide_citate_text.is_visible())
        check.is_true(page.txt_6_slide_autor.is_visible())
        check.equal(page.txt_6_slide_citate_text.get_text(), "Winning does not mean that someone else has to lose. The finest victories are those without losers.")
        check.equal(page.txt_6_slide_autor.get_text(), "Ingvar Kamprad")







@allure.story('Тест для проверки главной страницы')
@allure.feature('Проверка блока партнеров')
def test_main_partners(web_browser):
    page = MainPage(web_browser)
    page.btn_pip_up_cookies.click()
    element = web_browser.find_element(By.XPATH,'//div[@class="partner-grid"]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(4)
    with allure.step("проверка количества элементов"):
        check.equal(page.txt_partners_cards.count(), 12)
    elements_partners = [
        (page.txt_partners_block_about_text,"Partners"),
        (page.txt_partners_block_about_text_text,"We build long-term, strategic partnerships with both large and small organisations. Together with our partners, we develop innovative solutions and work to change complex systems, so they benefit the many people and protect our planet.")
    ]
    for elements, elements_text in elements_partners:
        with allure.step("проверка видимости"):
            check.is_true(elements.is_visible())
        with allure.step("проверка текста"):
            check.equal(elements.get_text(), elements_text)
    elements_partners_buttons = [
        (page.btn_partners_block_more_about_partners_button,"See all partners","https://ikeafoundation.org/partners/"),
        (page.btn_learn_about_our_work_together_button,"Learn more about our work together","https://ikeafoundation.org/focus")
    ]
    for elements, elements_text, elements_url in elements_partners_buttons:
        with allure.step("проверка видимости"):
            check.is_true(elements.is_visible())
        with allure.step("проверка текста"):
            check.equal(elements.get_text(), elements_text)
        with allure.step("проверка ссылок"):
            check.equal(elements.get_attribute("href"), elements_url)
        with allure.step("проверка кликабельности"):
            check.is_true(elements.is_clickable())



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
        number = [(4), (9), (10), (3), (1), (4), (10), (3), (5), (5), (53)]

        for count_elements in count:
            count_elements.click()
            check.equal(page.count_box.count(), number)
            '''
