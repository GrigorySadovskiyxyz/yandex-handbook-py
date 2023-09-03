import pandas as pd
import string


def length_stats(text): 
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    text = text.split()
    text.sort()
    odd, even = {}
    for item in text:
        if len(item) % 2 == 1: 
            odd[item] = len(item)
        else:
            even[item] = len(item)
    odd = pd.Series(odd)
    even = pd.Series(even)
    return odd, even
