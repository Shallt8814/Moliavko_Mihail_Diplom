import time
import allure
import pytest_check as check

from moliavko_m.diplom.locators.locators_example_stories_card_page import StoriesCard
from conftest import web_browser



@allure.story("Тест для проверки страницы Stories Card")
@allure.feature('Тест для проверки txt elements')
def test_text_stories_card(web_browser):
    page = StoriesCard(web_browser)
    page.btn_pip_up_cookies.click()
    elements_txt = [
        (page.txt_main_text, "Post-COP29 reflections: A call to action for Funders"),
        (page.txt_data, "DECEMBER 2, 2024"),
        (page.txt_about_news_text, "As COP29 in Azerbaijan has concluded, our co-worker Francesca Rappocciolo shares some takeaways on challenges and opportunities."),
        (page.txt_share_article, "Share article"),
        (page.txt_social, "Social"),
        (page.txt_social_about, "Stay up-to-date and follow us for news and info about exciting grants"),
        (page.current_page, "Post-COP29 reflections: A call to action for Funders"),
    ]
    for elements, elements_text in elements_txt:
        with allure.step("проверка видимости, текста"):
             check.is_true(elements.is_visible())
             check.equal(elements.get_text(), elements_text)
    with allure.step("проверка видимости, текста"):
         check.is_true(page.txt_text_of_card.is_visible())
         check.is_not_none(page.txt_text_of_card.get_text())



@allure.story("Тест для проверки страницы Stories Card")
@allure.feature('Тест для проверки хлебных крошек')
def test_breadcrumbs_stories_card(web_browser):
    page = StoriesCard(web_browser)
    page.btn_pip_up_cookies.click()
    elements_btn = [
        (page.btn_stories,"Stories","https://ikeafoundation.org/stories/"),
        (page.btn_home, "Home","https://ikeafoundation.org/nl/")
    ]
    for elements, elements_text, elements_url in elements_btn:
        with allure.step("проверка видимости, текста, ссылок"):
             check.is_true(elements.is_visible())
             check.equal(elements.get_text(), elements_text)
             check.equal(elements.get_attribute("href"), elements_url)



@allure.story("Тест для проверки страницы Stories Card")
@allure.feature('Тест для проверки кнопок')
def test_btn_stories_card(web_browser):
    page = StoriesCard(web_browser)
    page.btn_pip_up_cookies.click()
    x_coordinate = 0
    y_coordinate = 3200
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(2)
    elements_btn = [
        (page.btn_twitter, "https://twitter.com/intent/tweet?text=https%3A%2F%2Fikeafoundation.org%2Fstories%2Fpost-cop29-reflections-a-call-to-action-for-funders"),
        (page.btn_facebook, "https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fikeafoundation.org%2Fstories%2Fpost-cop29-reflections-a-call-to-action-for-funders"),
        (page.btn_linkedin, "https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fikeafoundation.org%2Fstories%2Fpost-cop29-reflections-a-call-to-action-for-funders&title=&summary=&source="),
    ]
    for elements, elements_url in elements_btn:
        with allure.step("проверка видимости, кликабельности, ссылок"):
             check.is_true(elements.is_visible())
             check.is_true(elements.is_clickable())
             check.equal(elements.get_attribute("href"), elements_url)
    with allure.step("проверка аттрибута рел, ссылки, видимости и кликабельности"):
         check.is_true(page.btn_insta.is_visible())
         check.is_true(page.btn_insta.is_clickable())
         check.equal(page.btn_insta.get_attribute("href"), "https://www.instagram.com/ikea_foundation")
         check.equal(page.btn_insta.get_attribute("rel"), "nofollow")
         check.equal(page.btn_insta.get_text(), "@ikea_foundation")
    x_coordinate = 0
    y_coordinate = 3500
    web_browser.execute_script(f"window.scrollTo({x_coordinate}, {y_coordinate})")
    time.sleep(2)
    with allure.step("проверка кликабельности и количества"):
         check.is_true(page.btn_links_insta.is_clickable())
         check.equal(page.btn_links_insta.count(), 4)



@allure.story("Тест для проверки страницы Stories Card")
@allure.feature('Тест для проверки main png')
def test_png_stories_card(web_browser):
    page = StoriesCard(web_browser)
    page.btn_pip_up_cookies.click()
    element_png = [
        (page.png, "1044", "392")
    ]
    for element, element_width, element_height in element_png:
        with allure.step("проверка видимости, высоты, ширины фото"):
             check.is_true(element.is_visible())
             check.equal(element.get_attribute("width"), element_width)
             check.equal(element.get_attribute("height"), element_height)

