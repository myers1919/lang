import json
import pandas as pd
import random

class Data:
    def __init__(self):
        self.dataset = self.get_data()
        print(self.dataset)

    def get_data(self):
        with open('data/vocab.json') as f:
            data = json.load(f)
        data = pd.DataFrame(data)
        data = data.transpose()
        return data
    
    def get_item(self):
        rng = random.randint(0, len(self.dataset))
        print(rng)
