from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from locators import Locators
from curl import *

class TestMainPageButtonLogin: # вход по кнопке «Войти в аккаунт» на главной

    def test_main_page_button_open_login_page(self, driver):
        driver.get(main_page)
        driver.find_element(*Locators.LOGIN_MAIN_PAGE).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        assert login_page in driver.current_url

class TestProfileButtonLogin: # вход через кнопку «Личный кабинет»

    def test_profile_button_open_login_page(self, driver):
        driver.get(main_page)
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        assert login_page in driver.current_url

class TestRegistrationFormLogin: # вход через кнопку в форме регистрации

    def test_registration_form_link_open_login_page(self, driver):
        driver.get(register_page)
        driver.find_element(*Locators.LOGIN_LINK).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        assert login_page in driver.current_url

class TestResetPasswordLogin: # вход через кнопку в форме восстановления пароля

    def test_reset_password_link_open_login_page(self, driver):
        driver.get(password_page)
        driver.find_element(*Locators.LOGIN_LINK).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        assert login_page in driver.current_url

