# Simple interactive novel generator. Basic project

SING. Базовый проект.

## Требования
1. **Python** версии 3.5 и выше
2. **Модуль pickle** для питона(`pip3 install pickle`)
3. Утилита **make**(пока что движок адаптирован для linux'а) `sudo apt-get install make`

## Для начала своего проекта
1. Скачать базовый проект, используя зеленую кнопку "Download" вверху справа, распаковать
2. Зайти в директорию, запустить **index.html**(для проверки работоспособности)
3. **Редактируя main.py** и периодически запуская **make**(который использует интерпретатор Python), генерируется файл HTML/_bytes.js, который содержит квест в байт-коде
4. **Запускать** используя index.html

## Демо
Демо-видео: https://youtu.be/VKieqWdUf4A?t=30

Демо-проект: https://github.com/NXsing/sing_demo

## Об API

Питоновые функции движка:
1. ```r([название комнаты])``` - начало блока комнаты
2. ```t(текст, [условие], [команда])``` - объявление текста комнаты
3. ```a(текст, команда, [условие])``` - объявление действия в комнате
4. ```e()``` - заверешние блока комнаты

Как видите, движок очень прост.

Есть еще "умная" функция `x(текст, [команда/условие])`, которая сама, на основе формата аргументов, вызывает t() или a(). Это позволяет писать код побыстрее.

## Условия, команды

Основные:
```python
a("Взять книгу","set BOOK","ifset BOOK")
a("Взять книгу","unset BOOK","ifnot BOOK")
a("Идти дальше","goto комната2")
```

Можно комбинировать через ";":
```python
a("Взять книгу","set BOOK;unset HANDFREE;goto room4","ifset BOOK;ifnot VISITED4")
```

Алиасы:
```python
a("Идти дальше","next")
a("Идти дальше","return")
```

## О движке

Питоновые функции(r,t,a,e) генерируют структуры, которые потом конвертируются в байт-код.

Байт-код потом интерпретируется в браузере, используя javascript.

Можно реализовать интерпретатор байт-кода и на любой-другой платформе(всего 15 инструкций). Сам байт-код(пока что) сохраняется в два файла: _bytes.js и bytes.pick

Файл bytes.pick можно импортировать в Питоне:
```python
import pickle
mem=pickle.load( open( "SOURCE/_bytes.pick", "rb" ) ) # байт-код прочитан
```

## Генератор в QSP
При запуске Makefile, автоматически генерируется, в том числе, файл qsp.txt.

Для того, чтобы получить файл квеста QSP, нужно передать [утилите txt2gam](http://qsp.su/index.php?option=com_content&task=view&id=52&Itemid=56) файл qsp.txt:
```
txt2gam.exe qsp.txt game.qsp
```
Для выполнения этой задачи, в дирректории базового проекта есть файл txt2qsp.bat.

Полученный файл game.qsp предназначен для запуска в QSP-плеере, его можно редактировать в программе QGen.

## todo

0. ~~Демонстрация~~
1. Видео по написанию простейшего квеста(использованию API, +multiline strings)
2. Видео по написанию алиасов(img, chain, yt)

## Контакты для связи

1. Почта: x_n хатико) ro.ru
2. NX на Discord-канале ifrus: https://discordapp.com/invite/X86kkzM
