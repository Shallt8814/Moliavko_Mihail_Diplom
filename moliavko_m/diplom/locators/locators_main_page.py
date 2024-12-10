import os

from  moliavko_m.diplom.page.base_page import WebPage
from moliavko_m.diplom.page.elements import WebElement



class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://goldenmotors.by'

        super().__init__(web_driver, url)

#header

    btn_headers_logo = WebElement(xpath='(//*[@class="attachment-full size-full wp-image-26"])[1]')
    btn_headers_viber = WebElement(xpath='//*[@class="elementor-icon elementor-social-icon elementor-social-icon-telegram-plane elementor-repeater-item-0e098d6"]')
    btn_headers_telegram = WebElement(xpath='//*[@class="elementor-icon elementor-social-icon elementor-social-icon-telegram-plane elementor-repeater-item-0e098d6"]')
    txt_headers_work_time = WebElement(xpath='(//*[@class="elementor-heading-title elementor-size-default"])[10]')
    btn_headers_first_number = WebElement(xpath='(//*[@class="elementor-heading-title elementor-size-default"])[6]')
    btn_headers_second_number = WebElement(xpath='(//*[@class="elementor-heading-title elementor-size-default"])[7]')
    btn_headers_third_number = WebElement(xpath='(//*[@class="elementor-heading-title elementor-size-default"])[8]')
    btn_headers_services = WebElement(xpath='(//a[@class="elementor-item elementor-item-anchor has-submenu"])[1]')
    # одно нажатие - меню; два нажатия - новая страница
    btn_headers_automobile = WebElement(xpath='(//*[@class="elementor-item"])[1]')
    btn_headers_mototech = WebElement(xpath='(//*[@class="elementor-item"])[2]')
    btn_headers_autowashing = WebElement(xpath='(//a[@class="elementor-item has-submenu"])[1]')
    #одно нажатие - меню; два нажатия - новая страница
    btn_headers_news = WebElement(xpath='(//*[@class="elementor-item"])[3]')
    btn_headers_for_clients = WebElement(xpath='(//*[@class="elementor-item"])[4]')
    btn_headers_contacts = WebElement(xpath='(//*[@class="elementor-item"])[5]')
    btn_headers_maps = WebElement(xpath='//*[@data-id="eb20104"]')
    txt_headers_town = WebElement(xpath='(//*[@class="elementor-heading-title elementor-size-default"])[1]')
    txt_headers_full_addres = WebElement(xpath='(//*[@class="elementor-heading-title elementor-size-default"])[2]')
    txt_headers_tg_viber = WebElement(xpath='//div[@data-id="a6446c4"]')
    txt_headers_numbers = WebElement(xpath='(//*[@class="elementor-heading-title elementor-size-default"])[5]')
    txt_headers_timetxt = WebElement(xpath='(//*[@class="elementor-heading-title elementor-size-default"])[9]')
    btn_cookies = WebElement(xpath='//*[@data-cky-tag="accept-button"]')

