import csv
import logging
import os

def save_predictions(file_name, predictions, output_folder):
    """
    Save predictions to a CSV file.
    :param file_name: Original file name.
    :param predictions: Predicted values.
    :param output_folder: Path to save the output.
    """
    output_file = os.path.join(output_folder, f"predicted_{file_name}")
    with open(output_file, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock-ID", "Timestamp", "Stock Price"])
        for i, price in enumerate(predictions):
            writer.writerow([file_name.split('.')[0], f"Timestamp-{i+1}", price])

def setup_logger():
    """
    Set up a logger for the application.
    """
    logger = logging.getLogger("StockPredictor")
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
