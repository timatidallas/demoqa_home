from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage


class SwagLabs(BasePage):
    def exit_icon(self):
        try:
            self.find_element(locator='div.login_logo')
        except NoSuchElementException:
            return False
        return True
    def equal_url(self):
        if self.get_url() == 'https://www.saucedemo.com/':
            return True
        return False