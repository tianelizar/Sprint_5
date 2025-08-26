from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from helper import *
from locators import Locators
from curl import *

class TestRegistrationSuccess: # успешная регистрация 

    def test_registration_valid_data_success(self, driver):
        driver.get(register_page)

        name, email, password = generate_valid_registration_data()

        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # ожидание загрузки страницы входа
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))

        # проверка url
        assert login_page in driver.current_url

class TestRegistrationFailed: # ошибка при некорректном пароле

    def test_registration_invalid_password_failed(self, driver):
        driver.get(register_page)

        name, email, bad_password = generate_invalid_registration_data()

        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(bad_password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.INVALID_PASSWORD))

        