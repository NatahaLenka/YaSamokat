import requests
import configuration
import data

def create_order():
    # Шаг 1: Выполнить запрос на создание заказа
    url = configuration.URL_SERVICE + configuration.CREATE_ORDERS
    return requests.post(url, json=data.order_body, headers=data.headers)


def get_order(trackid):
    # Шаг 3: Выполнить запрос на получение заказа по номеру трека
    url = configuration.URL_SERVICE + configuration.GET_ORDERS + str(trackid)
    return  requests.get(url, headers=data.headers)