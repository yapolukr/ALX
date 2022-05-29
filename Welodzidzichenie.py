class A:

    def __init__(self, x):
        print("A")


class B:

    def __init__(self, x):
        print("B")


class C(A,B):

    def __init__(self, x):
        B.__init__(self, x)
        A.__init__(self, x)

ob = C(111)