class length:
    def __init__(self, n):
        self.n = n

    def __add__(self, x):
        return self.n + x

    def __sub__(self, x):
        if x==str:
            raise TypeError
        if self.n > x:
            return self.n - x
        else:
            return x - self.n

    def __mul__(self, x):
         if not isinstance(x, int):
            raise TypeError
         else:
            return self.n * x


l = length(8.90)
print(l.__add__(3))
print(l.__sub__(9))
print(l.__sub__(8))
print(l.__mul__(2))
