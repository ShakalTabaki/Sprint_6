import pytest
from pages.main_page import MainPage
from data import ORDER_URL
from locators.main_page_locators import MainPageLocators


class TestMainPage:

    @pytest.mark.parametrize("button_locator", [
        MainPageLocators.ORDER_BUTTON_TOP,
        MainPageLocators.ORDER_BUTTON_BOTTOM
    ])
    def test_order_buttons_redirect(self, driver, button_locator):

        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_button(button_locator)

        assert ORDER_URL in driver.current_url
