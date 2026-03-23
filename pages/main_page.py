import allure
from data import BASE_URL
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    URL = BASE_URL

    @allure.step("Прокрутить страницу до вопроса FAQ с индексом {index}")
    def scroll_to_faq_question(self, index):
        question_locator = MainPageLocators.faq_question(index)
        self.scroll_to_element(question_locator)

    @allure.step("Кликнуть на вопрос FAQ с индексом {index}")
    def click_faq_question(self, index):
        question_locator = MainPageLocators.faq_question(index)
        self.click_on_element(question_locator)

    @allure.step("Проверить, что вопрос FAQ с индексом {index} раскрылся")
    def is_faq_expanded(self, index):
        question_locator = MainPageLocators.faq_question(index)
        return self.get_attribute(question_locator, "aria-expanded") == "true"
    
    @allure.step("Клик по кнопке Заказать")
    def click_order_button(self, locator):
        self.click_on_element(locator)




