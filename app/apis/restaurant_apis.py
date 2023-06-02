from app import app, jsonify, Restaurant

restaurants = Restaurant()


@app.route('/v1/restaurants')
def get_all_restaurants():
    try:
        return jsonify({
            'data': restaurants.get_all_restaurants()
        }), 200
    except Exception as e:
        return jsonify({
            'message': 'Not able to fetch all restaurants data.'
        }), 400


@app.route('/v1/restaurants/<int:id>')
def get_restaurant_by_id(id):
    try:
        return jsonify({
            'data': restaurants.get_restaurant_by_id(id)
        }), 200
    except Exception as e:
        return jsonify({
            'message': 'Not able to fetch restaurant data with specified id.'
        }), 400
