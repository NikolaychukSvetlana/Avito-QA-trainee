# Инструкция для проведения автотестов.

### Введение
Инструкция составлена для воможности воспроизведения автотестов и получения скриншотов результатов тестов. 
Применяется для счетчиков сохранённого объёма воды, предотвращённого объёма выброса CO2 и сэкономленной электроэнергии раздела "Ваш экологический вклад" сайта https://www.avito.ru/avito-care/eco-impact.
Автотесты написаны с использованием:
- Python
- Pytest
- Playwright

### Техническое описание
Для получения значений счетчиков используется программа test_cases.py. Она подменяет ответ от сервера, cодержащего показания счётчиков, тестовыми данными, расположенными в папке "data". Тестовые данные выбраны в соответствии с техникой тест-дизайна "Тестирование граничных значений".

Программа test_cases.py содержит 12 тест-кейсов:
01. Проверка показаний счетчиков при значении "999".
02. Проверка показаний счетчиков при значении "1 000".
03. Проверка показаний счетчиков при значении "1 001".
04. Проверка показаний счетчиков при значении "999 999".
05. Проверка показаний счетчиков при значении "1 000 000".
06. Проверка показаний счетчиков при значении "1 000 001".
07. Проверка показаний счетчиков при значении "999 999 999".
08. Проверка показаний счетчиков при значении "1 000 000 000".
09. Проверка показаний счетчиков при значении "1 000 000 001".
10. Проверка показаний счетчиков при значении "999 999 999 999".
11. Проверка показаний счетчиков при значении "1 000 000 000 000".
12. Проверка показаний счетчиков при значении "1 000 000 000 001".

Описание тест-кейсов находится в файле "TESTCASES.md".

В результате выполнения каждого тест-кейса программа создаёт скриншот блока со счётчиками. На снимке экрана отражены тестовые данные с показаниями счетчиков после обработки их микрофронтендом. Названия скриншотов соответствуют номерам тест-кейсов.

### Шаги воспроизведения автотестов
1. Установить python, pytest, playwright.
2. Для запуска автотестов выполнить команду в командной строке из корневой папки проекта:
```
pytest --headed
```
3. Дождаться завершения выполнения всех 12 тестов: появится сообщение "12 passed".
4. Перейти в папку "output". Сравнить показания счётчиков на скриншотах с ожидаемыми результатами тест-кейсов.

