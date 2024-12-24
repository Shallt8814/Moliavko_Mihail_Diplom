import os

from moliavko_m.diplom.page.base_page import WebPage
from moliavko_m.diplom.page.elements import WebElement



class ExampleGrant1(WebPage):

    def __init__(self, web_driver, url='https://ikeafoundation.org/grants/non-state-climate-action-integrity-research-and-stakeholder-engagement/'):
        if not url:
            url = os.getenv("MAIN_URL") or ''

        super().__init__(web_driver, url)
    ###
    btn_pip_up_cookies = WebElement(xpath='//button[@class="vogdprc-button vogdprc-button--accept"]')
    ###breadcrumbs
    btn_home = WebElement(xpath='//a[@href="https://ikeafoundation.org/nl/"]')
    btn_grants = WebElement(xpath='(//a[@href="https://ikeafoundation.org/grants/"])[2]')
    txt_current_grant_card = WebElement(xpath='//span[@class="breadcrumb_last"]')
    ###
    txt_none_state_climate = WebElement(xpath='//h1[@class="entry__title border-header h2"]')
    txt_none_state_climate_about = WebElement(xpath='//p[@class="grants-hero__description h4"]')
    ###grant amount
    txt_grant_amount = WebElement(xpath='(//div[@class="grant-payout__title"])[1]')
    txt_date_grant_txt = WebElement(xpath='(//div[@class="grant-payout__title"])[2]')
    txt_date_grant = WebElement(xpath='//div[@class="grant-payout__result"]')
    txt_total_money = WebElement(xpath='//span[@class="grant-payout__total-val"]')
    txt_current_money = WebElement(xpath='//span[@class="grant-payout__paid-val"]')
    progress_bar = WebElement(xpath='//div[@class="grant-payout__paid"]')
    ###
    txt_partner_card = WebElement(xpath='//div[@class="partner-single-card"]')
    btn_partner_link = WebElement(xpath='//a[@class="partner-single-card__link"]')
    btn_all_partners_grants = WebElement(xpath='//a[@class="button button--full"]')
    ###
    txt_share_grant = WebElement(xpath='//div[@class="share-widget__title h5"]')
    btn_share_on_twitter = WebElement(xpath='//a[@aria-label="Share on Twitter"]')
    btn_share_on_facebook = WebElement(xpath='//a[@aria-label="Share on Facebook"]')
    btn_share_on_linkedin = WebElement(xpath='//a[@aria-label="Share on LinkedIn"]')
    ###
    txt_related_articles = WebElement(xpath='//h2[@class="border-header"]')
    txt_card_with_men_text = WebElement(xpath='//div[@class="post-card__excerpt"]')
    btn_human_card_link = WebElement(xpath='//a[@aria-label="Read more"]')
