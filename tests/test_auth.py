from asyncio import timeout
from random import random

from selene.support.shared import config

from pages.page_tests import Authorization, Registration
import allure
import random


auth = Authorization()
reg = Registration()
mobile = random.randint(11111111111,99999999999)

def test_auth(browser_manager):

    with allure.step('Открыть главную страницу'):
        auth.open()

    with allure.step('Открыть окно авторизации'):
        auth.open_auth_window()

    with allure.step('Ввести номер телефона'):
        auth.type_mobile(mobile)

    with allure.step('Ввести пароль'):
        auth.type_pass('123456789')

    with allure.step('Нажать на кнопку Войти'):
        auth.click_enter_button()
        config.timeout = 3

    with allure.step('Проверка отображения ошибки'):
        auth.check_error('Пользователя с таким телефоном не найдено.')


def test_registration():

    with allure.step('Открыть главную страницу'):
        auth.open()

    with allure.step('Открыть окно авторизации'):
        auth.open_auth_window()

    with allure.step('Нажать на кнопку Зарегистрироваться'):
        reg.reg_button()

    with allure.step('Написать невалидную почту'):
        reg.type_email('test123')

    with allure.step('Написать валидный пароль'):
        reg.type_pass('Test12345678-')

    with allure.step('Нажать на кнопку Зарегистрироваться'):
        reg.reg_button_enter()

    with allure.step('Проверка отображения ошибки'):
        auth.check_error('Введите правильный адрес электронной почты.')
