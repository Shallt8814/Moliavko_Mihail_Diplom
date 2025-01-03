import os

from moliavko_m.diplom.page.base_page import WebPage
from moliavko_m.diplom.page.elements import WebElement

class ReportWindow(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://ikea-foundation.gan-compliance.com/p/Case?locale=en-US'

        super().__init__(web_driver, url)
    ###
    btn_pip_up_cookies = WebElement(xpath='//button[@class="vogdprc-button vogdprc-button--accept"]')
    ###
    select_language = WebElement(xpath='//div [@class="wrapper"]')
    ###
    logo = WebElement(xpath='//img [@alt="logo"]')
    ###
    txt_main_text = WebElement(xpath='//h1 [@class="gan-typography gan-typography--header1 ng-star-inserted"]')
    txt_main_text_about = WebElement(xpath='(//p [@class="gan-typography gan-typography--body2 gan-typography--pre-wrap ng-star-inserted"])[1]')
    txt_contact_info = WebElement(xpath='(//p [@class="gan-typography gan-typography--body2 gan-typography--pre-wrap ng-star-inserted"])[2]')
    txt_or = WebElement(xpath='//span [@class="esp-access-divider__text ng-star-inserted"]')
    txt_call_us = WebElement(xpath='//h2 [@class="gan-typography gan-typography--header2 ng-star-inserted"]')
    txt_powered_by = WebElement(xpath='(//div)[34]')
    txt_error = WebElement(xpath='//p[@class="gan-typography gan-typography--body2 ng-star-inserted"]')
    ###
    btn_create_report = WebElement(xpath='(//div[@class="gan-button__content ng-star-inserted"])[1]')
    btn_view_case = WebElement(xpath='(//div[@class="gan-button__content ng-star-inserted"])[2]')
    btn_powered_by = WebElement(xpath='//a[@href="https://ganintegrity.com/privacy-notice/"]')
    ###
    input_case_id = WebElement(xpath='//input[@id="mat-input-0"]')
    input_password = WebElement(xpath='//input[@id="mat-input-1"]')



