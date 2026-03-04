import pytest
import os
from pages.contact_page import ContactPage

class TestContactForm:
    @pytest.fixture
    def page(self, driver):
        contact_page = ContactPage(driver)
        html_path = os.path.abspath("simple_form.html")
        contact_page.open(f"file://{html_path}")
        return contact_page
    
    def test_positive_submit(self, page):
        page.fill_name("Иван")
        page.fill_email("ivan@mail.ru")
        page.submit()
        assert page.success_displayed()
    
    def test_negative_empty_fields(self, page):
        page.submit()
        assert page.is_visible(page.NAME_ERROR)
        assert page.is_visible(page.EMAIL_ERROR)
        assert not page.success_displayed()
def test_positive_minimal_data(self, page):
    """Тест только с обязательными полями"""
    page.fill_name("Петр")
    page.fill_email("petr@mail.ru")
    page.submit()
    assert page.success_displayed()
