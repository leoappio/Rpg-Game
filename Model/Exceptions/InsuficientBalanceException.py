class InsuficientBalanceException(Exception):
    def __init__(self):
        super().__init__("Insuficient Balance!")
