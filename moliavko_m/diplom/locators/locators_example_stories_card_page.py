import os

from moliavko_m.diplom.page.base_page import WebPage
from moliavko_m.diplom.page.elements import WebElement
from moliavko_m.diplom.page.elements import ManyWebElements



class StoriesCard(WebPage):

    def __init__(self, web_driver, url='https://ikeafoundation.org/stories/post-cop29-reflections-a-call-to-action-for-funders/'):
        if not url:
            url = os.getenv("MAIN_URL") or ''

        super().__init__(web_driver, url)
    ###
    btn_pip_up_cookies = WebElement(xpath='//button[@class="vogdprc-button vogdprc-button--accept"]')
    ###
    txt_main_text = WebElement(xpath='//h1[@class="entry__title border-header h2"]')
    txt_data = WebElement(xpath='//h2[@class="entry__date h5"]')
    txt_about_news_text = WebElement(xpath='//h3[@class="vo-block-heading wp-block-heading"]')
    txt_text_of_card = WebElement(xpath='//div[@class="entry__columns entry__wrapper"]')
    txt_share_article = WebElement(xpath='//div[@class="share-widget__title h5"]')
    txt_social = WebElement(xpath='//h2[@class="border-header"]')
    txt_social_about = WebElement(xpath='//p[@class="no-margin"]')
    current_page = WebElement(xpath='//span[@class="breadcrumb_last"]')
    ###
    btn_home = WebElement(xpath='(//a[@href="https://ikeafoundation.org/"])[2]')
    btn_stories = WebElement(xpath='(//a[@href="https://ikeafoundation.org/stories/"])[2]')
    btn_twitter = WebElement(xpath='//a[@aria-label="Share on Twitter"]')
    btn_facebook = WebElement(xpath='//a[@aria-label="Share on Facebook"]')
    btn_linkedin = WebElement(xpath='//a[@aria-label="Share on LinkedIn"]')
    btn_insta = WebElement(xpath='//a[@href="https://www.instagram.com/ikea_foundation"]')
    btn_links_insta = ManyWebElements(xpath='//a[@class="zoom-instagram-link magnific-active"]')
    ###
    png = WebElement(xpath='(//img)[1]')

