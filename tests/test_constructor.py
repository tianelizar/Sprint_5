from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from locators import Locators
from curl import *

class TestConstructorTypes: # переходы к разделам Булки, Соусы, Начинки

    def test_sauces_show_sauces(self, driver): # соусы
        driver.get(main_page)
        sauces = driver.find_element(*Locators.SAUCES)
        sauces.click()
        assert "tab_tab_type_current__2BEPc" in sauces.get_attribute("class")

    def test_buns_show_buns(self, driver): # булки
        driver.get(main_page)
        sauces = driver.find_element(*Locators.SAUCES) # по умолчанию конструктор стоит на булках, поэтому сначала переключаюсь на соусы
        sauces.click()
        buns = driver.find_element(*Locators.BUNS)
        buns.click()
        assert "tab_tab_type_current__2BEPc" in buns.get_attribute("class")

    def test_fillings_show_fillings(self, driver): # начинки
        driver.get(main_page)
        fillings = driver.find_element(*Locators.FILLINGS)
        fillings.click()
        assert "tab_tab_type_current__2BEPc" in fillings.get_attribute("class")

        