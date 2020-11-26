# A Black_Hole is derived from only a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model
import math


class Black_Hole(Simulton):
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, 20, 20)
    
    def update(self):
        inside = model.find(lambda x: self.contains(x.get_location()) and isinstance(x, Prey))
        for i in inside:
            model.remove(i)
        return inside
    
    def display(self, canvas):
        canvas.create_oval(self._x-(self._width / 2),      self._y-(self._height / 2),
                                self._x+(self._width / 2), self._y+(self._height / 2),
                                fill='black')
    
    def contains(self, xy):
        return math.sqrt((self._x - xy[0])**2 + (self._y - xy[1])**2) < self._height / 2
    
    
