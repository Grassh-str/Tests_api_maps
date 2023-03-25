from utils.http_methods import Http_methods

base_url = 'https://rahulshettyacademy.com'
key = '?key=qaclick123'

"""Создания, изменения, удаления новой локации"""
class Google_maps_api():

    """Создание новой локации"""

    @staticmethod
    def create_new_place():

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resourse = '/maps/api/place/add/json'
        post_url = base_url + post_resourse + key
        print(post_url)
        result_post = Http_methods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post

    """Проверка создания новой локации"""
    @staticmethod
    def get_new_place(place_id):

        get_resourse = '/maps/api/place/get/json'
        get_url = base_url + get_resourse + key + '&place_id=' + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """Изменение в новой локации"""
    @staticmethod
    def put_new_place(place_id):

        put_resourse = '/maps/api/place/update/json'
        put_url = base_url + put_resourse + key
        print(put_url)
        json_for_update_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = Http_methods.put(put_url, json_for_update_location)
        print(result_put.text)
        return result_put

    """Удаление новой локации"""
    @staticmethod
    def delete_new_place(place_id):

        delete_resourse = '/maps/api/place/delete/json'
        delete_url = base_url + delete_resourse + key
        print(delete_url)
        json_for_delete_location = {
            "place_id": place_id
        }
        result_delete = Http_methods.delete(delete_url, json_for_delete_location)
        print(result_delete.text)
        return result_delete