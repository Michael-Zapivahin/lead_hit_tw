## Тестовое задание на должность 'Junior+ Python разработчик'

#### Web-приложение для определения заполненных форм.


#### Как запустить dev-версию приложения


Скачайте код:
```sh
git clone https://github.com/Michael-Zapivahin/lead_hit_tw
```

Перейдите в каталог проекта:
```sh
cd lead_hit_tw
```

[Установите Python](https://www.python.org/), если этого ещё не сделали.

Проверьте, что `python` установлен и корректно настроен. Запустите его в командной строке:
```sh
python --version
```
**Важно!** Версия Python должна быть не ниже 3.10.

Возможно, вместо команды `python` здесь и в остальных инструкциях этого README придётся использовать `python3`. Зависит это от операционной системы и от того,

установлен ли у вас Python старой второй версии.

В каталоге проекта создайте виртуальное окружение:
```sh
python -m venv venv
```
Активируйте его. На разных операционных системах это делается разными командами:

- Windows: `.\venv\Scripts\activate`
- MacOS/Linux: `source venv/bin/activate`


Установите зависимости в виртуальное окружение:
```sh
pip install -r requirements.txt
```

Запустите приложение:

```sh
uvicorn main:app --reload
```


Упаковать приложение в Docker и запустить его по адресу http://localhost/docs
```cli
docker build -t get_template .
docker run -d --name get_template_container -p 80:80 get_template
```


