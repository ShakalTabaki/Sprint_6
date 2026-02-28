import pytest
from data import BASE_URL, DZEN_URL, ORDER_DATA
from pages.order_page import OrderPage
from selenium.webdriver.support.ui import WebDriverWait


class TestOrder:

 
    @pytest.mark.parametrize("order_data", ORDER_DATA)
    def test_order_flow(self, driver, order_data):

        order_page = OrderPage(driver)
        order_page.open()

        order_page = OrderPage(driver)

        order_page.click_coockie_button()
        order_page.fill_first_form(order_data)
        order_page.fill_second_form(order_data)

        assert order_page.is_order_successful()

        order_page.click_look_order_button()

        current_handles = driver.window_handles
        order_page.click_yandex_logo()
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > len(current_handles))
        new_window = [h for h in driver.window_handles if h not in current_handles][0]
        driver.switch_to.window(new_window)
        WebDriverWait(driver, 10).until(lambda d: DZEN_URL in d.current_url)
        assert DZEN_URL in driver.current_url

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        order_page.click_scooter_logo()
        assert BASE_URL in driver.current_url
        