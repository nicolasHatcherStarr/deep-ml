def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    res = []
    previous = None
    for i in samples:
        if i == previous:
            res.pop()
            occourance += 1
        else: 
            occourance = 1
        res.append((i , (occourance/len(samples))))
        previous = i
    return res