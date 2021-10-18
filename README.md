# MoreliaClientQt - десктопный клиент MoreliaTalk, написанный с использованием Python и Qt

Кроссплатформенный десктопный клиент для мессенджера MoreliaTalk, использующий гибкость Python и мощь Qt.

## В разработке используется

- [Python 3.9](https://www.python.org/) - язык программирования
- [PyQt5](https://www.riverbankcomputing.com/static/Docs/PyQt5/) - библиотека привязкок для Qt
- [Pillow](https://python-pillow.org/) - библиотека для обработки изображений
- [SQLObject](http://sqlobject.org/) - ORM для работы с базой данный
- [Pydantic](https://pydantic-docs.helpmanual.io/) - валидация данных
- [websockets](https://websockets.readthedocs.io/en/stable/) - библиотека для связи с сервером по протоколу [WebSocket](https://developer.mozilla.org/ru/docs/Web/API/WebSocket)

## Установка

Если вам требуется просто установить клиент, то следуйте ниже приведённым инструкциям.

**Windows:** перейдите во [вкладку релизов](https://github.com/MoreliaTalk/morelia_client_qt/releases), выберите последний релиз и скачайте архив **morelia_client_qt.zip**, распакуйте его, и запустите **.exe** файл внутри каталога

**macOS:** скоро

**Linux:** скоро

## Разработка клиента

### Установка python

Если на вашем компьютере не установлен python, заходим на [официальный сайт](https://www.python.org/) и скачиваем ту версию, которая указана [здесь](#в-разработке-используется)

### Клонирование репозитория на локальный компьютер

Если ты не включен в команду на GitHub'е проекта, то необходимо сначала форкнуть к себе репозиторий MoreliaClientQt перейдя по [ссылке](https://github.com/MoreliaTalk/morelia_client_qt/fork).

Клонировать репозиторий к себе на локальный компьютер используя командную строку и `git`

```cmd
git clone https://github.com/{username}/morelia_client_qt.git
```

Переключаемся на ветку develop

```
git checkout develop
```

При использовании `GitHub Desktop` выбрать в меню `File` пункт `Clone repository...` далее следовать инструкциям

### Установка pipenv

Если у тебя ранее не был установлен менеджер виртуальных окружений **pipenv**, то необходимо установить его командой

```cmd
python -m pip install pipenv
```

### Создание виртуального окружения и установка библиотек

В каталоге склонированного репозитория необходимо выполнить:

```cmd
pipenv shell
```

После чего у нас будет создано новое виртуальное окружение. Теперь пора установить библиотеки:

```cmd
pipenv install --ignore-pipfile
```

```cmd
pipenv install --dev --ignore-pipfile
```

Всё теперь все нужные зависимости установлены!

### Запуск клиента

Выполняем в консоли следующую команду

```cmd
pipenv run python run_client.py
```

## Лицензия

Copyright (c) 2021 - настоящее время [NekrodNIK](https://github.com/NekrodNIK), [rus-ai](https://github.com/rus-ai)

MoreliaClientQt находится под лицензией GNU General Public License версии 3 или более поздней(GPL-3.0-or-later). Подробности смотрите в файле COPYING.

