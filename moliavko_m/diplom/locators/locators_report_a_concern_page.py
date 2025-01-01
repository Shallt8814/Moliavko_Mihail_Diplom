import os

from moliavko_m.diplom.page.base_page import WebPage
from moliavko_m.diplom.page.elements import WebElement
from moliavko_m.diplom.page.elements import ManyWebElements



class ReportAConcern(WebPage):

    def __init__(self, web_driver, url='https://ikeafoundation.org/report-a-concern/'):
        if not url:
            url = os.getenv("MAIN_URL") or ''

        super().__init__(web_driver, url)
    ###
    btn_pip_up_cookies = WebElement(xpath='//button[@class="vogdprc-button vogdprc-button--accept"]')
    ###
    txt_main_text = WebElement(xpath='//h2[@class="border-header"]')
    txt_main_text_about = WebElement(xpath='//p[@class="vo-block-paragraph has-black-color has-text-color"]')
    txt_ikea_foundation = WebElement(xpath='(//h4[@class="vo-block-heading wp-block-heading"])[1]')
    txt_ikea = WebElement(xpath='(//h4[@class="vo-block-heading wp-block-heading"])[2]')
    ###
    btn_1 = WebElement(xpath='(//a[@class="wp-block-button__link wp-element-button"])[1]')
    btn_2 = WebElement(xpath='(//a[@class="wp-block-button__link wp-element-button"])[2]')
    btn_3 = WebElement(xpath='(//a[@class="wp-block-button__link wp-element-button"])[3]')
    btn_4 = WebElement(xpath='(//a[@class="wp-block-button__link wp-element-button"])[4]')
    btn_5 = WebElement(xpath='(//a[@class="wp-block-button__link wp-element-button"])[5]')
    btn_6 = WebElement(xpath='(//a[@class="wp-block-button__link wp-element-button"])[6]')
    ###
    many_btn = ManyWebElements(xpath='//a[@class="wp-block-button__link wp-element-button"]')
    