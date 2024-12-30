import os

from moliavko_m.diplom.page.base_page import WebPage
from moliavko_m.diplom.page.elements import WebElement
from moliavko_m.diplom.page.elements import ManyWebElements



class Partners(WebPage):

    def __init__(self, web_driver, url='https://ikeafoundation.org/partners/'):
        if not url:
            url = os.getenv("MAIN_URL") or ''

        super().__init__(web_driver, url)
    ###
    btn_pip_up_cookies = WebElement(xpath='//button[@class="vogdprc-button vogdprc-button--accept"]')
    ###
    txt_partners_text = WebElement(xpath='//h1[@class="archive-page__title border-header h2"]')
    txt_partners_text_about = WebElement(xpath='//div[@class="archive-page__description h4"]')
    ###
    txt_partners_cards = ManyWebElements(xpath='//div[@class="partner-card__content"]')
    ###
    btn_partner_01 = WebElement(xpath='(//div[@class="partner-card__content"])[1]')
    btn_partner_01_grants = WebElement(xpath='(//a[@class="link"])[1]')
    btn_partner_01_articles = WebElement(xpath='(//a[@class="link"])[2]')
    btn_partner_01_site = WebElement(xpath='(//a[@class="partner-card__url"])[1]')
    png_partner_01_logo = WebElement(xpath='(//img)[1]')
    ###
    btn_partner_02 = WebElement(xpath='(//div[@class="partner-card__content"])[19]')
    btn_partner_02_grants = WebElement(xpath='(//a[@class="link"])[23]')
    btn_partner_02_articles = WebElement(xpath='(//a[@class="link"])[24]')
    btn_partner_02_site = WebElement(xpath='(//a[@class="partner-card__url"])[19]')
    png_partner_02_logo = WebElement(xpath='(//img)[37]')
    ###
    btn_partner_03 = WebElement(xpath='(//div[@class="partner-card__content"])[158]')
    btn_partner_03_site = WebElement(xpath='(//a[@class="partner-card__url"])[158]')
    btn_partner_03_grants = WebElement(xpath='(//a[@class="link"])[216]')
    btn_partner_03_articles = WebElement(xpath='(//a[@class="link"])[215]')
    btn_partner_03_relises = WebElement(xpath='(//a[@class="link"])[216]')
    png_partner_03_logo = WebElement(xpath='(//img)[37]')
