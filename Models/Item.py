from main import json

class Item:
    # initilier
    def __init__(self,id):
        self.id = id
        self.name = None
        self.extract_data_from_db()

    # Methods
    def extract_data_from_db(self):
        file_reader = open("./database.json",)
        database = json.load(file_reader)
        for entry in database:
            if self.id == entry["article_number"]:
                self.name = entry["product_name"]
                self.company = entry["brand_code"]
                # self.price = entry["price"]
                # store this information somewhere
                # self.ratings = entry["ratings"] 
                self.product_description = entry["product_description"]
                # get the nutritional information
        file_reader.close()
    def get(self):
        data = {}
        if(self.name == None):
            print("Product Not Found")
            data["message"] = "Product Not Found"
            return json.dumps(data)
        data["id"] = self.id
        data["name"] = self.name
        data["company"] = self.company
        data["product_description"] = self.product_description
        # data["price"] = self.price
        # data["ratings"] = self.ratings
        print(data)
        return json.dumps(data)



