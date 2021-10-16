from main import app
from main import request
import requests
from Models.Item import Item
from main import json
import os
# @app.route('/nutrition-info',methods=['POST'])
def send_request(a):
    url="https://trackapi.nutritionix.com/v2/natural/nutrients"
    data={
        'query': a
    }
    headers_dict={
        'x-app-id':os.environ.get("X_APP_ID"),
        'x-app-key':os.environ.get("X_API_KEY"),
        'Content-Type':'application/json'
        }
    nut_resp = requests.post(url=url,headers=headers_dict,data=json.dumps(data))
    # data = json.loads(request.data)
    # product_info = Item(data["id"])
    # response = ""
    # if product_info.name == None:
    #     response = app.response_class(
    #     response=product_info.get(),
    #     status=404,
    #     mimetype='application/json'
    # )
    response = app.response_class(
        response=json.dumps(json.loads(nut_resp.text)),
        status=200,
        mimetype='application/json'
    )
    return response