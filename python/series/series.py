def slices(series, length):
    if length > len(series) or length < 1:
        raise ValueError("Wrong arguments provided")

    return [series[i:i + length] for i in range(0, len(series), 1) if i + length <= len(series)]
