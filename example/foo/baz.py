class Baz:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def foo(self, c: int):
        return self.a + self.b + c
    