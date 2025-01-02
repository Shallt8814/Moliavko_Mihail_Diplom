import os

from moliavko_m.diplom.page.base_page import WebPage
from moliavko_m.diplom.page.elements import WebElement
from moliavko_m.diplom.page.elements import ManyWebElements

class ReportList(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://ikea-foundation.gan-compliance.com/p/Case/create?locale=en-US'

        super().__init__(web_driver, url)
    ###
    btn_pip_up_cookies = WebElement(xpath='//button[@class="vogdprc-button vogdprc-button--accept"]')
    ###
    txt_main_text = WebElement(xpath='//h1[@class="header_1 ng-star-inserted"]')
    txt_main_text_about = WebElement(xpath='(//p)[1]')
    txt_we_value = WebElement(xpath='(//p)[2]')
    txt_we_value_points = WebElement(xpath='(//ul)[1]')
    txt_in_either_case = WebElement(xpath='(//p)[3]')
    txt_in_either_case_points = WebElement(xpath='(//ul)[2]')
    txt_please_identity = WebElement(xpath='(//p)[5]')
    txt_be_careful = WebElement(xpath='(//p)[15]')
    txt_add_information = WebElement(xpath='(//p)[18]')
    txt_if_you_are_not = WebElement(xpath='(//p)[21]')
    txt_privacy_is_important = WebElement(xpath='(//p)[24]')
    txt_privacy = WebElement(xpath='(//h1)[2]')
    ###
    how_are_you_reporting = WebElement(xpath='(//p[@class="gan-typography gan-typography--body1 gan-typography--inherit-color gan-typography--pre-wrap ng-star-inserted"])[1]')
    organization_concern = WebElement(xpath='(//p[@class="gan-typography gan-typography--body1 gan-typography--inherit-color gan-typography--pre-wrap ng-star-inserted"])[2]')
    what_relationship_to_ikea = WebElement(xpath='(//p[@class="gan-typography gan-typography--body1 gan-typography--inherit-color gan-typography--pre-wrap ng-star-inserted"])[3]')
    do_you_wish_to_be_anonymous = WebElement(xpath='(//p[@class="gan-typography gan-typography--body1 gan-typography--inherit-color gan-typography--pre-wrap ng-star-inserted"])[4]')
    full_name = WebElement(xpath='(//p[@class="gan-typography gan-typography--body1 gan-typography--inherit-color gan-typography--pre-wrap ng-star-inserted"])[5]')
    e_mail = WebElement(xpath='(//p[@class="gan-typography gan-typography--body1 gan-typography--inherit-color gan-typography--pre-wrap ng-star-inserted"])[6]')
    phone_number = WebElement(xpath='(//p[@class="gan-typography gan-typography--body1 gan-typography--inherit-color gan-typography--pre-wrap ng-star-inserted"])[7]')
    in_which_country = WebElement(xpath='(//p[@class="gan-typography gan-typography--body1 gan-typography--inherit-color gan-typography--pre-wrap ng-star-inserted"])[8]')
    describe_the_concern = WebElement(xpath='(//p[@class="gan-typography gan-typography--body1 gan-typography--inherit-color gan-typography--pre-wrap ng-star-inserted"])[10]')
    names_and_roles = WebElement(xpath='(//p[@class="gan-typography gan-typography--body1 gan-typography--inherit-color gan-typography--pre-wrap ng-star-inserted"])[11]')
    when_was_the_incident = WebElement(xpath='(//p[@class="gan-typography gan-typography--body1 gan-typography--inherit-color gan-typography--pre-wrap ng-star-inserted"])[12]')
    upload_any_photo = WebElement(xpath='(//p[@class="gan-typography gan-typography--body1 gan-typography--inherit-color gan-typography--pre-wrap ng-star-inserted"])[13]')
    ###
    input_full_name = WebElement(xpath='(//input)[9]')
    input_e_mail = WebElement(xpath='(//input)[10]')
    input_phone_number = WebElement(xpath='(//input)[11]')
    input_describe_concern = WebElement(xpath='(//div[@class="ql-editor ql-blank"])[1]')
    input_names_and_roles = WebElement(xpath='(//div[@class="ql-editor ql-blank"])[1]')
    input_data = WebElement(xpath='(//mat-form-field)[3]')
    ###
    select_country = WebElement(xpath='//div[@id="mat-select-value-1"]')
    search_country = WebElement(xpath='//input[@id="mat-input-0"]')
    many_countries = ManyWebElements(xpath='//mat-option[@role="option"]')
    argentina = WebElement(xpath='//span[text()="Argentina"]')
    belarus = WebElement(xpath='//mat-option[@id="mat-option-771"]')
    india = WebElement(xpath='//mat-option[@id="mat-option-854"]')
    finland = WebElement(xpath='//mat-option[@id="mat-option-826"]')
    btn_clear_in_which_country = WebElement(xpath='(//button)[5]')
    ###
    link_trust_line = WebElement(xpath='//a[@href="trustline@ikeafoundation.org"]')
    ###
    btn_web = WebElement(xpath='(//label[@class="mat-radio-label"])[1]')
    btn_open_door = WebElement(xpath='(//label[@class="mat-radio-label"])[2]')
    btn_hot_line = WebElement(xpath='(//label[@class="mat-radio-label"])[3]')
    btn_clear_how_are_you_reporting = WebElement(xpath='(//button)[2]')
    #
    btn_ikea_foundation = WebElement(xpath='(//span)[31]')
    #
    btn_i_am_from_outside = WebElement(xpath='(//label[@class="mat-radio-label"])[4]')
    btn_i_am_an_ikea = WebElement(xpath='(//label[@class="mat-radio-label"])[5]')
    btn_clear_what_relationship_to_ikea = WebElement(xpath='(//button)[3]')
    #
    btn_yes = WebElement(xpath='(//label[@class="mat-radio-label"])[6]')
    btn_no = WebElement(xpath='(//label[@class="mat-radio-label"])[7]')
    btn_clear_do_you_wish_to_be_anonymous = WebElement(xpath='(//button)[4]')
    #
    btn_create_case = WebElement(xpath='//button[@class="gan-button-next primary"]')
    btn_cancel = WebElement(xpath='//button[@class="gan-button-next default"]')
    ###
    input_captcha = WebElement(xpath='//input[@class="mat-mdc-input-element ng-tns-c1205077789-22 mat-mdc-form-field-input-control mdc-text-field__input cdk-text-field-autofill-monitored ng-touched ng-dirty ng-invalid"]')
    ###
    this_question_is_required_01 = WebElement(xpath="(//*[text()=' This question is required '])[1]")
    this_question_is_required_02 = WebElement(xpath="(//*[text()=' This question is required '])[2]")
    this_question_is_required_03 = WebElement(xpath="(//*[text()=' This question is required '])[3]")
    this_question_is_required_04 = WebElement(xpath="(//*[text()=' This question is required '])[4]")
    this_question_is_required_05 = WebElement(xpath="(//*[text()=' This question is required '])[5]")
    this_question_is_required_06 = WebElement(xpath="(//*[text()=' This question is required '])[6]")
    ###
    something_gone_wrong = WebElement(xpath='//h4[@class="gan-typography gan-typography--header4 gan-typography--inherit-color gan-typography--pre-wrap ng-star-inserted"]')
    how_are_you_reporting_error = WebElement(xpath="//div[@class='gan-button__content ng-star-inserted'][text()=' How are you reporting your concern?  ']")
    organization_concern_error = WebElement(xpath="//div[@class='gan-button__content ng-star-inserted'][text()=' Organisation concern relates to: ']")
    what_relationship_to_ikea_error = WebElement(xpath="//div[@class='gan-button__content ng-star-inserted'][text()=' What is your relationship to the organization? ']")
    do_you_wish_to_be_anonymous_error = WebElement(xpath="//div[@class='gan-button__content ng-star-inserted'][text()=' Do you wish to be anonymous? ']")
    in_which_country_error = WebElement(xpath="//div[@class='gan-button__content ng-star-inserted'][text()=' In which country did the incident occur? ']")
    describe_the_concern_error = WebElement(xpath="//div[@class='gan-button__content ng-star-inserted'][text()=' Please describe the concern(s) you want to report, and add as much detail as possible. ']")
    names_and_roles_error = WebElement(xpath="//div[@class='gan-button__content ng-star-inserted'][text()=' Please list the names and roles of the relevant people involved.  ']")
    ###
    confirm_message = WebElement(xpath='//mat-dialog-container')
    confirm_button = WebElement(xpath='//button[@class="gan-prompt__actions__button gan-prompt__actions__button--confirm ng-star-inserted"]')
    go_back_button = WebElement(xpath='//button[@class="gan-prompt__actions__button ng-star-inserted"]')
    ###
    gan_card = WebElement(xpath='(//gan-card)[3]')
    case_id = WebElement(xpath='(//input)[12]')
    password = WebElement(xpath='(//input)[13]')
    go_to_reporting_portal_btn_text = WebElement(xpath='(//div[@class="gan-button__content ng-star-inserted"])[2]')
    btn_go_to_reporting_portal = WebElement(xpath='(//button)[22]')




