from main import app
from main import request
from Models.Item import Item
from main import json
from nutrition_api.routes import send_request
from customer_rating_api.routes import get_rating
@app.route('/product-info',methods=['POST'])
def index():
    try:
        data = json.loads(request.data)
        product_info = Item(data["id"])
        data_to_send = json.loads(product_info.get())
        
        # Get the nutrition data
        nutrition_data = json.loads(send_request(data_to_send["name"]).data)  
        data_to_send["nutrition"] = nutrition_data["foods"][0]  
        # print(nutrition_data["foods"][0])
        
        # Get the customer rating data
        customer_rating = json.loads(get_rating(data["id"]).data)
        data_to_send["rating"] = customer_rating["product_rating"]
        print(customer_rating)

        response = app.response_class(
            response= json.dumps(data_to_send),
            status=200,
            mimetype='application/json'
        )
        return response
    except:
        response = app.response_class(
            response=json.dumps({"message":"The server encountered an error with your request"}),
            status=403,
            mimetype='application/json'
        )
        return response