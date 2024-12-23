import os

from moliavko_m.diplom.page.base_page import WebPage
from moliavko_m.diplom.page.elements import WebElement
from moliavko_m.diplom.page.elements import ManyWebElements



class GrantMaking(WebPage):

    def __init__(self, web_driver, url='https://ikeafoundation.org/grants'):
        if not url:
            url = os.getenv("MAIN_URL") or ''

        super().__init__(web_driver, url)
    ###
    btn_pip_up_cookies = WebElement(xpath='//button[@class="vogdprc-button vogdprc-button--accept"]')
    ###
    txt_grant_making = WebElement(xpath='//h1[@class="archive-page__title h2 border-header"]')
    txt_we_are_commited = WebElement(xpath='(//p)[1]')
    txt_this_dataset_includes = WebElement(xpath='(//p)[2]')
    txt_this_dataset = WebElement(xpath='(//p)[3]')
    txt_facts = WebElement(xpath='(//h2[@class="border-header"])[1]')
    txt_india_kenya = WebElement(xpath='(//h2[@class="fact__title h3"])[1]')
    txt_top_5 = WebElement(xpath='(//p[@class="fact__description"])[1]')
    txt_15_programme = WebElement(xpath='(//h2[@class="fact__title h3"])[2]')
    txt_currently_ongoing = WebElement(xpath='(//p[@class="fact__description"])[2]')
    txt_dataset = WebElement(xpath='(//h2[@class="border-header"])[2]')
    txt_our_grants_are = WebElement(xpath='//h3[@class="grants-map__title h4"]')
    txt_learnings = WebElement(xpath='(//h2[@class="border-header"])[3]')
    txt_learning_how_to_do = WebElement(xpath='//p[@class="vo-block-paragraph has-black-color has-text-color"]')
    txt_sort_by = WebElement(xpath='//span[@class="filter__label"]')
    txt_x_results_found = WebElement(xpath='//p[@class="grants-filters__results"]')
    txt_archive_cards = ManyWebElements(xpath='//article[@class="grants-card"]')
    ###
    input_search_for_a_keyword = WebElement(xpath='//input[@placeholder="Search for a keyword"]')
    ###
    btn_page = WebElement(xpath='(//a[@class="page-numbers"])[1]')
    btn_next_page = WebElement(xpath='//a[@class="next page-numbers"]')
    btn_previous_page = WebElement(xpath='//a[@class="prev page-numbers"]')
    ###
    #универсально для проверки седектов датасета
    txt_card_thematic_area_latest = WebElement(xpath='(//h2[@class="grants-card__title h4"])[1]')
    txt_card_thematic_area_latest_2 = WebElement(xpath='(//h2[@class="grants-card__title h4"])[2]')
    txt_no_posts = WebElement(xpath='//div[@class="grants-archive__results"]')
    ###
    btn_learn_more = WebElement(xpath='//a[@class="wp-block-button__link wp-element-button"]')
    ###
    btn_card_href = WebElement(xpath='(//a[@class="grants-card__anchor"])[1]')
    btn_little_card_href = WebElement(xpath='(//a[@href])[16]')





