import os
from data_processor import get_sample_data
from predictor import predict_next_values
from utils import save_predictions, setup_logger

# Set up logging
logger = setup_logger()

def main(input_folder, output_folder, files_per_exchange):
    try:
        os.makedirs(output_folder, exist_ok=True)

        # Process each stock exchange folder
        for exchange in os.listdir(input_folder):
            exchange_path = os.path.join(input_folder, exchange)
            if not os.path.isdir(exchange_path):
                continue

            files = [f for f in os.listdir(exchange_path) if f.endswith(".csv")]
            files_to_process = files[:files_per_exchange]

            if not files_to_process:
                logger.warning(f"No files found for exchange: {exchange}")
                continue

            for file in files_to_process:
                file_path = os.path.join(exchange_path, file)
                try:
                    sample_data = get_sample_data(file_path)
                    predictions = predict_next_values(sample_data)
                    save_predictions(file, predictions, output_folder)
                    logger.info(f"Processed {file} for exchange: {exchange}")
                except Exception as e:
                    logger.error(f"Error processing {file}: {e}")

    except Exception as e:
        logger.critical(f"Application error: {e}")

if __name__ == "__main__":
    main(input_folder="sample_data", output_folder="output", files_per_exchange=2)