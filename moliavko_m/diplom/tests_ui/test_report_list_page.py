import time
import allure
import pytest_check as check

from moliavko_m.diplom.locators.locators_report_list_page import ReportList
from conftest import web_browser

@allure.story('Проверка страницы Report List')
@allure.feature('Тест для проверки текста')
def test_text_report_list(web_browser):
    page = ReportList(web_browser)
    page.btn_no.click()
    time.sleep(2)
    page.btn_cancel.scroll_to_element()
    elements_txt = [
        (page.txt_main_text,"Welcome to the GAN Integrity Reporting Portal"),
        (page.txt_main_text_about, "Thank you for taking the time to submit a Report. Our Trust Line Team will review your Report and assign the Case for appropriate handling. We will keep you up to date as we go through the process."),
        (page.txt_we_value, "We value your input and want you to feel safe in making this report. At your discretion, you may either:"),
        (page.txt_we_value_points, "Disclose your name and contact information\nStay anonymous throughout the entire process."),
        (page.txt_in_either_case, "In either case, your information will be treated confidentially, and you are protected from retaliation for making this report."),
        (page.txt_in_either_case_points, "If you have any questions about how we handle your data, you can reach out to the compliance team at trustline@ikeafoundation.org."),
        (page.txt_please_identity, "Please identify if you are making this report for yourself, or on behalf of another individual."),
        (page.txt_be_careful, "Be careful not to provide information that may reveal your identity if you wish to remain anonymous."),
        (page.txt_add_information, "Please add information that can help identify other witnesses or participants."),
        (page.txt_if_you_are_not, "If you are not certain of the date, please select a date you think is closest to the incident date."),
        (page.txt_privacy_is_important, "Privacy is important. To protect the submitted data and ensure authorized access in the future, a random password will be automatically generated to secure confidentiality. This captcha helps protect the submission:"),
        (page.txt_privacy, "Privacy"),
        (page.how_are_you_reporting, "How are you reporting your concern? *"),
        (page.organization_concern, "Organisation concern relates to:*"),
        (page.what_relationship_to_ikea, "What is your relationship to the organization?*"),
        (page.do_you_wish_to_be_anonymous, "Do you wish to be anonymous?*"),
        (page.full_name, "Full Name*"),
        (page.e_mail, "E-Mail"),
        (page.phone_number, "Phone Number"),
        (page.in_which_country, "In which country did the incident occur?*"),
        (page.describe_the_concern, "Please describe the concern(s) you want to report, and add as much detail as possible.*"),
        (page.names_and_roles, "Please list the names and roles of the relevant people involved. *"),
        (page.when_was_the_incident, "When did the incident take place?"),
        (page.upload_any_photo, "Please upload any relevant evidence that you feel would be important in relation to this submission")
    ]
    for elements, elements_text in elements_txt:
        with allure.step("проверка видимости, текста "):
             check.is_true(elements.is_visible)
             check.equal(elements.get_text(), elements_text)



@allure.story('Проверка страницы Report List')
@allure.feature('Тест для проверки кнопок')
def test_btn_report_list(web_browser):
    page = ReportList(web_browser)
    time.sleep(2)
    elements_btn = [
        (page.btn_web,"Web"),
        (page.btn_open_door, "Open Door"),
        (page.btn_hot_line, "Hotline"),
        (page.btn_clear_how_are_you_reporting, "Clear Selection"),
        (page.btn_ikea_foundation, "IKEA Foundation"),
        (page.btn_i_am_from_outside, "I’m from outside the organisation and I would like to report an incident or (suspicion of) misconduct in relation to a project or organisation funded by the IKEA Foundation"),
        (page.btn_i_am_an_ikea, "I’m an IKEA Foundation co-worker"),
        (page.btn_clear_what_relationship_to_ikea, "Clear Selection"),
        (page.btn_yes, "Yes"),
        (page.btn_no, "No"),
        (page.btn_clear_do_you_wish_to_be_anonymous, "Clear Selection"),
    ]
    for elements, elements_text in elements_btn:
        with allure.step(""):
             check.is_true(elements.is_visible())
             check.equal(elements.get_text(), elements_text)
             check.is_true(elements.is_clickable())



