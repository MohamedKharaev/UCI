# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole
from prey import Prey
import model


class Pulsator(Black_Hole):
    shrink_timer = 30
    
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self._pulse_count = 0
        
    def update(self):
        self._pulse_count += 1
        inside = model.find(lambda x: self.contains(x.get_location()) and isinstance(x, Prey))
        for i in inside:
            model.remove(i)
        if len(inside) > 0:
            self._width += len(inside)
            self._height += len(inside)
            self._pulse_count = 0
        if self._pulse_count == Pulsator.shrink_timer:
            self._height -= 1
            self._width -= 1
            self._pulse_count = 0
        if self._width == 0:
            model.remove(self)
        