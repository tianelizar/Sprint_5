from selenium.webdriver.common.by import By

class Locators:
    
    # локаторы на главной странице
    PROFILE_BUTTON = By.XPATH, "//p[text()='Личный Кабинет']" # кнопка ЛК
    LOGIN_MAIN_PAGE = By.XPATH, "//button[text()='Войти в аккаунт']" # кнопка входа в аккаунт
    PLACE_ORDER = By.XPATH, "//button[text()='Оформить заказ']" # кнопка оформить заказ есть только когда пользователь авторизован

    # на странице входа
    EMAIL = By.XPATH, "//label[text()='Email']/following-sibling::input" # поле емейл
    PASSWORD = By.NAME, "Пароль" # поле пароль
    LOGIN_BUTTON = By.XPATH, "//button[text()='Войти']" # кнопка входа

    REGISTER_LINK = By.XPATH, "//a[@href='/register' and text()='Зарегистрироваться']" # ссылка регистрация
    RESET_PASSWORD = By.XPATH, "//a[@href='/forgot-password' and text()='Восстановить пароль']" # ссылка восстановить пароль

    # на странице регистрации
    NAME = By.XPATH, "//label[text()='Имя']/following-sibling::input" # поле Имя
    REGISTER_BUTTON = By.XPATH, "//button[text()='Зарегистрироваться']" # кнопка регистрации
    LOGIN_LINK = By.CSS_SELECTOR, "a.Auth_link__1fOlj[href='/login']" # ссылка на вход, он же на восстановлении пароля
    INVALID_PASSWORD = By.CSS_SELECTOR, "p.input__error.text_type_main-default" # сообщение при некорректном пароле

    # в ЛК
    LOGOUT = By.XPATH, "//button[text()='Выход']" # выход
    CONSTRUCTOR = By.XPATH, "//p[text()='Конструктор']" # переход в конструктор
    LOGO = By.XPATH, "//a[./*[name()='svg' and @width='290' and @height='50']]" # логотип

    # в разделе Конструктор
    BUNS = By.XPATH, "//div[contains(@class, 'tab_tab')]//span[text()='Булки']/.." # булки
    SAUCES = By.XPATH, "//div[contains(@class, 'tab_tab')]//span[text()='Соусы']/.." # соусы
    FILLINGS = By.XPATH, "//div[contains(@class, 'tab_tab')]//span[text()='Начинки']/.." # начинки
    ACTIVE_TAB = By.XPATH, "//div[contains(@class, 'tab_tab') and contains(@class, 'tab_tab_type_current')]" # активный раздел