@allure.story('Проверка страницы Report List')
@allure.feature('Тест для негативной проверки заполнения формы с пустыми полями')
def test_empty_report_list(web_browser):
    page = ReportList(web_browser)
    time.sleep(2)
    page.btn_web.click()
    page.btn_clear_how_are_you_reporting.click()
    page.btn_i_am_an_ikea.click()
    page.btn_clear_what_relationship_to_ikea.click()
    page.btn_no.click()
    page.btn_clear_do_you_wish_to_be_anonymous.click()
    page.select_country.click()
    page.search_country.send_keys("Argentina")
    page.argentina.click()
    time.sleep(1)
    page.btn_clear_in_which_country.click()
    elements_error = [
        (page.this_question_is_required_01, "This question is required"),
        (page.this_question_is_required_02, "This question is required"),
        (page.this_question_is_required_03, "This question is required"),
        (page.this_question_is_required_04, "This question is required"),
        (page.this_question_is_required_05, "This question is required"),
        (page.this_question_is_required_06, "This question is required"),
    ]
    for elements, elements_text in elements_error:
        with allure.step(""):
             check.is_true(elements.is_visible())
             check.equal(elements.get_text(), elements_text)
             page.btn_create_case.scroll_to_element()
             check.is_false(page.btn_create_case.is_clickable())


### !!! ВВЕСТИ ЧТО-НИБУДЬ В КАПЧУ !!! ###
@allure.story('Проверка страницы Report List')
@allure.feature('Тест для  проверки заполнения формы с невалидными данными')
def test_invalid_report_list(web_browser):
    page = ReportList(web_browser)
    page.btn_web.click()
    time.sleep(1)
    page.btn_ikea_foundation.click()
    page.btn_i_am_from_outside.click()
    page.btn_no.click()
    page.input_full_name.send_keys("@@@@")
    page.input_e_mail.send_keys("test")
    page.input_phone_number.send_keys("test")
    page.select_country.click()
    page.search_country.send_keys("Argentina")
    page.argentina.click()
    page.btn_cancel.scroll_to_element()
    page.input_describe_concern.send_keys("@@@@@@@@@")
    page.input_names_and_roles.send_keys("@@@@@@@@@")
    time.sleep(5)
    page.btn_create_case.click()
    time.sleep(1)
    with allure.step(""):
         check.is_false(page.confirm_message.is_visible())



### !!! ВВЕСТИ ФУЛЛ КАПЧУ !!! ###
@allure.story('Проверка страницы Report List')
@allure.feature('Тест для  проверки заполнения формы с валидными данными')
def test_valid_report_list(web_browser):
    page = ReportList(web_browser)
    page.btn_web.click()
    time.sleep(1)
    page.btn_ikea_foundation.click()
    page.btn_i_am_from_outside.click()
    page.btn_no.click()
    page.input_full_name.send_keys("Test")
    page.input_e_mail.send_keys("test@gmail.com")
    page.input_phone_number.send_keys("80170000000")
    page.select_country.click()
    page.search_country.send_keys("Argentina")
    page.argentina.click()
    page.btn_cancel.scroll_to_element()
    page.input_describe_concern.send_keys("Any text")
    page.input_names_and_roles.send_keys("Any text")
    time.sleep(20)
    page.btn_create_case.click()
    time.sleep(6)
    with allure.step(""):
         check.is_false(page.confirm_message.is_visible())
    page.go_back_button.click()
    page.btn_create_case.click()
    page.confirm_button.click()
    with allure.step(""):
         check.equal(page.case_id.get_attribute("id"), "case id")
         check.equal(page.password.get_attribute("id"), "password")
         check.equal(page.go_to_reporting_portal_btn_text.get_text(), "GO TO REPORTING PORTAL")



