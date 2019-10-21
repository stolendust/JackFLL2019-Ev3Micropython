#---------------------------------------------
# ev3 action library - movement, includeing:
# * going straight on exact distance 
# * turning accuratelly on exact degrees
# JackRobot Studio, 11/10/2019
#---------------------------------------------
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

