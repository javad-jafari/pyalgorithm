"""
make a class like Foo :

* in first init f.x = 0
* if f.x < 0  return -1
* if f.x > 0 return last two digit of number


f = Foo()
print(f.x) = 0
f.x = -56
print(f.x) = -1

f.x = 356
print(f.x) = 56
"""


class Foo(object):

    def __init__(self):
        self.x = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if x < 0:
            self._x = -1
            return self._x
        if x > 0:
            self._x = int(str(x)[-2:])
            return self._x
        self._x = x
