#!/usr/bin/env pybricks-micropython

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
    log.info('test beep')
    brick.sound.beep()

    log.info('test large moter')
    lmoter = Motor(Port.A)
    lmoter.run_time(300, 3000)
    lmoter.run_time(-100, 2000)

if __name__ == '__main__':
    log.debug('>>> brickrun main()')
    main()
    log.debug('<<< brickrun main()')