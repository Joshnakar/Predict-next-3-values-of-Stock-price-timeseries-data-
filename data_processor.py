import pandas as pd
import random

def get_sample_data(file_path):
    """
    Fetch 10 consecutive data points starting from a random timestamp.
    :param file_path: Path to the stock CSV file.
    :return: List of 10 stock prices.
    """
    data = pd.read_csv(file_path)
    if data.empty:
        raise ValueError("File is empty.")

    if len(data) < 10:
        raise ValueError("File has less than 10 data points.")

    start_index = random.randint(0, len(data) - 10)
    sample = data.iloc[start_index:start_index + 10]
    return sample["stock price"].tolist()
