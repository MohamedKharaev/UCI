# A Hunter is derived from both a Mobile_Simulton and a Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import model


class Hunter(Pulsator,Mobile_Simulton):
    hunt_radius = 200
    
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        self._speed = 5
        self.randomize_angle()
        
    def update(self):
        Pulsator.update(self)
        in_hunt_radius = model.find(lambda x: isinstance(x, Prey) and x.distance(self.get_location()) <= 200)
        if len(in_hunt_radius) > 0:
            closest = sorted(in_hunt_radius, key = lambda x: x.distance(self.get_location()))[0]
            self.set_angle(atan2(closest.get_location()[1] - self.get_location()[1], closest.get_location()[0] - self.get_location()[0]))
        self.move()
