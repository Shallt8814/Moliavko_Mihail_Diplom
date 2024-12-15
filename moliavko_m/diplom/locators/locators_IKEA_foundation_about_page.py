import os

from moliavko_m.diplom.page.base_page import WebPage
from moliavko_m.diplom.page.elements import WebElement
from moliavko_m.diplom.page.elements import ManyWebElements



class HeaderFooter(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://ikeafoundation.org/about/'

        super().__init__(web_driver, url)

    #cookies
    btn_pip_up_сookies = WebElement(xpath='//button[@class="vogdprc-button vogdprc-button--accept"]')