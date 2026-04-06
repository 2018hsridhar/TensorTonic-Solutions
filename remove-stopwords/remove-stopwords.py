def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    removed_list = []
    stop = set(stopwords)
    for token in tokens:
        if(token not in stop):
            removed_list.append(token)
    return removed_list
