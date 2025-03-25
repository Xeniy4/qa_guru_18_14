from pages.for_tests import SubscribeTotalAmount, SubscribeFromBook, SearchBook
import allure

amount_subscribe = SubscribeTotalAmount
book_subscribe = SubscribeFromBook


def test_total_amount_subscribe():

    with allure.step('Открыть страницу "Подписки"'):
        amount_subscribe.open()

    with allure.step('Выбрать открытку'):
        amount_subscribe.select_postcard()

    with allure.step('Написать текст получателю'):
        amount_subscribe.type_text_message_for_recipient('тест')

    with allure.step('Скролл вниз'):
        amount_subscribe.scroll()

    with allure.step('Написать email получателя'):
        amount_subscribe.type_recipient_email('recipient_test@test.com')

    with allure.step('Выбрать стандартный тариф'):
        amount_subscribe.select_tarif()

    with allure.step('Выбрать период'):
        amount_subscribe.select_period()

    with allure.step('Скролл вниз'):
        amount_subscribe.scroll()

    with allure.step('Выбрать способ оплаты'):
        amount_subscribe.select_pay()

    with allure.step('Проверка итоговой суммы'):
        amount_subscribe.check_total_amount('229 руб.')


def test_subscribe_from_book():

    with allure.step('Открыть страницу Книги'):
        book_subscribe.open()

    with allure.step('Перейти на страницу книги'):
        book_subscribe.select_book()

    with allure.step('Нажать на кнопку "Оформить подписку"'):
        book_subscribe.click_subscribe()

    with allure.step('Проверка отображения кнопки "Зарегистрироваться"'):
        book_subscribe.check_text('Зарегистрироваться')

