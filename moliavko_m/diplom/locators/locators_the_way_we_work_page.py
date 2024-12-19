import os

from moliavko_m.diplom.page.base_page import WebPage
from moliavko_m.diplom.page.elements import WebElement
from moliavko_m.diplom.page.elements import ManyWebElements



class TheWayWeWorkPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://ikeafoundation.org/the-way-we-work/'

        super().__init__(web_driver, url)
    ###
    btn_pip_up_cookies = WebElement(xpath='//button[@class="vogdprc-button vogdprc-button--accept"]')
    ###
    png_1 = WebElement(xpath='(//img[@decoding="async"])[1]')
    png_2 = WebElement(xpath='(//img[@decoding="async"])[2]')
    png_3 = WebElement(xpath='(//img[@decoding="async"])[3]')
    png_4 = WebElement(xpath='(//img[@decoding="async"])[4]')
    ###
    txt_under_1_png = WebElement(xpath='(//figcaption[@class="wp-element-caption"])[1]')
    txt_under_2_png = WebElement(xpath='(//figcaption[@class="wp-element-caption"])[2]')
    txt_under_3_png = WebElement(xpath='(//figcaption[@class="wp-element-caption"])[3]')
    txt_under_4_png = WebElement(xpath='(//figcaption[@class="wp-element-caption"])[4]')
    ###
    txt_1_block_text_1 = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[1]')
    txt_1_block_text_2 = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[2]')
    txt_1_block_text_3 = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[3]')
    txt_1_block_text_4 = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[4]')
    txt_1_block_text_5 = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[5]')
    txt_1_block_text_6 = WebElement(xpath='(//li)[13]')
    txt_1_block_text_7 = WebElement(xpath='(//li)[14]')
    txt_1_block_text_8 = WebElement(xpath='(//li)[15]')
    txt_1_block_text_9 = WebElement(xpath='(//li)[16]')
    txt_1_block_text_10 = WebElement(xpath='(//li)[17]')
    txt_1_block_text_11 = WebElement(xpath='(//li)[18]')
    txt_1_block_text_12 = WebElement(xpath='(//li)[19]')
    ###
    txt_2_block_text_1 = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[6]')
    txt_2_block_text_2 = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[7]')
    txt_2_block_text_3 = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[8]')
    txt_2_block_text_4 = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[9]')
    ###
    txt_3_block_text_1 = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[10]')
    txt_3_block_text_2 = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[11]')
    txt_3_block_text_3 = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[12]')
    ###
    txt_4_block_text_1 = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[13]')
    txt_4_block_text_2 = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[14]')
    txt_4_block_text_3 = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[15]')
    txt_4_block_text_4 = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[16]')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    