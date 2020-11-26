# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
import random

#img = PhotoImage(file='ufo.gif')

class Floater(Prey):
    def __init__(self, x, y):
        Prey.__init__(self, x, y, 10, 10, 0, 5)
        self.randomize_angle()
        
    def update(self):
        if random.random() < .3:
            if self._speed < 3.5:
                self._speed = random.uniform(3, self._speed + .5)
            elif self._speed > 6.5:
                self._speed = random.uniform(self._speed - .5, 7)
            else:
                self._speed = random.uniform(self._speed - 5, self._speed + 5)
            self._angle += random.uniform(-.5, .5)
        self.move()
        self.wall_bounce()
        
    def display(self, canvas):
        canvas.create_oval(self._x-5,      self._y-5,
                                self._x+5, self._y+5,
                                fill='red')
        #canvas.create_image(self._x, self._y, image = img)
    