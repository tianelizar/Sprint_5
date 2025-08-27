from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from locators import Locators
from curl import *

class TestConstructorTypes: # переходы к разделам Булки, Соусы, Начинки

    def test_sauces_show_sauces(self, driver): # соусы
        driver.get(main_page)
        sauces = driver.find_element(*Locators.SAUCES)
        sauces.click()
        assert sauces == driver.find_element(*Locators.ACTIVE_TAB)

    def test_buns_show_buns(self, driver): # булки
        driver.get(main_page)
        driver.find_element(*Locators.SAUCES).click() # по умолчанию конструктор стоит на булках, поэтому сначала переключаюсь на соусы
        buns = driver.find_element(*Locators.BUNS)
        buns.click()
        assert buns == driver.find_element(*Locators.ACTIVE_TAB)

    def test_fillings_show_fillings(self, driver): # начинки
        driver.get(main_page)
        fillings = driver.find_element(*Locators.FILLINGS)
        fillings.click()
        assert fillings == driver.find_element(*Locators.ACTIVE_TAB)

        