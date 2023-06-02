import json
import os

class Category:
    def __init__(self):
        self.categories = self.__load_all_categories()

    def __load_all_categories(self):
        try:
            with open(os.path.join(os.path.dirname(__file__), '..', 'data/categories.json'), 'r') as file:
                category_data = json.load(file)
            return category_data
        except Exception as e:
            raise Exception('Categorys not fetched')

    def get_all_categories(self):
        try:
            return self.categories
        except Exception as e:
            raise Exception('Categorys not fetched')

    def get_category_by_id(self, id):
        try:
            for category in self.categories:
                if category['id'] == id:
                    return category
            return None

        except Exception as e:
            raise Exception('Category details not fetched')