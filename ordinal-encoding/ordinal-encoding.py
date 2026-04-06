from collections import defaultdict

def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    Ordering preserves meaning : it is data reduction BUT
    some info kept ( natural rank ) 
    """
    orderMap = defaultdict(int)
    for idx,val in enumerate(ordering):
        orderMap[val] = idx
    encoding = [orderMap[val] for val in values]
    return encoding
        
