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
    page.btn_pip_up_сookies.click()
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
    page.btn_pip_up_сookies.click()
    elements_headers = [
        (page.btn_FAQ_footer,"FAQ","https://ikeafoundation.org/faq/"),
        (page.btn_vacancies_footer,"Vacancies","https://ikeafoundation.org/vacancies/"),
        (page.btn_privacy_policy_footer,"Privacy Policy","https://ikeafoundation.org/privacy-policy/"),
        (page.btn_ANBI_footer,"ANBI","https://ikeafoundation.org/anbi-documents/"),
        (page.btn_documents_footer,"Documents","https://ikeafoundation.org/documents/"),
        #(page.btn_cookie_preference_footer,"",""),
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

    elements_headers = [
        page.txt_footer_columns,
        page.txt_footer_column_1,
        page.txt_footer_column_2,
        page.txt_footer_column_3,
        page.txt_ikea_foundation_footer,
        page.txt_logo_button_footer,
        page.txt_trust_line_footer,
        page.txt_trust_text_footer,
        page.txt_social_media_footer,
        page.txt_social_media_block_footer,
    ]
    for elements in elements_headers:
        with allure.step('Проверка на отображение'):
            check.is_true(elements.is_visible())



@allure.story('Тест для проверки футера')
@allure.feature('Тест для проверки поиска по сайту')
def test_headers_5(web_browser):
    page = HeaderFooter(web_browser)
    page.btn_pip_up_сookies.click()
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
    page.btn_pip_up_сookies.click()
    with allure.step("проверка количества элемента"):
        check.equal(page.social_media_footer_blocks.count(), 4)

@allure.story('Тест для проверки главной страницы')
@allure.feature('Проверка основного презентабельного текста и текста грантов')
def test_main_presentable_text(web_browser):
    page = MainPage(web_browser)
    page.btn_pip_up_сookies.click()
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
    page.btn_pip_up_сookies.click()
    element_text = [
        (page.txt_our_focus_people,"People"),
        (page.txt_our_focus_people_text,"We’re committed to helping families living in poverty and people who have been forced to flee their homes to build sustainable livelihoods. We see great opportunities in regenerative agriculture, green enterprise and the productive use of renewable energy."),
        (page.txt_our_focus_planet,"Planet"),
        (page.txt_our_focus_planet_text,"We are committed to taking bold climate action. Our mission is clear: drastically reduce greenhouse gas emissions to mitigate global temperature rise to 1.5°C and support vulnerable communities in adapting to the inevitable impacts of climate change. In the foreseeable future, our top priority is emission reduction, as we believe it is the most urgent step toward securing a sustainable future for all."),
    ]
    element = web_browser.find_element(By.XPATH,'//div[@class="entry__inner padded container has-parent-"]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(2)
    for elements, elements_text in element_text:
        with allure.step("проверка видимости"):
            check.is_true(elements.is_visible())
        with allure.step("проверка текста"):
            check.equal(elements.get_text(), elements_text)
    elementos_textos = [
        (page.txt_our_grands_text,"Find out about the partners we fund and the amount, duration and scope of our grants.")
    ]
    element = web_browser.find_element(By.XPATH,'//div[@id="tns2-iw"]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(2)
    for elements, elements_text in elementos_textos:
        with allure.step("проверка на видимость"):
            check.is_true(elements.is_visible)
        with allure.step("проверка совпадения текста"):
            check.equal(elements.get_text(), elements_text)
    elementas_textas = [
        (page.txt_our_learnings_text,"Learning how to do things better is at the heart of our culture. We believe there are always ways to improve, so we can increase our impact for people and the planet.")
    ]
    element = web_browser.find_element(By.XPATH,'//div[@class="wp-block-columns is-style-border-bottom is-layout-flex wp-container-core-columns-is-layout-1 wp-block-columns-is-layout-flex"]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(2)
    for elements, elements_text in elementas_textas:
        with allure.step("проверка на видимость"):
            check.is_true(elements.is_visible)
        with allure.step("проверка совпадения текста"):
            check.equal(elements.get_text(), elements_text)



@allure.story('Тест для проверки главной страницы')
@allure.feature('Проверка кнопок Our focus, Our grants, Our learnings')
def test_main_activities_buttons(web_browser):
    page = MainPage(web_browser)
    page.btn_pip_up_сookies.click()
    element_button = [
        (page.btn_our_focus_more_button,"","https://ikeafoundation.org/focus"),
        (page.btn_our_grands_more_buttons,"Learn more","https://ikeafoundation.org/grants/"),
        (page.btn_our_learnings_more_button,"Learn more","https://ikeafoundation.org/learnings/"),
    ]

    element = web_browser.find_element(By.XPATH, '//div[@class="entry__inner padded container has-parent-"]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(2)
    with allure.step("проверка на видимость"):
        check.is_true(page.btn_our_focus_more_button.is_visible())
    page.btn_our_focus_more_button.click()
    web_browser.back()
    element = web_browser.find_element(By.XPATH, '//div[@id="tns2-iw"]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    with allure.step("проверка на видимость"):
        check.is_true(page.btn_our_grands_more_buttons.is_visible())
    page.btn_our_grands_more_buttons.click()
    web_browser.back()
    element = web_browser.find_element(By.XPATH, '//div[@class="wp-block-columns is-style-border-bottom is-layout-flex wp-container-core-columns-is-layout-1 wp-block-columns-is-layout-flex"]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    with allure.step("проверка на видимость"):
        check.is_true(page.btn_our_learnings_more_button.is_visible())
    page.btn_our_learnings_more_button.click()
    web_browser.back()
    for elements, elements_text, elements_url in element_button:
        with allure.step("проверка совпадения текста"):
            check.equal(elements.get_text(), elements_text)
        with allure.step("проверка совпадения ссылок"):
            check.equal(elements.get_attribute("href"), elements_url)



@allure.story('Тест для проверки главной страницы')
@allure.feature('Проверка наличия и отображения цитат основателя и кнопок ориентирования')
def test_main_citates(web_browser):
    page = MainPage(web_browser)
    page.btn_pip_up_сookies.click()
    element = web_browser.find_element(By.XPATH,'(//div[@class="slider__track"])[2]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(2)
    with allure.step(""):
        check.is_true(page.txt_1_slide_citate_text.is_visible())
        check.is_true(page.txt_1_slide_autor.is_visible())
        check.equal(page.txt_1_slide_citate_text.get_text(), "No method is more effective than the good example.")
        check.equal(page.txt_1_slide_autor.get_text(), "Ingvar Kamprad")
    page.btn_citates_slider_right_button.click()
    page.btn_citates_slider_left_button.click()
    page.btn_citates_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.txt_2_slide_citate_text.is_visible())
        check.is_true(page.txt_2_slide_autor.is_visible())
        check.equal(page.txt_2_slide_citate_text.get_text(), "Development is not always the same thing as progress.")
        check.equal(page.txt_2_slide_autor.get_text(), "Ingvar Kamprad")
    page.btn_citates_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.txt_3_slide_citate_text.is_visible())
        check.is_true(page.txt_3_slide_autor.is_visible())
        check.equal(page.txt_3_slide_citate_text.get_text(), "By always asking why we are doing this or that, we can find new paths.")
        check.equal(page.txt_3_slide_autor.get_text(), "Ingvar Kamprad")
    page.btn_citates_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.txt_4_slide_citate_text.is_visible())
        check.is_true(page.txt_4_slide_autor.is_visible())
        check.equal(page.txt_4_slide_citate_text.get_text(), "The fear of making mistakes is the root of bureaucracy and the enemy of development.")
        check.equal(page.txt_4_slide_autor.get_text(), "Ingvar Kamprad")
    page.btn_citates_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.txt_5_slide_citate_text.is_visible())
        check.is_true(page.txt_5_slide_autor.is_visible())
        check.equal(page.txt_5_slide_citate_text.get_text(), "Time is your most important resource.")
        check.equal(page.txt_5_slide_autor.get_text(), "Ingvar Kamprad")
    page.btn_citates_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.txt_6_slide_citate_text.is_visible())
        check.is_true(page.txt_6_slide_autor.is_visible())
        check.equal(page.txt_6_slide_citate_text.get_text(), "Winning does not mean that someone else has to lose. The finest victories are those without losers.")
        check.equal(page.txt_6_slide_autor.get_text(), "Ingvar Kamprad")



@allure.story('Тест для проверки главной страницы')
@allure.feature('Проверка видимости последних новостей и кнопок ориентирования')
def test_main_news(web_browser):
    page = MainPage(web_browser)
    page.btn_pip_up_сookies.click()
    element = web_browser.find_element(By.XPATH,'(//h2[@class="border-header"])[2]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(2)
    with allure.step(""):
        check.is_true(page.btn_1_news_slide.is_visible())
        check.is_true(page.txt_1_news_slide_text.is_visible())
        check.equal(page.txt_1_news_slide_text.get_text(), "Post-COP29 reflections: A call to action for Funders")
        check.is_true(page.btn_1_news_slide.is_clickable())
    with allure.step(""):
        check.is_true(page.btn_2_news_slide.is_visible())
        check.is_true(page.txt_2_news_slide_text.is_visible())
        check.equal(page.txt_2_news_slide_text.get_text(), "Maja Lazić, World Bank-UNHCR Joint Data Center on Forced Displacement: “There’s a huge momentum around the data that’s being produced on people forced to flee”")
        check.is_true(page.btn_2_news_slide.is_clickable())
    with allure.step(""):
        check.is_true(page.btn_3_news_slide.is_visible())
        check.is_true(page.txt_3_news_slide_text.is_visible())
        check.equal(page.txt_3_news_slide_text.get_text(), 'Meena Kamath, The Chancery Lane Project: "I wanted to use the power of the law to fight climate change."')
        check.is_true(page.btn_3_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    page.btn_slider_left_button.click()
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_4_news_slide.is_visible())
        check.is_true(page.txt_4_news_slide_text.is_visible())
        check.equal(page.txt_4_news_slide_text.get_text(), 'IKEA Foundation supports MSF in Sudan crisis scale-up')
        check.is_true(page.btn_4_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_5_news_slide.is_visible())
        check.is_true(page.txt_5_news_slide_text.is_visible())
        check.equal(page.txt_5_news_slide_text.get_text(), 'Tom Rivett-Carnac, Global Optimism: "I refuse to accept that we’re going to lose these incredible ecosystems."')
        check.is_true(page.btn_5_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_6_news_slide.is_visible())
        check.is_true(page.txt_6_news_slide_text.is_visible())
        check.equal(page.txt_6_news_slide_text.get_text(), 'Is it still possible to change the future of our planet? Read more in our 2023 Annual Review')
        check.is_true(page.btn_6_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_7_news_slide.is_visible())
        check.is_true(page.txt_7_news_slide_text.is_visible())
        check.equal(page.txt_7_news_slide_text.get_text(), '"How storytelling can be used for effective change."')
        check.is_true(page.btn_7_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_8_news_slide.is_visible())
        check.is_true(page.txt_8_news_slide_text.is_visible())
        check.equal(page.txt_8_news_slide_text.get_text(), 'Urmila Sarkar, Generation Unlimited: "“I really believe that young people can make a difference in the world”')
        check.is_true(page.btn_8_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_9_news_slide.is_visible())
        check.is_true(page.txt_9_news_slide_text.is_visible())
        check.equal(page.txt_9_news_slide_text.get_text(),'Tzeporah Berman, Fossil Fuel Non-Proliferation Treaty Initiative: "Never underestimate the power that we have to make change"')
        check.is_true(page.btn_9_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_10_news_slide.is_visible())
        check.is_true(page.txt_10_news_slide_text.is_visible())
        check.equal(page.txt_10_news_slide_text.get_text(),'Katarina Kahlmann: "Entrepreneurs in the Global South can help address environmental problems and also increase their income”')
        check.is_true(page.btn_10_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_11_news_slide.is_visible())
        check.is_true(page.txt_11_news_slide_text.is_visible())
        check.equal(page.txt_11_news_slide_text.get_text(), 'Thami Schweichler, United Repair Center: "Change may be a phone call away."')
        check.is_true(page.btn_11_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_12_news_slide.is_visible())
        check.is_true(page.txt_12_news_slide_text.is_visible())
        check.equal(page.txt_12_news_slide_text.get_text(), 'Dr. Catherine Mwema, BOMA: "We just need to give hardworking communities hope through our support."')
        check.is_true(page.btn_12_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_13_news_slide.is_visible())
        check.is_true(page.txt_13_news_slide_text.is_visible())
        check.equal(page.txt_13_news_slide_text.get_text(), '"More funding is needed for the just transition to sustainable buildings."')
        check.is_true(page.btn_13_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_14_news_slide.is_visible())
        check.is_true(page.txt_14_news_slide_text.is_visible())
        check.equal(page.txt_14_news_slide_text.get_text(), 'How we are working on global transformations for people and planet')
        check.is_true(page.btn_14_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_15_news_slide.is_visible())
        check.is_true(page.txt_15_news_slide_text.is_visible())
        check.equal(page.txt_15_news_slide_text.get_text(), 'Call to action: "invite women to our table, hear their voices."')
        check.is_true(page.btn_15_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_16_news_slide.is_visible())
        check.is_true(page.txt_16_news_slide_text.is_visible())
        check.equal(page.txt_16_news_slide_text.get_text(), 'Tom Trewinnard, Syli: "The climate story needs to be a human story"')
        check.is_true(page.btn_16_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_17_news_slide.is_visible())
        check.is_true(page.txt_17_news_slide_text.is_visible())
        check.equal(page.txt_17_news_slide_text.get_text(), '"Sustainable livelihood intervention in displacement setting."')
        check.is_true(page.btn_17_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_18_news_slide.is_visible())
        check.is_true(page.txt_18_news_slide_text.is_visible())
        check.equal(page.txt_18_news_slide_text.get_text(), '''Emily Farnworth, Centre for Climate Engagement at Hughes Hall (University of Cambridge):"It's much more powerful when people can hear from their peers"''')
        check.is_true(page.btn_18_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_19_news_slide.is_visible())
        check.is_true(page.txt_19_news_slide_text.is_visible())
        check.equal(page.txt_19_news_slide_text.get_text(), 'Swedish companies can play a leading role in mitigating climate change')
        check.is_true(page.btn_19_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_20_news_slide.is_visible())
        check.is_true(page.txt_20_news_slide_text.is_visible())
        check.equal(page.txt_20_news_slide_text.get_text(),'Sebastián Kind, RELP (formerly Greenmap) and Climate Breakthrough Awardee: “We proved something innovative in Argentina that will benefit many other countries”')
        check.is_true(page.btn_20_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_21_news_slide.is_visible())
        check.is_true(page.txt_21_news_slide_text.is_visible())
        check.equal(page.txt_21_news_slide_text.get_text(), 'Saliem Fakir, African Climate Foundation: "We need to champion our own causes".')
        check.is_true(page.btn_21_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_22_news_slide.is_visible())
        check.is_true(page.txt_22_news_slide_text.is_visible())
        check.equal(page.txt_22_news_slide_text.get_text(), 'Caroline Clark-Maxwell, IFRS Foundation: “If everyone could understand each other, we could do the impossible.”')
        check.is_true(page.btn_22_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_23_news_slide.is_visible())
        check.is_true(page.txt_23_news_slide_text.is_visible())
        check.equal(page.txt_23_news_slide_text.get_text(), '''"It's a matter of chance where one is born."''')
        check.is_true(page.btn_23_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_24_news_slide.is_visible())
        check.is_true(page.txt_24_news_slide_text.is_visible())
        check.equal(page.txt_24_news_slide_text.get_text(), '“When we started naming heat waves, social change happened”')
        check.is_true(page.btn_24_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_25_news_slide.is_visible())
        check.is_true(page.txt_25_news_slide_text.is_visible())
        check.equal(page.txt_25_news_slide_text.get_text(), 'Shloka Nath, India Climate Collaborative: "It’s not just about the planet, it’s about us."')
        check.is_true(page.btn_25_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_26_news_slide.is_visible())
        check.is_true(page.txt_26_news_slide_text.is_visible())
        check.equal(page.txt_26_news_slide_text.get_text(), 'The IKEA Foundation pledges more than € 11 million in emergency humanitarian aid for Sudan')
        check.is_true(page.btn_26_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_27_news_slide.is_visible())
        check.is_true(page.txt_27_news_slide_text.is_visible())
        check.equal(page.txt_27_news_slide_text.get_text(),'Noah Horowitz, Clean Cooling Collaborative: "We need to be a lot smarter in how we build things and how we use them.”')
        check.is_true(page.btn_27_news_slide.is_clickable())
    page.btn_slider_right_button.click()
    with allure.step(""):
        check.is_true(page.btn_28_news_slide.is_visible())
        check.is_true(page.txt_28_news_slide_text.is_visible())
        check.equal(page.txt_28_news_slide_text.get_text(), '25,000 Health Facilities Across India are Transforming Public Health Systems to address Growing Critical Climate Issues')
        check.is_true(page.btn_28_news_slide.is_clickable())
    with allure.step(""):
        check.is_true(page.btn_29_news_slide.is_visible())
        check.is_true(page.txt_29_news_slide_text.is_visible())
        check.equal(page.txt_29_news_slide_text.get_text(), 'How books can change children’s lives')
        check.is_true(page.btn_29_news_slide.is_clickable())



@allure.story('Тест для проверки главной страницы')
@allure.feature('Проверка юдлка партнеров')
def test_main_partners(web_browser):
    page = MainPage(web_browser)
    page.btn_pip_up_сookies.click()
    element = web_browser.find_element(By.XPATH,'//div[@class="partner-grid"]')
    web_browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(4)
    with allure.step(""):
        check.equal(page.txt_partners_cards.count(), 12)
    elements_partners = [
        (page.txt_partners_block_about_text,"Partners"),
        (page.txt_partners_block_about_text_text,"We build long-term, strategic partnerships with both large and small organisations. Together with our partners, we develop innovative solutions and work to change complex systems, so they benefit the many people and protect our planet.")
    ]
    for elements, elements_text in elements_partners:
        with allure.step(""):
            check.is_true(elements.is_visible())
        with allure.step(""):
            check.equal(elements.get_text(), elements_text)
    elements_partners_buttons = [
        (page.btn_partners_block_more_about_partners_button,"See all partners","https://ikeafoundation.org/partners/"),
        (page.btn_learn_about_our_work_together_button,"Learn more about our work together","https://ikeafoundation.org/focus")
    ]
    for elements, elements_text, elements_url in elements_partners_buttons:
        with allure.step(""):
            check.is_true(elements.is_visible())
        with allure.step(""):
            check.equal(elements.get_text(), elements_text)
        with allure.step(""):
            check.equal(elements.get_attribute("href"), elements_url)
        with allure.step(""):
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
