# src/exceptions.py

class MissingDataException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ModelTrainingException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
