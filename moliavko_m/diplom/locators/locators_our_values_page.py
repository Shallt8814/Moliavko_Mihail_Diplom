import os

from moliavko_m.diplom.page.base_page import WebPage
from moliavko_m.diplom.page.elements import WebElement
from moliavko_m.diplom.page.elements import ManyWebElements



class OurValues(WebPage):

    def __init__(self, web_driver, url='https://ikeafoundation.org/values/'):
        if not url:
            url = os.getenv("MAIN_URL") or ''

        super().__init__(web_driver, url)
    ###
    btn_pip_up_cookies = WebElement(xpath='//button[@class="vogdprc-button vogdprc-button--accept"]')
    ###
    txt_values = WebElement(xpath='//h2[@class="border-header"]')
    txt_at_the_ikea_foundation = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[1]')
    txt_our_values = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[2]')
    txt_togetherness = WebElement(xpath='//*[@id="post-32111"]/div/div/div[2]/ul/li[1]')
    txt_caring_for = WebElement(xpath='//*[@id="post-32111"]/div/div/div[2]/ul/li[2]')
    txt_cost_bla_bla = WebElement(xpath='//*[@id="post-32111"]/div/div/div[2]/ul/li[3]')
    txt_simplicity = WebElement(xpath='//*[@id="post-32111"]/div/div/div[2]/ul/li[4]')
    txt_renew = WebElement(xpath='//*[@id="post-32111"]/div/div/div[2]/ul/li[5]')
    txt_different = WebElement(xpath='//*[@id="post-32111"]/div/div/div[2]/ul/li[6]')
    txt_give = WebElement(xpath='//*[@id="post-32111"]/div/div/div[2]/ul/li[7]')
    txt_lead = WebElement(xpath='//*[@id="post-32111"]/div/div/div[2]/ul/li[8]')
    txt_our_framework = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[3]')
    txt_the_work_of_ikea = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[4]')
    txt_we_do_not = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[5]')
    txt_if_you_suspect = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[6]')
    txt_what_is_misconduct = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[7]')
    txt_misconduct_is = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[8]')
    txt_how_can_i_rise = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[9]')
    txt_the_ikea_foundation = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[10]')
    txt_this_trust = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[11]')
    txt_we_will = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[12]')
    txt_photo_text = WebElement(xpath='//figcaption[@class="wp-element-caption"]')
    ###
    btn_report_a_concern = WebElement(xpath='//a[@class="wp-block-button__link has-dark-red-background-color has-text-color has-background wp-element-button"]')
    btn_ikea_framework = WebElement(xpath='//a[@href="https://ikeafoundation.org/wp-content/uploads/2022/12/IF_Ethical_Framework_July22_02-1.pdf"]')
    ###
    png_photo = WebElement(xpath='//img[@decoding="async"]')
    ###
    many_points_of_values = ManyWebElements(xpath='//*[@id="post-32111"]/div/div/div[2]/ul/li')