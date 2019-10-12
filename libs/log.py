#-------------------------------
# logging into file and stderr
# JackRobot Studio, 11/10/2019
#-------------------------------
import sys
import time
import logging

from pybricks.parameters import (Port, Stop, Direction, Button, Color, Align)
from pybricks import ev3brick as brick
from .config import LOG, ROBOT, WATCH_DOG

def __log(message, level):
    # format the time stamp with millisecond
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y%m%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)

    # write into log file
    message_formated = '%s/%s: %s' % (time_stamp, logging._level_dict.get(level), message)
    with open(LOG['file'], "a") as f:
        f.write(message_formated + "\n")

    # print
    print(message_formated, file=sys.stderr)

def info(message):
    if(LOG['level'] > logging.INFO):
        return
    __log(message, logging.INFO)

# log error message and warn with beeps
def error(message):
    if(LOG['level'] > logging.ERROR):
        return
    __log(message, logging.ERROR)
    brick.sound.beeps(WATCH_DOG['warning_beep_times'] + 1) 

def debug(message):
    if(LOG['level'] > logging.DEBUG):
        return
    __log(message, logging.DEBUG)

# log warn message and warn with beeps
def warning(message):
    if(LOG['level'] > logging.WARNING):
        return
    __log(message, logging.WARNING)
    brick.sound.beeps(WATCH_DOG['warning_beep_times']) 


# log robot configuration in a clear way
def log_robot_config():
    message_list = ['--- ROBOT CONFIG ---']

    # log constant value of ev3 micropython for better understanding
    message_list.append('---Ports: S1(%d)-S4(%d) / A(%d)-D(%d)' % (Port.S1, Port.S4,Port.A, Port.D))

    # sort keys in robot configuration and format keys and values
    for key in sorted(ROBOT.keys()):
        value = ROBOT[key]
        message_list.append('---%s: %s' % (key, value))
    
    debug('\n'.join(message_list))

def log_robot_info():
    message_list = ['--- ROBOT INFO ---']
    # log constant value of ev3 micropython for better understanding
    message_list.append('---battary voltage=%dmV, current=%d' % (brick.battery.voltage(), brick.battery.current()))

    # check battery and beep 3 times when voltage belows 2000mV
    if(brick.battery.voltage() < WATCH_DOG['min_battery_voltage']):
        warning('low voltage of robot battery: %d' % brick.battery.voltage())

    debug('\n'.join(message_list))
    
