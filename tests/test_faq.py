import pytest
from pages.main_page import MainPage
from data import FAQ_COUNT
from selenium.webdriver.support.ui import WebDriverWait


class TestFAQ:


    @pytest.mark.parametrize("index", range(0, FAQ_COUNT))
    def test_faq_questions_expand(self, driver, index):
        page = MainPage(driver)
        page.open()

        page.scroll_to_faq_question(index)
        page.click_faq_question(index)

        assert page.is_faq_expanded(index), \
            f"Вопрос {index} не раскрылся"
        