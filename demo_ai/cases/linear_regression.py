import json 

class LinearRegression():
 # y = m*x + c

    m: float
    c: float

    def __init__(self, m: float, c: float) -> None:
        self.m = m
        self.c = c

    def predict(self, x: int) -> float:
        return (self.m * x + self.c ) * 1000

    def training(self) -> bool:
        return True

    def load_model(self, filenamame: str = ""):
        with open(filenamame, 'r') as file:
            values = json.load(file)
            print(values)
            self.m = values['m']
            self.c = values['c']

