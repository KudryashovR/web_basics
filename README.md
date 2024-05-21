### Web Basics

Этот проект является простым HTTP-сервером, написанным на Python с использованием встроенного модуля `http.server`.
Сервер обслуживает HTML-файл, который называется `index.html`.

## Установка

1. Убедитесь, что у вас установлен Python 3.
2. Скачайте или склонируйте этот репозиторий.

## Использование

1. Поместите файл `index.html` в ту же директорию, что и этот скрипт.
2. Запустите скрипт:

```sh
python server.py
```

3. Откройте ваш веб-браузер и перейдите по адресу http://localhost:8080.

## Содержание скрипта

### Импортируемые модули

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
```

Скрипт использует два класса из модуля `http.server`:

- `BaseHTTPRequestHandler`: используется для обработки HTTP-запросов.
- `HTTPServer`: предоставляет инфраструктуру для создания серверов.

### Глобальные переменные

```python
hostName = "localhost"
serverPort = 8080
```

Эти переменные задают имя хоста и порт для сервера.

### Класс MyServer

Этот класс наследуется от `BaseHTTPRequestHandler` и реализует собственную логику обработки запросов:

```python
class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за обработку входящих запросов от клиентов
    """

    filename = "index.html"

    def get_context(self):
        """
        Получение страницы.
        """
        with open(self.filename) as file:
            context = file.read()
        return context

    def do_GET(self):
        """
        Метод для обработки входящих GET-запросов.
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(self.get_context(), "utf-8"))
```

- `get_context`: Метод для чтения содержимого файла `index.html`.
- `do_GET`: Метод для обработки входящих GET-запросов. Отправляет HTTP-ответ со статусом 200 и HTML содержимым файла.

### Основной блок скрипта

```python
if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
```

- Создается и запускается сервер с указанными адресом и портом.
- Сервер начинает непрерывное обслуживание клиентских запросов.
- При прерывании (`KeyboardInterrupt`) сервер останавливается и закрывает соединение.

## Часто задаваемые вопросы

### Почему я получаю ошибку при попытке открыть index.html?

Убедитесь, что файл `index.html` находится в той же директории, что и ваш скрипт. Также проверьте, что файл называется
именно `index.html`.

### Как изменить порт или имя хоста?

Вы можете изменить значения переменных `hostName` и `serverPort` в начале скрипта на те, которые вам необходимы.

### Как добавить поддержку других типов запросов (POST, PUT и т.д.)?

Вы можете добавить поддержку других типов запросов, добавив методы в класс `MyServer`. Например, метод `do_POST` для
обработки POST-запросов.

### Дополнительные ресурсы

- Документация по модулю `http.server` (https://docs.python.org/3/library/http.server.html)

---

Если у вас возникли вопросы или проблемы, пожалуйста, создайте issue в репозитории.