import requests
import json

class Request(object):
    GITHUB_URL = ""

    def __init__(self):
        self.__header = None

    def set_header(self, header):
        self.__header = header

    def get(self, url, data=None):
        response = requests.get(url=url, params=data)

        return self.__parse(response)

    def post(self, url, data):
        response = requests.post(url, data)

        return self.__parse(response)

    def put(self):
        pass

    def delete(self):
        pass

    def patch(self):
        pass

    def __parse(self, response):
        return json.loads(response.json())