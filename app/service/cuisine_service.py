import json
import os

class Cuisine:
    def __init__(self):
        self.cuisines = self.__load_all_cuisines()

    def __load_all_cuisines(self):
        try:
            with open(os.path.join(os.path.dirname(__file__), '..', 'data/cuisines.json'), 'r') as file:
                cuisine_data = json.load(file)
            return cuisine_data
        except Exception as e:
            raise Exception('Cuisines not fetched')

    def get_all_cuisines(self):
        try:
            return self.cuisines
        except Exception as e:
            raise Exception('Cuisines not fetched')

    def get_cuisine_by_id(self, id):
        try:
            for cuisine in self.cuisines:
                if cuisine['id'] == id:
                    return cuisine
            return None

        except Exception as e:
            raise Exception('Cuisine details not fetched')