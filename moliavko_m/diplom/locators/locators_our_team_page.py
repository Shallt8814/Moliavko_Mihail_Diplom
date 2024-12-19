import os

from moliavko_m.diplom.page.base_page import WebPage
from moliavko_m.diplom.page.elements import WebElement
from moliavko_m.diplom.page.elements import ManyWebElements



class OurTeam(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://ikeafoundation.org/team/'

        super().__init__(web_driver, url)
    ###
    btn_pip_up_cookies = WebElement(xpath='//button[@class="vogdprc-button vogdprc-button--accept"]')
    ###
    txt_meet_our_team = WebElement(xpath='(//h2[@class="border-header"])[1]')
    txt_meet_our_team_about = WebElement(xpath='//p[@class="vo-block-paragraph is-style-lead has-black-color has-text-color"]')
    ###
    txt_leadership = WebElement(xpath='(//h2[@class="border-header"])[2]')
    txt_jessika_anderen = WebElement(xpath='(//h3[@class="vo-block-heading wp-block-heading has-black-color has-text-color"])[1]')
    txt_Chief_Executive_Officer = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[1]')
    txt_Marilia_Bezerra = WebElement(xpath='(//h3[@class="vo-block-heading wp-block-heading has-black-color has-text-color"])[3]')
    txt_Chief_Programmes_Officer = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[3]')
    txt_Stelios_Kyriakakis = WebElement(xpath='(//h3[@class="vo-block-heading wp-block-heading has-black-color has-text-color"])[5]')
    txt_Chief_Operating_Officer = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[5]')
    txt_Amanda_Coady = WebElement(xpath='(//h3[@class="vo-block-heading wp-block-heading has-black-color has-text-color"])[2]')
    txt_Chief_of_Staff = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[2]')
    txt_Christa_Berends = WebElement(xpath='(//h3[@class="vo-block-heading wp-block-heading has-black-color has-text-color"])[4]')
    txt_Chief_People_Officer = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[4]')
    txt_Programmes = WebElement(xpath='(//h2[@class="border-header"])[3]')
    txt_Elizabeth_McKeon = WebElement(xpath='(//h4[@class="vo-block-heading wp-block-heading has-black-color has-text-color"])[1]')
    txt_Programmes_Director_Planet = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[7]')
    txt_Haileselassie_Medhin = WebElement(xpath='(//h4[@class="vo-block-heading wp-block-heading has-black-color has-text-color"])[2]')
    txt_Programmes_Director_People = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[8]')
    txt_Operations = WebElement(xpath='(//h2[@class="border-header"])[4]')
    txt_Feike_Derksen = WebElement(xpath='(//h4[@class="vo-block-heading wp-block-heading has-black-color has-text-color"])[3]')
    txt_General_Counsel = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[9]')
    txt_Jordi_Johannisse = WebElement(xpath='(//h4[@class="vo-block-heading wp-block-heading has-black-color has-text-color"])[4]')
    txt_Head_of_Finance = WebElement(xpath='(//p[@class="vo-block-paragraph has-black-color has-text-color"])[10]')
    txt_Ulrika_Carlsson = WebElement(xpath='//p[@class="vo-block-paragraph is-style-lead"]')
    txt_Head_of_Grant_Operations = WebElement(xpath='//p[@class="vo-block-paragraph"]')
    ###
    png_jessika_anderen = WebElement(xpath='(//img[@decoding="async"])[1]')
    png_Marilia_Bezerra = WebElement(xpath='(//img[@decoding="async"])[3]')
    png_Stelios_Kyriakakis = WebElement(xpath='(//img[@decoding="async"])[5]')
    png_Amanda_Coady = WebElement(xpath='(//img[@decoding="async"])[2]')
    png_Christa_Berends = WebElement(xpath='(//img[@decoding="async"])[4]')
    png_Elizabeth_McKeon = WebElement(xpath='(//img[@decoding="async"])[6]')
    png_Haileselassie_Medhin = WebElement(xpath='(//img[@decoding="async"])[7]')
    png_Feike_Derksen = WebElement(xpath='(//img[@decoding="async"])[8]')
    png_Jordi_Johannisse = WebElement(xpath='(//img[@decoding="async"])[9]')
    png_Ulrika_Carlsson = WebElement(xpath='(//img[@decoding="async"])[10]')
    ###
    png_many_png = ManyWebElements(xpath='//img[@decoding="async"]')


