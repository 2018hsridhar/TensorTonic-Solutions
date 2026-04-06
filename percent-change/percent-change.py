def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    Needed in finance for stock returns
    Normalize series acros scales : stationarity!
    """
    percent_changes = []
    for idx in range(len(series) - 1):
        firstEl = series[idx]
        secondEl = series[idx+1]
        pct_i = 0
        if(firstEl != 0):
            pct_i = (secondEl - firstEl) / firstEl
        percent_changes.append(pct_i)
    return percent_changes
