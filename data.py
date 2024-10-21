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
    
    def get_items(self):
        df = self.dataset.copy()
        set_size = 5
        item_ids = [] # Empty list for collecting selected item IDs
        for item in range(set_size):
            rng = random.randint(0, len(self.dataset)-1)
            print(rng)
            row = df.iloc[rng]# Get associated row from df
            print(row)
