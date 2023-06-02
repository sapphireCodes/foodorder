# foodorder-api

## Below are the apis you can use for fetching the required data:

#### 1. Fetching All Restaurants : [GET] https://foodorder-api-elti.onrender.com/v1/restaurants
#### 2. Fetching single Restaurant based on product id : [GET] https://foodorder-api-elti.onrender.com/v1/restaurants/<int:id>
#### 1. Fetching All Categories : [GET] https://foodorder-api-elti.onrender.com/v1/categories
#### 2. Fetching single Category based on product id : [GET] https://foodorder-api-elti.onrender.com/v1/categories/<int:id>
#### 3. Fetching All Cuisines : [GET] https://foodorder-api-elti.onrender.com/v1/cuisines
#### 4. Fetching single Cuisine based on product id : [GET] https://foodorder-api-elti.onrender.com/v1/cuisines/<int:id>
#### 5. Fetching All Users: [GET] https://foodorder-api-elti.onrender.com/v1/users
#### 6. Fetching single user data based on user id: [GET] https://foodorder-api-elti.onrender.com/v1/users/<int:id>
#### 7. login API : [POST] https://foodorder-api-elti.onrender.com/v1/login. - Request Body - {username, password}

## Running the app using the below command
        gunicorn -w 4 -b 0.0.0.0 'main:app'
