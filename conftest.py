import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from curl import *
from data import Credentials
from locators import Locators


@pytest.fixture
def driver():
    # Создаем опции для Chrome
    options = Options()
    options.add_argument("--window-size=1200,600")  
    driver = webdriver.Chrome(options=options)
    
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    
    # фикстура для авторизации пользователя
    driver.get(login_page)
    driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    return driver


