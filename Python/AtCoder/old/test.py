class MyClass:
    def __init__(self, arr):
        self.arr = arr
        self.child_class = MyClass2(self, arr)

    def getsum(self):
        return sum(self.arr)


class MyClass2:
    def __init__(self, par, arr):
        arr = [a+1 for a in arr]
        self.parent_class = par
        self.arr = arr

    def getsum(self):
        return sum(self.arr)

    def get_parent_sum(self):
        return self.parent_class.getsum()


myobj = MyClass([1, 2, 3])
print(myobj.getsum())
print(myobj.child_class.getsum())
print(myobj.child_class.get_parent_sum())
