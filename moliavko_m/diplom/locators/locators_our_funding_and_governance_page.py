import os

from moliavko_m.diplom.page.base_page import WebPage
from moliavko_m.diplom.page.elements import WebElement




class OurFundingAndGovernance(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://ikeafoundation.org/our-funding-and-governance/'

        super().__init__(web_driver, url)

    btn_pip_up_cookies = WebElement(xpath='//button[@class="vogdprc-button vogdprc-button--accept"]')
    ###
    txt_funding = WebElement(xpath='(//h2[@class="border-header"])[1]')
    txt_the_ikea_foundation = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[1]')
    txt_ingka_foundation = WebElement(xpath='(//strong)[1]')
    txt_imas_foundation = WebElement(xpath='(//strong)[2]')
    txt_ikea_foundation = WebElement(xpath='(//strong)[3]')
    txt_governance = WebElement(xpath='(//h2[@class="border-header"])[2]')
    txt_the_ikea_foundation_board = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[2]')
    txt_anders_moberg = WebElement(xpath='(//strong)[4]')
    txt_chairperson = WebElement(xpath='(//p[@class="vo-block-paragraph"])[2]')
    txt_jonas_kamprad = WebElement(xpath='(//strong)[6]')
    txt_krister_mattson = WebElement(xpath='(//strong)[7]')
    txt_peter_kamprad= WebElement(xpath='(//strong)[8]')
    ###
    png_anders_moberg = WebElement(xpath='(//img[@decoding="async"])[1]')
    png_johan_kuylenstierna = WebElement(xpath='(//img[@decoding="async"])[2]')
    png_jonas_kamprad = WebElement(xpath='(//img[@decoding="async"])[3]')
    png_krister_mattson = WebElement(xpath='(//img[@decoding="async"])[4]')
    png_peter_kamprad = WebElement(xpath='(//img[@decoding="async"])[5]')


