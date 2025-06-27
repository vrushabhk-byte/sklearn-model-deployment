def preprocess_input(data):
    # Basic preprocessing: assume input is a dict with numeric values
    return [float(v) for v in data.values()]
