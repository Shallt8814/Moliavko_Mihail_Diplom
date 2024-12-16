import os

from moliavko_m.diplom.page.base_page import WebPage
from moliavko_m.diplom.page.elements import WebElement
from moliavko_m.diplom.page.elements import ManyWebElements



class IkeaFoundationAboutPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://ikeafoundation.org/about/'

        super().__init__(web_driver, url)

    #cookies
    btn_pip_up_сookies = WebElement(xpath='//button[@class="vogdprc-button vogdprc-button--accept"]')
    ###
    txt_main_text = WebElement(xpath='(//h2[@class="border-header"])[1]')
    txt_main_our_vision = WebElement(xpath='//p[@class="vo-block-paragraph is-style-lead"]')
    img_african_people = WebElement(xpath='(//img[@decoding="async"])[1]')
    txt_african_people_discription = WebElement(xpath='//figcaption[@class="wp-element-caption"]')
    txt_about_ikea_foundation = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[1]')
    ###
    txt_block_of_facts = WebElement(xpath='//div[@class="facts grid "]')
    txt_facts = WebElement(xpath='(//h2[@class="border-header"])[2]')
    txt_3_fact = ManyWebElements(xpath='//div[@class="fact"]')
    txt_147_partners = WebElement(xpath='(//h3[@class="fact__title h3"])[1]')
    txt_support_during_2022 = WebElement(xpath='(//p[@class="fact__description"])[1]')
    txt_n_billion = WebElement(xpath='(//h3[@class="fact__title h3"])[2]')
    txt_granted_by_ikea = WebElement(xpath='(//p[@class="fact__description"])[2]')
    txt_1_billion = WebElement(xpath='(//h3[@class="fact__title h3"])[3]')
    txt_pledged_to_reduce = WebElement(xpath='(//p[@class="fact__description"])[3]')
    ###
    txt_ingvars_vision_block = WebElement(xpath='//div[@class="wp-block-media-text has-media-on-the-right is-stacked-on-mobile is-vertically-aligned-top"]')
    txt_ingvars_vision_about = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[2]')
    txt_ingvars_photo = WebElement(xpath='(//img[@decoding="async"])[2]')
    txt_button_learn_histry_block = WebElement(xpath='//div[@class="wp-block-buttons is-layout-flex wp-block-buttons-is-layout-flex"]')
    btn_learn_about_history = WebElement(xpath='//a[@class="wp-block-button__link wp-element-button"]')
    btn_ingvard_story = WebElement(xpath='//a[@href="https://about.ikea.com/en/about-us/history-of-ikea/from-child-entrepreneur-to-ikea-founder"]')
    ###
    txt_our_focus = WebElement(xpath='(//h2[@class="border-header"])[3]')
    txt_our_focus_people = WebElement(xpath='(//h3[@class="focus__area-header h4"])[1]')
    txt_our_focus_people_text = WebElement(xpath='(//p[@class="focus__area-excerpt"])[1]')
    txt_our_focus_planet = WebElement(xpath='(//h3[@class="focus__area-header h4"])[2]')
    txt_our_focus_planet_text = WebElement(xpath='(//p[@class="focus__area-excerpt"])[2]')
    btn_our_focus_more_button = WebElement(xpath='//a[@class="button"]')







