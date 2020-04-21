from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_order__to_the_basket(self):
        self.browser.find_element(*ProductPageLocators.button_add_basket).click()

    def get_name_order(self) -> str:
        name_order = self.browser.find_element(
            *ProductPageLocators.name_order).text
        return name_order

    def get_price_order(self) -> str:
        price_order = self.browser.find_element(
            *ProductPageLocators.price_oder).text
        return price_order

    def find_order_name_complete(self, name_order: str):
        try:
            # Успешность добавляния в корзину
            self.browser.find_element_by_xpath(
                f'//*[@class="alertinner "]'
                f'/*[contains(text(),"{name_order}")]')
        except Exception:
            raise Exception(f'Название товара не совпадает - {name_order}')

    def find_order_price_complete(self, price_order: str):
        # Успешность добавляния в корзину
        price_result = self.browser.find_element_by_xpath(
            f'//*[@class="alertinner "]/p/strong').text
        assert price_result == price_order,\
            'Цена товара в корзине не совпадает с ценой товара'
