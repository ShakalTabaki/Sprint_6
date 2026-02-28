from pages.base_page import BasePage
from data import ORDER_URL
from locators.order_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure
from selenium.webdriver.support.ui import WebDriverWait


class OrderPage(BasePage):

    URL = ORDER_URL

    @allure.step("Кликнуть на кнопку принятия куки")
    def click_coockie_button(self):
        self.click_on_element(OrderPageLocators.COOKIE_BUTTON)


    @allure.step("Заполнить первую форму")
    def fill_first_form(self, data):
        self.send_keys(OrderPageLocators.NAME_INPUT, data["name"])
        self.send_keys(OrderPageLocators.LAST_NAME_INPUT, data["last_name"])
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, data["address"])
        self.choose_metro_station(data["metro"])
        self.send_keys(OrderPageLocators.PHONE_INPUT, data["phone"])
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)
        self.wait_for_element(OrderPageLocators.DATE_INPUT)

    @allure.step("Выбрать станцию метро")
    def choose_metro_station(self, station_name):
        metro_input = self.wait_for_element(OrderPageLocators.METRO_INPUT)

        metro_input.click()
        metro_input.clear()
        metro_input.send_keys(station_name)
        metro_option_locator = (
            OrderPageLocators.METRO_OPTION[0],
            OrderPageLocators.METRO_OPTION[1].format(station_name)
        )
        option = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(metro_option_locator))
        option.click()

    @allure.step("Выбрать срок аренды")
    def choose_rent_period(self, period):
        self.click_on_element(OrderPageLocators.RENT_PERIOD_DROPDOWN)

        locator = (
            OrderPageLocators.RENT_PERIOD_OPTION[0],
            OrderPageLocators.RENT_PERIOD_OPTION[1].format(period)
        )

        self.click_on_element(locator)

    @allure.step("Выбрать цвет самоката")
    def choose_color(self, color):
        color_map = {
            "black": OrderPageLocators.COLOR_BLACK,
            "grey": OrderPageLocators.COLOR_GREY
        }
        if color in color_map:
            self.click_on_element(color_map[color])

    @allure.step("Заполнить вторую форму")
    def fill_second_form(self, data):
        self.send_keys(OrderPageLocators.DATE_INPUT, data["date"])
        self.wait_for_element(OrderPageLocators.DATE_INPUT).send_keys(Keys.ENTER)
        self.choose_rent_period(data["rent_period"])
        self.choose_color(data["color"])
        self.send_keys(OrderPageLocators.COMMENT_INPUT, data["comment"])
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)
        self.click_on_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Проверить успешное оформление")
    def is_order_successful(self):
        return self.wait_for_element(OrderPageLocators.SUCCESS_MODAL)
    
    @allure.step("Клик по кнопке Посмотреть заказ")
    def click_look_order_button(self):
        self.click_on_element(OrderPageLocators.LOOK_ORDER_BUTTON)
    
    @allure.step("Клик по логотипу Самоката")
    def click_scooter_logo(self):
        self.click_on_element(OrderPageLocators.SCOOTER_LOGO)

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click_on_element(OrderPageLocators.YANDEX_LOGO)