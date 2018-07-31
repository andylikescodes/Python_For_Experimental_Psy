from pygaze.display import Display
import pygaze.libtime as timer
from pygaze.screen import Screen
from constants import *

fixscreen = Screen()
fixscreen.draw_fixation(fixtype='dot')

disp = Display()
timer.pause(2000)
disp.close()