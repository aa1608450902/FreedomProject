import http.client


class HttpMessenger(object):
    @staticmethod
    def send(address, method, url, body):
        connection = http.client.HTTPConnection(address)
        connection.request(method, url, body)
        if method == "get" or method == "GET":
            return None
        elif method == "post" or method == "POST":
            return connection.getresponse().read()
        else:
            return connection.getresponse().read()