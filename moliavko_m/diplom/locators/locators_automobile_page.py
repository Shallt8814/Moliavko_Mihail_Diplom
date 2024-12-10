import os

from  moliavko_m.diplom.page.base_page import WebPage
from moliavko_m.diplom.page.elements import WebElement



class AutomobilePage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("AUTOMOBILE_URL") or 'https://goldenmotors.by/avtomobili/'

        super().__init__(web_driver, url)

    btn_cookies = WebElement(xpath='//*[@data-cky-tag="accept-button"]')
    search_marka_auto = WebElement(xpath='(//div[@data-filter-id="2338"])[1]')
    select_BWM_marka = WebElement(xpath='//option[@data-label="BMW"]')
    search_model_auto = WebElement(xpath='(//div[@data-filter-id="2338"])[2]')
    select_X5_model = WebElement(xpath='//option[@data-label="X5"]')
    search_type_korobka = WebElement(xpath='//div[@data-filter-id="489"]')
    select_automat_korobka = WebElement(xpath='//option[@data-label="автоматическая"]')
    search_type_motor = WebElement(xpath='//div[@data-filter-id="494"]')
    select_benzin_motor = WebElement(xpath='//option[@data-label="бензиновый"]')
    search_type_privod = WebElement(xpath='//div[@data-filter-id="495"]')
    select_full_privod = WebElement(xpath='//option[@data-label="полный"]')
    search_type_kuzova = WebElement(xpath='//div[@data-filter-id="493"]')
    select_vnedorojnik_kusov = WebElement(xpath='//option[@data-label="внедорожник"]')

    block_with_car = WebElement(xpath='//div[@data-post-id="10722"]')