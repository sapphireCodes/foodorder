from app import app, jsonify, Cuisine

cuisines = Cuisine()


@app.route('/v1/cuisines')
def get_all_cuisines():
    try:
        return jsonify({
            'data': cuisines.get_all_cuisines()
        }), 200
    except Exception as e:
        return jsonify({
            'message': 'Not able to fetch all cuisines data.'
        }), 400


@app.route('/v1/cuisines/<int:id>')
def get_cuisine_by_id(id):
    try:
        return jsonify({
            'data': cuisines.get_cuisine_by_id(id)
        }), 200
    except Exception as e:
        return jsonify({
            'message': 'Not able to fetch cuisine data with specified id.'
        }), 400
