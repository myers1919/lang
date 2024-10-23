import json
import os
import pandas as pd
import random

class Data:
    def __init__(self):
        self.dataset = self.get_data()
        self.stats = self.get_stats()
        self.item_set = None
        self.current_item = None

    def get_data(self):
        with open('data/vocab.json') as f:
            data = json.load(f)
        data = pd.DataFrame(data)
        data = data.transpose()
        data = data.reset_index().rename(columns={'index':'id'})
        return data
    
    def get_stats(self):
        df = self.dataset.copy()
        df['n_seen'] = int(0)
        df['n_correct'] = int(0)
        df['n_incorrect'] = int(0)
        df['%_correct'] = float(0)
        filepath = 'data/stats.csv'
        if not os.path.exists(filepath):
            print("Stats file did not exist. Creating it now.")
            df.to_csv(filepath, index=False, encoding="utf-8")
        return df
        
    
    def get_items(self):
        df = self.dataset.copy()
        set_size = 10
        item_set = [] # Empty list for collecting selected item IDs
        for i in range(set_size):
            rng = random.randint(0, len(self.dataset)-1)
            row = df.iloc[rng] # Get associated row from df
            item_set.append(row)
            print(f"Item {i+1}: {item_set[i].deutsch}")
        self.item_set = item_set

    def get_current_item(self):
        if len(self.item_set) > 0:
            self.current_item = self.item_set[0]

    def parse_current_item(self):
        self.id = self.current_item.id
        self.question = self.current_item.deutsch
        self.answer = self.current_item.englisch
        print(f"Current question: {self.question}")
        print(f"Current answer: {self.answer}")

    def get_current_alternatives(self):
        import Levenshtein
        df = self.dataset.copy()
        df['L'] = self.dataset['englisch'].apply(lambda x: Levenshtein.distance(x, self.answer))
        df = df.sort_values(by=['L'], ascending=True)
        self.alternatives = df.englisch[1:4].tolist()
        print(f"Alternative answers are: {self.alternatives}")
