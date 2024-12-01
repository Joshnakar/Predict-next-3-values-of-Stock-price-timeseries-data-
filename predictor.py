import pandas as pd

def predict_next_values(data):
    """
    Predict the next 3 stock price values.
    :param data: List of stock prices (10 values).
    :return: List of predicted stock prices.
    """
    if len(data) != 10:
        raise ValueError("Input data must contain exactly 10 data points.")

    n = data[-1]
    n_plus_1 = sorted(data)[-2]  # 2nd highest value
    n_plus_2 = n + (n_plus_1 - n) / 2
    n_plus_3 = n_plus_2 + (n_plus_1 - n_plus_2) / 4

    return [n_plus_1, n_plus_2, n_plus_3]
