# Stock Price Predictor

## Overview
A Python-based application to predict the next 3 stock prices for CSV data.

## Setup
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt


Build and run the Docker container:

bash
Copy code
docker build -t stock-predictor .
docker run -v $(pwd)/output:/app/output stock-predictor
