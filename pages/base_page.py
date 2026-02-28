import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return self.driver.current_url

    @allure.step("Открыть страницу")
    def open(self):
        self.driver.get(self.URL)

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=20):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)


    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    @allure.step("Получить атрибут элемента")
    def get_attribute(self, locator, attribute, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.get_attribute(attribute)
    
    @allure.step("Отправить текст в поле")
    def send_keys(self, locator, text, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear() 
        element.send_keys(text)