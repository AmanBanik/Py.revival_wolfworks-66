class TwoDvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The vector is: ({self.i}i + {self.j}j)")

class ThreeDvector(TwoDvector):# inheritance
    def __init__(self, i, j, k):
        super().__init__(i, j)# prev class ke fun se fetch karega
        self.k = k

    def show(self):
        print(f"The vector is: ({self.i}i + {self.j}j + {self.k}k)")

a= TwoDvector(2, 3)

a.show()

b = ThreeDvector(2, 3, 4)

b.show()  