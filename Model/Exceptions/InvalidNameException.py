class InvalidNameException(Exception):
    def __init__(self):
        super().__init__("Name must have at least 3 characters!")