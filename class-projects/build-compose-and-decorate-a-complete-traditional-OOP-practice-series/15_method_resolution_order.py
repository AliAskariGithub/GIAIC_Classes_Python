class A:
    def show(self):
        return "Class A"

class B(A):
    def show(self):
        return "Class B"

class C(A):
    def show(self):
        return "Class C"

class D(B, C):
    pass

# Example usage
if __name__ == "__main__":
    d = D()
    print(d.show())
    print(D.__mro__)