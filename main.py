#!/usr/bin/env pybricks-micropython

#-------------------------------
# main entry  
# JackRobot Studio, 11/10/2019
#-------------------------------

from time import perf_counter

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from libs import config
from libs import log


def main():
    # sound test
    log.info('test beep')
    brick.sound.beep()

    # moter test
    log.info('test large moter')
    lmoter = Motor(Port.A)
    lmoter.run_time(300, 3000)
    lmoter.run_time(-100, 2000)

if __name__ == '__main__':
    startTime = perf_counter()
    log.debug('>>> brickrun - main')
    main()
    usedTime = perf_counter() - startTime
    log.info("TOTAL TIME USED: %ds" % usedTime)
    log.debug("<<< brickrun - main")