from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за обработку входящих запросов от клиентов
    """

    __filename = "index.html"

    def get_context(self):
        """
        Получение страницы.
        """

        with open(self.__filename) as file:
            context = file.read()

        return context

    def do_GET(self):
        """
        Метод для обработки входящих GET-запросов
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(self.get_context(), "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()

    print("Server stopped.")