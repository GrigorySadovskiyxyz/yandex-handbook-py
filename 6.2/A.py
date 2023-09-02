import pandas as pd
import string


def length_stats(text): 
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    text = text.split()
    text.sort()
    d = {}
    for item in text:
        d[item] = len(item)
    d = pd.Series(d)
    return d
