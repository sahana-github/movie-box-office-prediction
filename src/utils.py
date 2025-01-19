# You can add any logging or helper functions here for your project

import logging

def setup_logger():
    logger = logging.getLogger('MovieBoxOffice')
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
