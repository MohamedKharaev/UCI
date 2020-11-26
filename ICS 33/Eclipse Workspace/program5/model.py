import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special
import tkinter
import simulton


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running        = False
cycle_count    = 0
placed_objects = set()
current_object = ''
#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, placed_objects, current_object
    running        = False
    cycle_count    = 0
    placed_objects = set()
    current_object = ''
    
#start running the simulation
def start ():
    global running
    running = True

#stop running the simulation (freezing it)
def stop ():
    global running
    running = False

#step just one update in the simulation
def step ():
    global running
    if running:
        update_all()
        running = False
    else:
        running = True
        update_all()
        running = False


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global current_object
    current_object = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if current_object == '':
        pass
    elif current_object == 'Remove':
        for s in list(placed_objects):
            if s.contains((x, y)):
                model.remove(s)
    else:
        placed_objects.add(eval(current_object + '({},{})'.format(x, y)))


#add simulton s to the simulation
def add(s):
    placed_objects.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    placed_objects.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    return set(filter(lambda x: p(x), placed_objects))


#call update for every simulton in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        for o in list(placed_objects):
            o.update()


#delete from the canvas each simulton in the simulation; then call display for each
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    controller.the_canvas.delete(tkinter.ALL)
    for o in placed_objects:
        o.display(controller.the_canvas)
    controller.the_progress.config(text=str(len(placed_objects))+" simultons/"+str(cycle_count)+" cycles")