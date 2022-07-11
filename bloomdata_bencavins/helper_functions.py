import random
import pandas as pd


def random_phrase():
    adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
    nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return adjective + ' ' + noun

def random_float(min_val, max_val):
    return random.uniform(min_val, max_val)

def random_bowling_score():
    return random.randint(0, 300)

def silly_tuple():
    return (random_phrase(), random_float(1.0, 5.0), random_bowling_score())

df = pd.DataFrame({'a': [1, None], 'b': [None, 2]})

def null_count(df):
    return df.isnull().sum().sum()