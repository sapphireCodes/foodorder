from app import app
from app.apis.restaurant_apis import *
from app.apis.category_apis import *
from app.apis.cuisine_apis import *
from app.apis.user_apis import * 

if __name__ == '__main__':
    app.run(debug=True, port=8080)