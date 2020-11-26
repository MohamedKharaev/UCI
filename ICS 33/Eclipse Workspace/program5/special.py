# acts the same as a regular ball however every time it
# touches another Prey, it speeds up. 

from ball import Ball
from prey import Prey
import model

class Special(Ball):
    def __init__(self, x, y):
        Ball.__init__(self, x, y)
        
    def update(self):
        Ball.update(self)
        for x in model.placed_objects:
            if self.contains(x.get_location()) and x is not self and isinstance(x, Prey):
                self._speed += 1
        
    def display(self,canvas):
        canvas.create_oval(self._x-Ball.radius,      self._y-Ball.radius,
                                self._x+Ball.radius, self._y+Ball.radius,
                                fill='yellow')
