# src/logging.py

import logging

def setup_logging():
    logging.basicConfig(filename='movie_prediction.log', level=logging.INFO)
    return logging

# Example usage
logger = setup_logging()
logger.info('Logging setup complete.')

# Log other events (e.g., model training)
logger.info('Model training started.')
