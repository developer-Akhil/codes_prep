class Add(object):

    def result(self, x, y):
        print("Addition :", x + y)


class Multiply(Add):

    def result(self, a, b):
        super().result(30, 50)
        print("Multiplication :", a * b)


m = Multiply()

m.result(10, 20)
