import os

from moliavko_m.diplom.page.base_page import WebPage
from moliavko_m.diplom.page.elements import WebElement
from moliavko_m.diplom.page.elements import ManyWebElements



class HeaderFooter(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://ikeafoundation.org/'

        super().__init__(web_driver, url)

    #cookies
    btn_pip_up_cookies = WebElement(xpath='//button[@class="vogdprc-button vogdprc-button--accept"]')

    #header

    btn_button_in_header = WebElement(xpath='//button[@class="hamburger header__navigation-toggle"]')
    btn_logo_button_header = WebElement(xpath='//a[@class="header__branding"]')
    txt_site_navigation_menu_header = WebElement(xpath='//nav[@id="site-navigation"]')
    btn_button_searching = WebElement(xpath='//button[@class="header__navigation-search"]')
    txt_searching_block = WebElement(xpath='//div[@class="header-search search--show"]')
    btn_search_input = WebElement(xpath='//input[@class="search-field"]')
    btn_confirm_search = WebElement(xpath='//input[@class="search-submit"]')

    txt_foundation_week_2023 = WebElement(xpath='//a[@href="https://ikeafoundation.org/23/"]')

    btn_about_us_header = WebElement(xpath='//li[@id="menu-item-35348"]')
    btn_menu_about_us_header_foundation = WebElement(xpath='//a[@href="/about"]')
    btn_menu_about_us_header_themes = WebElement(xpath='//a[@href="/themes"]')
    btn_menu_about_us_header_way_we_work = WebElement(xpath='//a[@href="/about/the-way-we-work"]')
    btn_menu_about_us_header_team = WebElement(xpath='//a[@href="/team"]')
    btn_menu_about_us_header_values = WebElement(xpath='//a[@href="/about/values"]')
    btn_menu_about_us_header_funding = WebElement(xpath='//a[@href="/our-funding-and-governance"]')
    btn_grand_making_header = WebElement(xpath='//a[@href="https://ikeafoundation.org/grants/"]')
    btn_learnings_header = WebElement(xpath='//a[@href="/learnings"]')
    btn_partners_header = WebElement(xpath='//a[@href="/partners"]')
    btn_press_header = WebElement(xpath='//a[@href="/press"]')
    btn_stories_header = WebElement(xpath='//a[@href="https://ikeafoundation.org/stories/"]')

    #footer

    txt_footer_columns = WebElement(xpath='//div[@class="padded container grid"]')
    txt_footer_column_1 = WebElement(xpath='(//div[@class="column span-4-sm span-4-md span-4-lg"])[1]')
    txt_footer_column_2 = WebElement(xpath='(//div[@class="column span-4-sm span-4-md span-4-lg"])[2]')
    txt_footer_column_3 = WebElement(xpath='(//div[@class="column span-4-sm span-4-md span-4-lg"])[3]')
    txt_ikea_foundation_footer = WebElement(xpath='(//h1[@class="h4 footer__title"])[1]')
    btn_FAQ_footer = WebElement(xpath='//*[@href="/faq/"]')
    btn_vacancies_footer = WebElement(xpath='//*[@href="/vacancies/"]')
    btn_privacy_policy_footer = WebElement(xpath='//*[@href="https://ikeafoundation.org/privacy-policy/"]')
    btn_ANBI_footer = WebElement(xpath='//*[@href="https://ikeafoundation.org/anbi-documents/"]')
    btn_documents_footer = WebElement(xpath='//*[@href="https://ikeafoundation.org/documents/"]')
    btn_cookie_preference_footer = WebElement(xpath='//*[@href="#"]')
    txt_logo_button_footer = WebElement(xpath='//*[@class="icon icon--ikea-white "]')
    txt_trust_line_footer = WebElement(xpath='(//h1[@class="h4 footer__title"])[2]')
    txt_trust_text_footer = WebElement(xpath="//*[contains(text(),'The Trust Line enables external stakeholders')]")
    btn_footer_link = WebElement(xpath='//a[@href="https://ikeafoundation.org/values/"]')
    txt_social_media_footer = WebElement(xpath='//h2[@class="h4"]')
    txt_social_media_block_footer = WebElement(xpath='//div[@class="social-media"]')
    btn_twitter_footer = WebElement(xpath='//a[@href="https://twitter.com/IKEAFoundation"]')
    btn_linkedin_footer = WebElement(xpath='//a[@href="https://nl.linkedin.com/company/ikea-foundation"]')
    btn_youtube_footer = WebElement(xpath='//a[@href="https://www.youtube.com/user/IKEAFoundation/"]')
    btn_instagram_footer = WebElement(xpath='//a[@href="https://www.instagram.com/ikea_foundation/"]')

    social_media_footer_blocks = ManyWebElements(xpath='//a[@class="social-button"]')
