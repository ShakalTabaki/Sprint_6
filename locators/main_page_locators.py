from selenium.webdriver.common.by import By


class MainPageLocators:

    @staticmethod
    def faq_question(index):
        return (By.ID, f"accordion__heading-{index}")
    
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[2]")