#footer

    logo_footer = WebElement(xpath='//*[@data-id="f129ddb"]')
    footer_first_number = WebElement(xpath='//*[@data-id="eb410fc"]')
    footer_second_number = WebElement(xpath='//*[@data-id="9cb8991"]')
    footer_fasebook_icon = WebElement(xpath='//*[@class="elementor-icon elementor-social-icon elementor-social-icon-facebook elementor-repeater-item-8eeb10a"]')
    footer_insta_icon = WebElement(xpath='//*[@class="elementor-icon elementor-social-icon elementor-social-icon-instagram elementor-repeater-item-d2d6cbd"]')
    footer_telegram_icon = WebElement(xpath='//*[@class="elementor-icon elementor-social-icon elementor-social-icon-telegram-plane elementor-repeater-item-bdcb27c"]')
    footer_info_business = WebElement(xpath='//*[@data-id="010eca2"]')
    footer_privacy_policy = WebElement(xpath='//*[@data-id="2169331"]')
    footer_catalog = WebElement(xpath='//*[@data-id="416c502"]')
    footer_automobile = WebElement(xpath='(//*[@class="elementor-icon-list-item"])[1]')
    footer_mototech = WebElement(xpath='(//*[@class="elementor-icon-list-item"])[2]')
    footer_services = WebElement(xpath='//*[@data-id="15723e8"]')
    footer_commission_sell = WebElement(xpath='(//*[@class="elementor-icon-list-item"])[3]')
    footer_urgent_car_purchase = WebElement(xpath='(//*[@class="elementor-icon-list-item"])[4]')
    footer_trade_in = WebElement(xpath='(//*[@class="elementor-icon-list-item"])[5]')
    footer_car_on_credit = WebElement(xpath='(//*[@class="elementor-icon-list-item"])[6]')
    footer_car_for_leasing = WebElement(xpath='(//*[@class="elementor-icon-list-item"])[7]')
    footer_car_selection = WebElement(xpath='(//*[@class="elementor-icon-list-item"])[8]')
    footer_car_made_to_order = WebElement(xpath='(//*[@class="elementor-icon-list-item"])[9]')
    footer_urgent_car_sale = WebElement(xpath='(//*[@class="elementor-icon-list-item"])[10]')
    footer_car_wash = WebElement(xpath='(//*[@class="elementor-icon-list-item"])[11]')
    footer_about_us = WebElement(xpath='//*[@data-id="e781c3b"]')
    footer_news = WebElement(xpath='(//*[@class="elementor-icon-list-item"])[12]')
    footer_blog = WebElement(xpath='(//*[@class="elementor-icon-list-item"])[13]')
    footer_addres = WebElement(xpath='//*[@data-id="2185edf"]')
    footer_wath_on_map = WebElement(xpath='//*[@data-id="6394006"]')
    footer_work_time = WebElement(xpath='//*[@data-id="022233f"]')

