from dockyard.var import GLOBAL
import requests

class Request(object):
    GITHUB_URL = ""

    def __init__(self):
        self.__headers = None

    def set_header(self, header):
        self.__headers = header

    def get(self, url, data=None):
        GLOBAL.puts("Request: ", data)
        response = requests.get(url=url, params=data, headers=self.__headers)
        return self.__parse(response)

    def post(self, url, data):
        GLOBAL.puts("Request: ", data)
        response = requests.post(url, data=data, headers=self.__headers)
        return self.__parse(response)

    def put(self):
        pass

    def delete(self):
        pass

    def patch(self):
        pass

    def __parse(self, response):
        GLOBAL.puts("Response: ", response.text)
        return response.json()