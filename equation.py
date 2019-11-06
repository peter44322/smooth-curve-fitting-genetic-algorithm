class Equation:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def substituteX(self, x):
        # print(self.coefficients)
        y = 0.0
        for i in range(len(self.coefficients)):
            y += self.coefficients[i] * (x ** i)
        return round(y, 6)
