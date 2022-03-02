class InvalidParameterException(Exception):
    def __init__(self,parameter_name, method_name, class_name):
        super().__init__("The parameter ",parameter_name," in method ", method_name," in class ",class_name," is invalid!")
