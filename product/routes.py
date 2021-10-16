from product import app
from product import request
from Models.Item import Item
from product import json

@app.route('/product-info',methods=['POST'])
def index():
    data = json.loads(request.data)
    product_info = Item(data["id"])
    response = app.response_class(
        response=product_info.get(),
        status=200,
        mimetype='application/json'
    )
    return response