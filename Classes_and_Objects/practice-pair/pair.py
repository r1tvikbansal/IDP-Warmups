# Write your solution here!

class Pair:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        
    def __getitem__(self, i):
        if i == 0:
            return self._x
        elif i == 1:
            return self._y
        else:
            print('Error: Invalid Index!')
    
    def __setitem__(self, i, v):
        print('Error: Pair is immutable!')
        
    def __eq__(self, obj):
        return (self._x == obj._x) and (self._y == obj._y)
    
    def __repr__(self):
       return f'({self._x}, {self._y})'