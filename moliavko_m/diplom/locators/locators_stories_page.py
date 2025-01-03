import os

from moliavko_m.diplom.page.base_page import WebPage
from moliavko_m.diplom.page.elements import WebElement
from moliavko_m.diplom.page.elements import ManyWebElements



class Stories(WebPage):

    def __init__(self, web_driver, url='https://ikeafoundation.org/stories/'):
        if not url:
            url = os.getenv("MAIN_URL") or ''

        super().__init__(web_driver, url)
    ###
    btn_pip_up_cookies = WebElement(xpath='//button[@class="vogdprc-button vogdprc-button--accept"]')
    ###
    txt_stories = WebElement(xpath='//h1[@class="archive-page__title border-header h2"]')
    txt_category = WebElement(xpath='(//span[@class="filter__label"])[1]')
    txt_sort_by = WebElement(xpath='(//span[@class="filter__label"])[2]')
    stories_cards = ManyWebElements(xpath='//div[@class="column span-4-lg span-4-md span-4-sm post-card__wrapper"]')
    ###
    btn_select_category = WebElement(xpath='//select[@name="category"]')
    btn_sort_by = WebElement(xpath='//select[@name="orderby"]')
    btn_search = WebElement(xpath='//input[@placeholder="Search for a keyword"]')
    btn_previous = WebElement(xpath='//a[@class="prev page-numbers"]')
    btn_next = WebElement(xpath='//a[@class="next page-numbers"]')
    btn_1_page = WebElement(xpath='(//a[@class="page-numbers"])[1]')
    btn_2_page = WebElement(xpath='(//a[@class="page-numbers"])[1]')
    ###
    exp_card_btn = WebElement(xpath='//a[@href="https://ikeafoundation.org/stories/post-cop29-reflections-a-call-to-action-for-funders/"]')
    exp_card_text = WebElement(xpath='(//div[@class="post-card__excerpt"])[1]')
    ###
    searched_element = WebElement(xpath='(//div[@class="post-card__excerpt"])[1]')
    ###
    searched_pagination_element = WebElement(xpath='(//div[@class="post-card__excerpt"])[1]')











