from selene import browser, have


class AuthAuthorizations:
    AUTH_BUTTON = '.ant-col.ant-col-xs-0 .cy-login-button'
    ENTER_BUTTON = '.kAlGSv'

    def open(self):
        browser.open('/')

    def open_auth_window(self):
        browser.element(self.AUTH_BUTTON).click()

    def type_mobile(self,value):
        browser.element('.ant-input.cy-login-email-input').type(value)

    def type_pass(self,value):
        browser.element('.ant-input-password').type(value)

    def click_enter_button(self):
        browser.element(self.ENTER_BUTTON).click()

    def check_error(self,value):
        browser.element('.frvPfg').should(have.text(value))
        #Пользователя с таким телефоном не найдено

