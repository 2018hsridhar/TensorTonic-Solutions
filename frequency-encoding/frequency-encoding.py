import numpy as np
from collections import defaultdict


def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    Categories -> make into frequency datae
    """
    freqMap = defaultdict(int)
    propMap = defaultdict(int)
    for val in values:
        freqMap[val] += 1
    total_num_values = len(values)
    for k, v in freqMap.items():
        propMap[k] = (v/total_num_values)
    freq_encode = []
    print(propMap)
    freq_encode = [propMap[val] for val in values]
    # return freq_encode
    return freq_encode
        
        
    
