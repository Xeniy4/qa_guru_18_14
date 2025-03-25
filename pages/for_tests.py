from selene import browser, have

#готово
class Authorization:
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

#готово
class Registration:
    def type_email(self,value):
        browser.element('.cy-registration-email-input').type(value)

    def type_pass(self,value):
        browser.element('.cy-registration-password-input').type(value)

    def check_error(self,value):
        browser.element('.ant-form-item-has-error .ant-form-item-control').should(have.text(value))
        #Введите правильный адрес электронной почты.


class SubscribeTotalAmount:
    def open(self):
        browser.open('/purchase_gift/')

    def scroll(self):
        browser.execute_script("window.scrollBy(0,6000)")

    def select_postcard(self):
        browser.all('.jMEEuK')[2].click()

    def type_text_message_for_recipient(self,value):
        browser.element('.sc-1eoglf1-5').type(value)

    def type_recipient_email(self,value):
        browser.element('.cy-certificate-form-email-input .ant-input').type(value)
        # или .cy-certificate-form-email-input

    def select_tarif(self):
        browser.element('.cy-buy-gift-standard').click()

    def select_period(self):
        browser.element('.cy-payment-period-selector-1').click()

    def select_pay(self):
        browser.element('.cy-payment-method-paypal').click()

    def check_total_amount(self,value):
        browser.element('.czbcvn-4 .sc-bdfBwQ').should(have.text(value))
        #229 руб.


class SubscribeFromBook:

    def open(self):
        browser.open('/catalog/books/')

    def select_book(self):
        browser.all('.e4xwgl-0.iJwsmp')[4].click()

    def click_subscribe(self):
        browser.element('.ant-btn-trial').click()

    def check_text(self,value):
        browser.element('.ant-btn-block').should(have.text(value))
        #Зарегистрироваться


class Podcast:
    def open(self):
        browser.open('/podcasters/')

    def type_email(self,value):
        browser.element('#PodcastSubmitForm_podcast_email').type(value)

    def type_author_name(self,value):
        browser.element('#PodcastSubmitForm_podcast_name').type(value)

    def type_rss(self,value):
        browser.element('#PodcastSubmitForm_podcast_link').type(value)

    def type_comment(self,value):
        browser.element('#PodcastSubmitForm_podcast_comment').type(value)

    def click_button_send(self):
        browser.element('.ant-btn').click()

    def check_error(self,value):
        browser.element('.ant-form-item-explain').should(have.text(value))
        #Вы должны согласиться с условиями


class SearchBook:
    def type_search_text(self,value):
        browser.element('.ant-input').type(value)

    def press_enter(self):
        browser.element('.ant-input').press_enter()

    def check_name_book(self,value):
        browser.element('.e4xwgl-1 .hhskLb').should(have.text(value))
        #Алмазная колесница


