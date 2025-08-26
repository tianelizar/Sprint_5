from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from locators import Locators
from curl import *

class TestLoginExistingCredentials: # проверка успешного входа

    def test_login_existing_credentials_success(self, login):
        # заполнение полей через фикстуру
        driver = login
        # подождать, пока прогрузится, и проверить наличие кнопки оформить заказ
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PLACE_ORDER))

class TestProfilePageRedirect: # переход по клику на «Личный кабинет при залогиненном пользователе

    def test_profile_button_open_profile_page(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PLACE_ORDER))
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGOUT))
        assert profile_page in driver.current_url

class TestConstructorFromProfile: # переход по клику на «Конструктор» и на логотип Stellar Burgers

    def test_constructor_open_main_page(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PLACE_ORDER))
        driver.find_element(*Locators.PROFILE_BUTTON).click() 
        # личный кабинет не открывается по прямой ссылке driver.get(profile_page)
        # поэтому здесь и далее дополнительные переходы по клику
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR))
        driver.find_element(*Locators.CONSTRUCTOR).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PLACE_ORDER))
        assert driver.current_url == main_page

    def test_logo_open_main_page(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PLACE_ORDER))
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGO))
        driver.find_element(*Locators.LOGO).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PLACE_ORDER))
        assert driver.current_url == main_page


class TestLogoutButton: # выход по кнопке «Выйти» в личном кабинете

    def test_logout_button_logs_out(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PLACE_ORDER))
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGOUT))
        driver.find_element(*Locators.LOGOUT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        assert login_page in driver.current_url

        