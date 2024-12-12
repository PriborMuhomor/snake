class CalculatorVektor:
    def __init__(self):
        self.v1 = list(input("введите первое значение: ").split(","))
        self.v2 = list(input("введите второе значение: ").split(","))



    def vector_add(self):
        return [int(self.v1[i]) + int(self.v2[i]) for i in range(len(self.v1))]

    def scalar_product(self):
        return sum(int(self.v1[i]) * int(self.v2[i]) for i in range(len(self.v1)))

    def vector_length(self):
        return sum(x ** 2 for x in self.v) ** 0.5
calculator = CalculatorVektor()
print(calculator.scalar_product())
