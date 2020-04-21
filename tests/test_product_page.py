from pages.main_page import MainPage
from pages.product_page import ProductPage
from time import sleep


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, link)
    product_page.add_order__to_the_basket()
    page.solve_quiz_and_get_code()
    order_name = product_page.get_name_order()
    price_order = product_page.get_price_order()

    product_page.find_order_name_complete(order_name)
    product_page.find_order_price_complete(price_order)
