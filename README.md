# Телеграм бот с расписанием преподователей РТУ МИРЭА

## О проекте:
Проект представляет собой бота для телеграма, который позволяет получать расписание `преподавателей РТУ МИРЭА.`


Проект написан на языке `Python` с использованием библиотеки `pyTelegramBotAPI.`


Расписание берется через [API Mirea Ninja](https://github.com/mirea-ninja/rtu-mirea-schedule), который предоставляет расписание в формате `JSON.`

Бот находится в стадии активной разработки, поэтому возможны ошибки и недоработки.
***
## Установка:
Для работы бота необходимо установить следующие библиотеки:

 * `pyTelegramBotAPI`
 * `requests`

Или установить их с помощью файла `requirements.txt`

Создать файл  `config.py` и вставить в него следующий код:

    token = 'Ваш токен'


