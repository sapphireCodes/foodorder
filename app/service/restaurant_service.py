import json
import os

class Restaurant:
    def __init__(self):
        self.restaurants = self.__load_all_restaurants()

    def __load_all_restaurants(self):
        try:
            with open(os.path.join(os.path.dirname(__file__), '..', 'data/restaurants.json'), 'r') as file:
                restaurant_data = json.load(file)
            return restaurant_data
        except Exception as e:
            raise Exception('Restaurants not fetched')

    def get_all_restaurants(self):
        try:
            return self.restaurants
        except Exception as e:
            raise Exception('Restaurants not fetched')

    def get_restaurant_by_id(self, id):
        try:
            for restaurant in self.restaurants:
                if restaurant['id'] == id:
                    return restaurant
            return None

        except Exception as e:
            raise Exception('Restaurant details not fetched')