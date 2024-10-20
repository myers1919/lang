import json

class ItemManager:
    def __init__(self):
        self.load_item_data()
        self.get_item()

    def load_item_data(self):
        filepath = "data/vocab.json"
        with open(filepath, 'r') as f:
            self.item_data = json.load(f)

    def get_item(self):
        print("THIS IS GETTING AN ITEM FROM")
        print(self.item_data)
