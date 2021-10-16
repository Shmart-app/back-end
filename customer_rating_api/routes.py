from main import app
from main import request
import requests
from Models.Item import Item
from main import json
from main import sqlite3

# Expects a request body of type
# {id: "132131244", rating:4.3}

@app.route('/customer-in',methods=["POST"])
def send_rating():
    try:
        data = json.loads(request.data)
        product_id = data["id"]
        given_rating = data["rating"]
        given_rating = max(0,given_rating)
        given_rating = min(given_rating,5)
        conn = sqlite3.connect('sql/products.db')
        print("Opened database successfully")
        resultant_rating = given_rating
        # Check if the product id exists
        if conn.execute("SELECT EXISTS(SELECT * from product WHERE id=?)",(product_id,)).fetchall()[0][0] == 1:  
            updated_rating = conn.cursor()
            number_of_ratings = conn.cursor()
            updated_rating = updated_rating.execute("SELECT rating from product WHERE id=?",(product_id,)).fetchall()[0][0]
            number_of_ratings  = number_of_ratings.execute("SELECT number_of_ratings from product WHERE id=?",(product_id,)).fetchall()[0][0]     
            updated_rating = round((updated_rating*number_of_ratings + given_rating) / (number_of_ratings + 1),2)
            # update the entries
            print("UPDATED RATING:?",(updated_rating,))
            conn.execute('UPDATE product SET rating = ? WHERE id = ?',(updated_rating,product_id))
            conn.execute('UPDATE product SET number_of_ratings = ? WHERE id = ?',(number_of_ratings + 1,product_id))
            resultant_rating = updated_rating
        else:
            conn.execute("INSERT INTO product (id,rating,number_of_ratings) values (?,?,?)",(product_id,given_rating,1))

        updated_rating = conn.cursor()
        
        print("Updated successfully")
        conn.commit()
        conn.close()
        response = app.response_class(
            response=json.dumps({"updated_rating":resultant_rating}),
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

# Expects a request body of type
# {id: "132131244", rating:4.3}

# @app.route('/customer-in',methods=["GET"])
def get_rating(p_id):
    # data = json.loads(request.data)
    # product_id = data["id"]
    product_id = p_id
    rating = None
    conn = sqlite3.connect('sql/products.db')
    if conn.execute("SELECT EXISTS(SELECT * from product WHERE id=?)",(product_id,)).fetchall()[0][0] == 1:  
        rating = conn.cursor()
        rating = rating.execute("SELECT rating from product WHERE id=?",(product_id,)).fetchall()[0][0]
    conn.close()
    response = app.response_class(
            response=json.dumps({"product_rating":rating}),
            status=200,
            mimetype='application/json'
        )
    return response
