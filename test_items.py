import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestCart():

    def test_add_to_cart_button(self, browser):
        browser.get(link)
        button = browser.find_elements_by_class_name("btn-add-to-basket")

        assert len(button) > 0, "Button for adding to cart not found"
