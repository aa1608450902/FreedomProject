import http.client


class HttpMessenger(object):
    @staticmethod
    def send(address, method, url, body):
        connection = http.client.HTTPConnection(address)
        connection.request(method, url, body)
        method = method.upper()
        response = None
        if method != "GET":
            response = connection.getresponse().read()
        connection.close()
        return response