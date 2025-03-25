# 4 и 3 тест поиск в поиске и подкаст
from pages.for_tests import Podcast, SearchBook
import allure

podcast = Podcast
search = SearchBook

def test_add_podcast():

    with allure.step('Открыть страницу добавления подкаста'):
        podcast.open()

    with allure.step('Заполнить поле "Ваша почта"'):
        podcast.type_email('tes12345@test.com')

    with allure.step('Заполнить поле "Имя автора"'):
        podcast.type_author_name('test')

    with allure.step('Заполнить поле "Ссылка на RSS"'):
        podcast.type_rss('https://test.com')

    with allure.step('Заполнить поле "Комментарий"'):
        podcast.type_comment('комментарий тест')

    with allure.step('Нажать на кнопку "Отправить"'):
        podcast.click_button_send()

    with allure.step('Проверка текста ошибки'):
        podcast.check_error('Вы должны согласиться с условиями')


def test_search_book():
    with allure.step('Открыть главную страницу'):
        search.open()

    with allure.step('Написать текст'):
        search.type_search_text('Алмазная колесница')

    with allure.step('Нажать на Enter'):
        search.press_enter()

    with allure.step('Проверка поиска книги'):
        search.check_name_book('Алмазная колесница')

