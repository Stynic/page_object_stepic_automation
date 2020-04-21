from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    URL = 'http://selenium1py.pythonanywhere.com/'
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class ProductPageLocators():
    # Кнопка добавления в корзину
    button_add_basket = (By.CSS_SELECTOR, '.btn-add-to-basket')

    # Название товара
    name_order = (By.XPATH, "//*[@class ='col-sm-6 product_main']/h1")
    # Цена товара
    price_oder = (By.XPATH, "//*[@class='price_color']")
