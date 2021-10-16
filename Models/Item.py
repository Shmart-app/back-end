from product import json
class Item:
    # initilier
    def __init__(self,id):
        self.id = id
        self.extract_data_from_db()
    # Methods
    def extract_data_from_db(self):
        file_reader = open("./database.json",)
        database = json.load(file_reader)
        for entry in database:
            if self.id == entry["id"]:
                self.name = entry["name"]
                self.company = entry["company"]
                self.price = entry["price"]
                self.ratings = entry["ratings"]
        file_reader.close()
    def get(self):
        data = {}
        data["id"] = self.id
        data["name"] = self.name
        data["company"] = self.company
        data["price"] = self.price
        data["ratings"] = self.ratings
        print(data)
        return json.dumps(data)



