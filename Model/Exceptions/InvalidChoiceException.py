class InvalidChoiceException(Exception):
    def __init__(self):
        super().__init__("Invalid Choice!")