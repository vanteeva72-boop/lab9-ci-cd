from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactPage(BasePage):
    NAME_INPUT = (By.ID, "name")
    EMAIL_INPUT = (By.ID, "email")
    MESSAGE_INPUT = (By.ID, "message")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[onclick='submitForm()']")
    NAME_ERROR = (By.ID, "nameError")
    EMAIL_ERROR = (By.ID, "emailError")
    SUCCESS_MSG = (By.ID, "successMessage")
    FORM = (By.ID, "contactForm")
    
    def open(self, url):
        self.driver.get(url)
    
    def fill_name(self, name):
        self.send_keys(self.NAME_INPUT, name)
    
    def fill_email(self, email):
        self.send_keys(self.EMAIL_INPUT, email)
    
    def submit(self):
        self.click(self.SUBMIT_BUTTON)
    
    def success_displayed(self):
        return self.is_visible(self.SUCCESS_MSG)