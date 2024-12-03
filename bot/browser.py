# browser.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Browser:
    def __init__(self):
        self.driver = None

    def start_browser(self):
        # Usa ChromeDriverManager per gestire automaticamente il ChromeDriver
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

    def close_browser(self):
        if self.driver:
            self.driver.quit()