#body

    body_block_of_slider = WebElement(xpath='//*[@data-id="5991925"]')
    body_left_button_slider = WebElement(xpath='//*[@class="eicon-chevron-left"]')
    body_right_button_slider = WebElement(xpath='//*[@class="eicon-chevron-right"]')
    body_slider = WebElement(xpath='//*[@id="swiper-wrapper-6c42c89cdf2112de"]')
    body_first_slide = WebElement(xpath='(//*[@data-id="9c2cab3"])[2]')
    body_second_slide = WebElement(xpath='(//*[@data-id="1780416"])[2]')
    body_slider_button_first = WebElement(xpath='//*[@data-bullet-index="0"]')
    body_slider_button_second = WebElement(xpath='//*[@data-bullet-index="1"]')
    body_first_slider_autohouse = WebElement(xpath='(//*[@class="elementor-heading-title elementor-size-default"])[26]')
    body_first_slider_parking = WebElement(xpath='(//*[@class="elementor-heading-title elementor-size-default"])[27]')
    body_first_slider_prices = WebElement(xpath='(//*[@class="elementor-heading-title elementor-size-default"])[28]')
    body_first_slider_purchase_tradein = WebElement(xpath='(//*[@class="elementor-heading-title elementor-size-default"])[29]')
    body_second_slider_motorcycles_in_minsk = WebElement(xpath='(//*[@class="elementor-heading-title elementor-size-default"])[22]')
    body_second_slider_parking = WebElement(xpath='(//*[@class="elementor-heading-title elementor-size-default"])[23]')
    body_second_slider_prices = WebElement(xpath='(//*[@class="elementor-heading-title elementor-size-default"])[24]')
    body_second_slider_purchase_tradein = WebElement(xpath='(//*[@class="elementor-heading-title elementor-size-default"])[25]')
    body_block_of_special_offers = WebElement(xpath='//*[@data-id="c144e70"]')
    body_special_offers = WebElement(xpath='(//*[@class="elementor-heading-title elementor-size-default"])[30]')

    body_block_auto_photo = WebElement(xpath='//*[@data-id="c2a6c71"]')
    body_block_auto_name = WebElement(xpath='(//*[@class="elementor-heading-title elementor-size-default"])[31]')
    body_block_auto_rus_price = WebElement(xpath='//*[@data-id="2e0e9e3"]')
    body_block_auto_us_price = WebElement(xpath='//*[@data-id="576bd46"]')
    body_block_auto_year = WebElement(xpath='//*[@data-id="eeff48e"]')
    body_block_auto_mileage = WebElement(xpath='//*[@data-id="347a106"]')
    body_block_auto_transmission = WebElement(xpath='//*[@data-id="43b2e0c"]')
    body_block_auto_about_button = WebElement(xpath='(//*[@class="elementor-button elementor-button-link elementor-size-sm"])[1]')

    body_block_car_selection = WebElement(xpath='//*[@data-id="d05d9da"]')
    body_block_car_selection_text = WebElement(xpath='//*[@data-id="2fa1c58"]')
    body_block_car_selection_price = WebElement(xpath='//*[@data-id="ba978c4"]')
    body_block_car_selection_model = WebElement(xpath='//*[@data-id="9f347b7"]')
    body_block_car_selection_minmax_price = WebElement(xpath='//*[@data-id="0637cb4"]')
    body_block_car_selection_min_price = WebElement(xpath='(//*[@class="jet-range__inputs__group"])[1]')
    body_block_car_selection_max_price = WebElement(xpath='(//*[@class="jet-range__inputs__group"])[2]')
    body_block_car_selection_min_price_input = WebElement(xpath='(//*[@class="jet-range__inputs__min"])[1]')
    body_block_car_selection_max_price_input = WebElement(xpath='(//*[@class="jet-range__inputs__max"])[1]')
    body_block_car_selection_marka_avto = WebElement(xpath='(//*[@class="jet-select__control depth-0"])[1]')
    body_block_car_selection_button_confirm_filters = WebElement(xpath='(//*[@class="apply-filters__button"])[1]')

    #marka_avto menu
    body_block_car_selection_marka_avto_Audi = WebElement(xpath='//*[@data-label="Audi"]')
    body_block_car_selection_marka_avto_BMW = WebElement(xpath='//*[@data-label="BMW"]')
    body_block_car_selection_marka_avto_Buick = WebElement(xpath='//*[@data-label="Buick"]')
    body_block_car_selection_marka_avto_BYD = WebElement(xpath='//*[@data-label="BYD"]')
    body_block_car_selection_marka_avto_Chrysler = WebElement(xpath='//*[@data-label="Chrysler"]')
    body_block_car_selection_marka_avto_Citroen = WebElement(xpath='//*[@data-label="Citroen"]')
    body_block_car_selection_marka_avto_Dacia = WebElement(xpath='//*[@data-label="Dacia"]')
    body_block_car_selection_marka_avto_Fiesta = WebElement(xpath='//*[@data-label="Fiesta"]')
    body_block_car_selection_marka_avto_Ford = WebElement(xpath='//*[@data-label="Ford"]')
    body_block_car_selection_marka_avto_GMC = WebElement(xpath='//*[@data-label="GMC"]')
    body_block_car_selection_marka_avto_Honda = WebElement(xpath='//*[@data-label="Honda"]')
    body_block_car_selection_marka_avto_Hummer = WebElement(xpath='//*[@data-label="Hummer"]')
    body_block_car_selection_marka_avto_Hyundai = WebElement(xpath='//*[@data-label="Hyundai"]')
    body_block_car_selection_marka_avto_Infiniti = WebElement(xpath='//*[@data-label="Infiniti"]')
    body_block_car_selection_marka_avto_JEEP = WebElement(xpath='//*[@data-label="JEEP"]')
    body_block_car_selection_marka_avto_Kia = WebElement(xpath='//*[@data-label="Kia"]')
    body_block_car_selection_marka_avto_Land_Rover = WebElement(xpath='//*[@data-label="Land Rover"]')
    body_block_car_selection_marka_avto_Lexus = WebElement(xpath='//*[@data-label="Lexus"]')
    body_block_car_selection_marka_avto_Mazda = WebElement(xpath='//*[@data-label="Mazda"]')
    body_block_car_selection_marka_avto_Mercedes_Benz = WebElement(xpath='//*[@data-label="Mercedes-Benz"]')
    body_block_car_selection_marka_avto_Mini = WebElement(xpath='//*[@data-label="Mini"]')
    body_block_car_selection_marka_avto_Mitsubishi = WebElement(xpath='//*[@data-label="Mitsubishi"]')
    body_block_car_selection_marka_avto_Opel = WebElement(xpath='//*[@data-label="Opel"]')
    body_block_car_selection_marka_avto_Peugeot = WebElement(xpath='//*[@data-label="Peugeot"]')
    body_block_car_selection_marka_avto_Porsche = WebElement(xpath='//*[@data-label="Porsche"]')
    body_block_car_selection_marka_avto_Renault = WebElement(xpath='//*[@data-label="Renault"]')
    body_block_car_selection_marka_avto_Skoda = WebElement(xpath='//*[@data-label="Skoda"]')
    body_block_car_selection_marka_avto_Subaru = WebElement(xpath='//*[@data-label="Subaru"]')
    body_block_car_selection_marka_avto_Tesla = WebElement(xpath='//*[@data-label="Tesla"]')
    body_block_car_selection_marka_avto_Toyota = WebElement(xpath='//*[@data-label="Toyota"]')
    body_block_car_selection_marka_avto_Volkswagen = WebElement(xpath='//*[@data-label="Volkswagen"]')
    body_block_car_selection_marka_avto_Volvo = WebElement(xpath='//*[@data-label="Volvo"]')
    body_block_car_selection_marka_avto_Zeekr = WebElement(xpath='//*[@data-label="Zeekr"]')
    body_block_car_selection_marka_avto_Спецпредложения = WebElement(xpath='//*[@data-label="Спецпредложения"]')

    body_block_slider_of_auto = WebElement(xpath='//*[@data-id="8514039"]')
    body_block_slider_of_auto_left_button = WebElement(xpath='(//*[@class="jet-listing-grid__slider-icon prev-arrow slick-arrow"])[1]')
    body_block_slider_of_auto_right_button = WebElement(xpath='(//*[@class="jet-listing-grid__slider-icon next-arrow slick-arrow"])[1]')
    body_block_slider_of_auto_1_slide_button = WebElement(xpath='(//*[@role="presentation"])[4]')
    body_block_slider_of_auto_2_slide_button = WebElement(xpath='(//*[@role="presentation"])[5]')
    body_block_slider_of_auto_3_slide_button = WebElement(xpath='(//*[@role="presentation"])[6]')
    body_block_slider_of_auto_4_slide_button = WebElement(xpath='(//*[@role="presentation"])[7]')
    body_block_slider_of_auto_5_slide_button = WebElement(xpath='(//*[@role="presentation"])[8]')
    body_block_slider_of_auto_6_slide_button = WebElement(xpath='(//*[@role="presentation"])[9]')
    body_block_slider_of_auto_catalog_button = WebElement(xpath='(//*[@class="elementor-button elementor-button-link elementor-size-sm"])[2]')
    #это добро всё ниже появляется:
    body_block_slider_of_auto_element_0 = WebElement(xpath='(//*[@data-slick-index="0"])[2]')
    #при первой кнопке
    body_block_slider_of_auto_element_1 = WebElement(xpath='(//*[@data-slick-index="1"])[1]')
    #при 1,2 кнопках
    body_block_slider_of_auto_element_2 = WebElement(xpath='(//*[@data-slick-index="2"])[1]')
    #при 1,2,3 кнопках
    body_block_slider_of_auto_element_3 = WebElement(xpath='(//*[@data-slick-index="3"])[1]')
    #при 1,2,3,4 кнопках
    body_block_slider_of_auto_element_4 = WebElement(xpath='(//*[@data-slick-index="4"])[1]')
    #при 2,3,4,5 кнопках
    body_block_slider_of_auto_element_5 = WebElement(xpath='(//*[@data-slick-index="5"])[1]')
    #при 3,4,5,6 кнопках
    body_block_slider_of_auto_element_6 = WebElement(xpath='(//*[@data-slick-index="6"])[1]')
    #при 4,5,6 кнопках
    body_block_slider_of_auto_element_7 = WebElement(xpath='(//*[@data-slick-index="7"])[1]')
    #при 5,6 кнопках
    body_block_slider_of_auto_element_8 = WebElement(xpath='(//*[@data-slick-index="8"])[1]')
    #при 6 кнопках

    body_block_1_car_logo = WebElement(xpath='//*[@data-id="a172679"]')
    body_block_2_car_logo = WebElement(xpath='//*[@data-id="e695a50"]')
    body_block_1_car_logo_Hyundai = WebElement(xpath='//*[@data-id="8ec4d4d"]')
    body_block_1_car_logo_Mazda = WebElement(xpath='//*[@data-id="bd53888"]')
    body_block_1_car_logo_Ford = WebElement (xpath='//*[@data-id="b719497"]')
    body_block_1_car_logo_Mersedes = WebElement (xpath='//*[@data-id="72d95ec"]')
    body_block_1_car_logo_Skoda = WebElement (xpath='//*[@data-id="2c69ce2"]')
    body_block_1_car_logo_Chevrolet = WebElement (xpath='//*[@data-id="d783bf6"]')
    body_block_2_car_logo_Pejo = WebElement (xpath='//*[@data-id="c09d221"]')
    body_block_2_car_logo_Kia = WebElement (xpath='//*[@data-id="33b1f77"]')
    body_block_2_car_logo_Wolkswagen = WebElement (xpath='//*[@data-id="20bec27"]')
    body_block_2_car_logo_Opel = WebElement (xpath='//*[@data-id="5829149"]')
    body_block_2_car_logo_Reno = WebElement (xpath='//*[@data-id="f171f59"]')
    body_block_2_car_logo_Volvo = WebElement (xpath='//*[@data-id="1cbdeeb"]')

    body_block_moto_selection = WebElement(xpath='//*[@data-id="e2fa13a"]')
    body_block_moto_selection_text = WebElement(xpath='//*[@data-id="f3662b3"]')
    body_block_moto_selection_price = WebElement(xpath='//*[@data-id="e25878e"]')
    body_block_moto_selection_minmax_price = WebElement(xpath='//*[@data-id="5fb9540"]')
    body_block_moto_selection_min_price = WebElement(xpath='(//*[@class="jet-range__inputs__group"])[3]')
    body_block_moto_selection_max_price = WebElement(xpath='(//*[@class="jet-range__inputs__group"])[4]')
    body_block_moto_selection_min_price_input = WebElement(xpath='(//*[@class="jet-range__inputs__min"])[2]')
    body_block_moto_selection_max_price_input = WebElement(xpath='(//*[@class="jet-range__inputs__max"])[2]')
    body_block_moto_selection_moto_marka = WebElement(xpath='//*[@data-id="efafed1"]')
    body_block_moto_selection_confirm_button = WebElement(xpath='(//*[@class="apply-filters__button"])[2]')

    #moto_marka menu
    body_block_moto_selection_moto_marka_American_Iron_Horse_Legend = WebElement(xpath='//*[@data-label="BMW Motorrad AG"]')
    body_block_moto_selection_moto_marka_BMW_Motorrad_AG = WebElement(xpath='')
    body_block_moto_selection_moto_marka_CFMOTO = WebElement(xpath='')
    body_block_moto_selection_moto_marka_Ducati = WebElement(xpath='')
    body_block_moto_selection_moto_marka_Harley_Davidson = WebElement(xpath='')
    body_block_moto_selection_moto_marka_Honda = WebElement(xpath='(//*[@data-label="Honda"])[2]')
    body_block_moto_selection_moto_marka_Husqvarna = WebElement(xpath='')
    body_block_moto_selection_moto_marka_Indian = WebElement(xpath='')
    body_block_moto_selection_moto_marka_Indian_Chief = WebElement(xpath='')
    body_block_moto_selection_moto_marka_Kawasaki = WebElement(xpath='')
    body_block_moto_selection_moto_marka_KTM = WebElement(xpath='')
    body_block_moto_selection_moto_marka_Piaggio = WebElement(xpath='')
    body_block_moto_selection_moto_marka_Suzuki = WebElement(xpath='')
    body_block_moto_selection_moto_marka_Triumph = WebElement(xpath='')
    body_block_moto_selection_moto_marka_Victory = WebElement(xpath='')
    body_block_moto_selection_moto_marka_Yamaha = WebElement(xpath='')


