from playwright.sync_api import Page, Route, expect

def test01(page: Page):
    # Подмена ответа от сервера на данные из файла (значение 999)
    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="data/test1.json"))

    # Открытие страницы
    page.goto('https://www.avito.ru/avito-care/eco-impact')

    # Кликаем по блоку счётчиков для получения скриншота
    page.locator(selector='.desktop-impact-items-F7T6E').click()

    # Сохраняем скриншот
    page.screenshot(type='jpeg', path='output/01.jpeg')

def test02(page: Page):
    # Подмена ответа от сервера на данные из файла (значение 1000)
    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="data/test2.json"))

    # Открытие страницы
    page.goto('https://www.avito.ru/avito-care/eco-impact')

    # Кликаем по блоку счётчиков для получения скриншота
    page.locator(selector='.desktop-impact-items-F7T6E').click()

    # Сохраняем скриншот
    page.screenshot(type='jpeg', path='output/02.jpeg')

def test03(page: Page):
    # Подмена ответа от сервера на данные из файла (значение 1001)
    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="data/test3.json"))

    # Открытие страницы
    page.goto('https://www.avito.ru/avito-care/eco-impact')

    # Кликаем по блоку счётчиков для получения скриншота
    page.locator(selector='.desktop-impact-items-F7T6E').click()

    # Сохраняем скриншот
    page.screenshot(type='jpeg', path='output/03.jpeg')

def test04(page: Page):
    # Подмена ответа от сервера на данные из файла (значение 999999)
    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="data/test4.json"))

    # Открытие страницы
    page.goto('https://www.avito.ru/avito-care/eco-impact')

    # Кликаем по блоку счётчиков для получения скриншота
    page.locator(selector='.desktop-impact-items-F7T6E').click()

    # Сохраняем скриншот
    page.screenshot(type='jpeg', path='output/04.jpeg')

def test05(page: Page):
    # Подмена ответа от сервера на данные из файла (значение 1000000)
    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="data/test5.json"))

    # Открытие страницы
    page.goto('https://www.avito.ru/avito-care/eco-impact')

    # Кликаем по блоку счётчиков для получения скриншота
    page.locator(selector='.desktop-impact-items-F7T6E').click()

    # Сохраняем скриншот
    page.screenshot(type='jpeg', path='output/05.jpeg')

def test06(page: Page):
    # Подмена ответа от сервера на данные из файла (значение 1000001)
    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="data/test6.json"))

    # Открытие страницы
    page.goto('https://www.avito.ru/avito-care/eco-impact')

    # Кликаем по блоку счётчиков для получения скриншота
    page.locator(selector='.desktop-impact-items-F7T6E').click()

    # Сохраняем скриншот
    page.screenshot(type='jpeg', path='output/06.jpeg')

def test07(page: Page):
    # Подмена ответа от сервера на данные из файла (значение 999999999)
    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="data/test7.json"))

    # Открытие страницы
    page.goto('https://www.avito.ru/avito-care/eco-impact')

    # Кликаем по блоку счётчиков для получения скриншота
    page.locator(selector='.desktop-impact-items-F7T6E').click()

    # Сохраняем скриншот
    page.screenshot(type='jpeg', path='output/07.jpeg')

def test08(page: Page):
    # Подмена ответа от сервера на данные из файла (значение 1000000000)
    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="data/test8.json"))

    # Открытие страницы
    page.goto('https://www.avito.ru/avito-care/eco-impact')

    # Кликаем по блоку счётчиков для получения скриншота
    page.locator(selector='.desktop-impact-items-F7T6E').click()

    # Сохраняем скриншот
    page.screenshot(type='jpeg', path='output/08.jpeg')

def test09(page: Page):
    # Подмена ответа от сервера на данные из файла (значение 1000000001)
    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="data/test9.json"))

    # Открытие страницы
    page.goto('https://www.avito.ru/avito-care/eco-impact')

    # Кликаем по блоку счётчиков для получения скриншота
    page.locator(selector='.desktop-impact-items-F7T6E').click()

    # Сохраняем скриншот
    page.screenshot(type='jpeg', path='output/09.jpeg')

def test10(page: Page):
    # Подмена ответа от сервера на данные из файла (значение 999999999999)
    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="data/test10.json"))

    # Открытие страницы
    page.goto('https://www.avito.ru/avito-care/eco-impact')

    # Кликаем по блоку счётчиков для получения скриншота
    page.locator(selector='.desktop-impact-items-F7T6E').click()

    # Сохраняем скриншот
    page.screenshot(type='jpeg', path='output/10.jpeg')

def test11(page: Page):
    # Подмена ответа от сервера на данные из файла (значение 1000000000000)
    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="data/test11.json"))

    # Открытие страницы
    page.goto('https://www.avito.ru/avito-care/eco-impact')

    # Кликаем по блоку счётчиков для получения скриншота
    page.locator(selector='.desktop-impact-items-F7T6E').click()

    # Сохраняем скриншот
    page.screenshot(type='jpeg', path='output/11.jpeg')

def test12(page: Page):
    # Подмена ответа от сервера на данные из файла (значение 1000000000001)
    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="data/test12.json"))

    # Открытие страницы
    page.goto('https://www.avito.ru/avito-care/eco-impact')

    # Кликаем по блоку счётчиков для получения скриншота
    page.locator(selector='.desktop-impact-items-F7T6E').click()

    # Сохраняем скриншот
    page.screenshot(type='jpeg', path='output/12.jpeg')