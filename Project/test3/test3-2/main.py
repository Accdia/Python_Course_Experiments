import sys

def DECO(*args):
    def deco(func):
        def callfunc(*args):
            if not all(isinstance(item, float) for item in [*args]):
                return "error"
            return func(*args)
        return callfunc
    return deco
@DECO(3.0,4.0)
def triangular(S,h):
    return S*h/3
@DECO(1.0)
def sphere(R):
    return 3.14*R*R*R*4/3
@DECO(1.0,2.0)
def quadrangular(S,h):
    return S*h
print(triangular('w',4.0))
print(triangular(2.0,3.0))
print(sphere(1.0))
print(quadrangular(1.0,2.0))