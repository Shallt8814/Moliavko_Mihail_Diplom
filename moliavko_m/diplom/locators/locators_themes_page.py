import os

from moliavko_m.diplom.page.base_page import WebPage
from moliavko_m.diplom.page.elements import WebElement
from moliavko_m.diplom.page.elements import ManyWebElements



class ThemesPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://ikeafoundation.org/themes/'

        super().__init__(web_driver, url)

    #cookies
    btn_pip_up_cookies = WebElement(xpath='//button[@class="vogdprc-button vogdprc-button--accept"]')
    ###
    txt_themes_text = WebElement(xpath='(//h2[@class="border-header"])[1]')
    txt_themes_text_about = WebElement(xpath='//p[@class="vo-block-paragraph is-style-lead"]')
    txt_themes_people = WebElement(xpath='(//h2[@class="vo-block-heading wp-block-heading"])[1]')
    txt_themes_planet = WebElement(xpath='(//h2[@class="vo-block-heading wp-block-heading"])[2]')
    png_themes_people = WebElement(xpath='(//img[@decoding="async"])[1]')
    png_themes_planet = WebElement(xpath='(//img[@decoding="async"])[2]')
    txt_people_text_about = WebElement(xpath='//p[@class="vo-block-paragraph has-black-color has-text-color"]')
    txt_planet_text_about = WebElement(xpath='//p[@class="vo-block-paragraph has-text-align-left has-black-color has-text-color"]')
    ###
    txt_thematics_areas = WebElement(xpath='(//h2[@class="border-header"])[2]')
    txt_thematic_areas_people = WebElement(xpath='(//div[@class="vo-block-rows__main-title h3 container padded"])[1]')
    txt_renewable_energy = WebElement(xpath='(//div[@class="vo-block-rows__item-title h4"])[1]')
    txt_renewable_energy_about = WebElement(xpath='(//p[@class="vo-block-rows__item-description"])[1]')
    txt_employment = WebElement(xpath='(//div[@class="vo-block-rows__item-title h4"])[2]')
    txt_employment_about= WebElement(xpath='(//p[@class="vo-block-rows__item-description"])[2]')
    txt_agricultural = WebElement(xpath='(//div[@class="vo-block-rows__item-title h4"])[3]')
    txt_agricultural_about= WebElement(xpath='(//p[@class="vo-block-rows__item-description"])[3]')
    txt_refugee = WebElement(xpath='(//div[@class="vo-block-rows__item-title h4"])[4]')
    txt_refugee_about = WebElement(xpath='(//p[@class="vo-block-rows__item-description"])[4]')
    btn_renewable_energy = WebElement(xpath='(//a[@class="vo-block-rows__anchor"])[1]')
    btn_employment = WebElement(xpath='(//a[@class="vo-block-rows__anchor"])[2]')
    btn_agricultural = WebElement(xpath='(//a[@class="vo-block-rows__anchor"])[3]')
    btn_refugee = WebElement(xpath='(//a[@class="vo-block-rows__anchor"])[4]')
    ###
    txt_planet = WebElement(xpath='(//div[@class="vo-block-rows__main-title h3 container padded"])[2]')
    txt_governance = WebElement(xpath='(//div[@class="vo-block-rows__item-title h4"])[5]')
    txt_governance_about = WebElement(xpath='(//p[@class="vo-block-rows__item-description"])[5]')
    txt_real_economy = WebElement(xpath='(//div[@class="vo-block-rows__item-title h4"])[6]')
    txt_real_economy_about = WebElement(xpath='(//p[@class="vo-block-rows__item-description"])[6]')
    btn_governance = WebElement(xpath='(//a[@class="vo-block-rows__anchor"])[5]')
    btn_real_economy = WebElement(xpath='(//a[@class="vo-block-rows__anchor"])[6]')
    ###
    txt_special_initiatives = WebElement(xpath='(//div[@class="vo-block-rows__main-title h3 container padded"])[3]')
    txt_read_more = WebElement(xpath='(//div[@class="vo-block-rows__item-title h4"])[7]')
    txt_read_more_about = WebElement(xpath='(//p[@class="vo-block-rows__item-description"])[7]')
    btn_read_more = WebElement(xpath='(//a[@class="vo-block-rows__anchor"])[7]')
    ###
    txt_many_links = ManyWebElements(xpath='//div[@class="vo-block-rows__item "]')


