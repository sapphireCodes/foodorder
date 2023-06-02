from app import app, jsonify, Category

categories = Category()


@app.route('/v1/categories')
def get_all_categories():
    try:
        return jsonify({
            'data': categories.get_all_categories()
        }), 200
    except Exception as e:
        return jsonify({
            'message': 'Not able to fetch all categories data.'
        }), 400


@app.route('/v1/categories/<int:id>')
def get_category_by_id(id):
    try:
        return jsonify({
            'data': categories.get_category_by_id(id)
        }), 200
    except Exception as e:
        return jsonify({
            'message': 'Not able to fetch category data with specified id.'
        }), 400
