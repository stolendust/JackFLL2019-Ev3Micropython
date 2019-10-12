#----------------------------------------------------------
# config information for whole project
# just define global variants here, this is a tiny project
#----------------------------------------------------------
import sys
import logging
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)

# configuration of our built robot 
ROBOT = {
    'drive_motor_port_left' : Port.A,
    'drive_motor_port_right' : Port.D,
    'wheel_axle_track' : 111, # distance between the midpoint of two wheels
    'wheel_diameter' : 43.2,
    'sensor_gyro_port' : Port.S2,
    'sensor_color_port' : Port.S1
}

# logging configuration: log file, log level
LOG = {
    'file':'brickrun.log',
    'level': logging.DEBUG,
}

# warth the status of robot, warn in unhealth cases
WATCH_DOG = {
    'min_battery_voltage' : 2000,
    'warning_beep_times' : 2
}


#---------------------------------------
# initialize project
#---------------------------------------

