import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
import platform

@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания драйвера"""
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # Новый headless режим
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--remote-debugging-port=9222")
    
    # Определяем ОС и путь к Chrome
    system = platform.system()
    
    if system == "Linux":  # Для GitHub Actions
        chrome_options.binary_location = "/usr/bin/google-chrome"
        service = Service()
    else:  # Для локального запуска на Windows
        from webdriver_manager.chrome import ChromeDriverManager
        service = Service(ChromeDriverManager().install())
    
    driver = webdriver.Chrome(
        service=service,
        options=chrome_options
    )
    
    yield driver
    driver.quit()