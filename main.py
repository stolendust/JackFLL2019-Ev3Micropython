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

from libs.config import ROBOT 
from libs import log


def main():
    # sound test
    log.info('test beep')
    brick.sound.beep()

    # color sensor test
    sensor_color = ColorSensor(ROBOT['sensor_color_port'])
    log.debug('color sensor: color=%s' % sensor_color.color())

    # gyro sensor test
    sensor_gyro = GyroSensor(ROBOT['sensor_gyro_port'])
    log.debug('gyro sensor: speed=%d, angle=%d' % (sensor_gyro.speed(), sensor_gyro.angle()))

    # moter test
    rotation = 10 
    speed, angle = -1000, rotation * 360

    log.info('test going straight, speed=%d, angle=%d, rotation=%d' % (speed, angle, rotation))
    motor_right = Motor(ROBOT['drive_motor_port_left'])
    motor_left = Motor(ROBOT['drive_motor_port_right'])

    robot = DriveBase(motor_left, motor_right, ROBOT['wheel_diameter'], ROBOT['wheel_axle_track'])
    robot.drive(50, 0)
    wait(5000)
    robot.stop()  

if __name__ == '__main__':
    startTime = perf_counter()
    log.debug('>>> brickrun - main')

    # log basic envionment information 
    log.log_robot_config()
    log.log_robot_info()

    main()

    usedTime = perf_counter() - startTime
    log.info("--- TOTAL TIME USED: %ds ---" % usedTime)
    log.debug("<<< brickrun - main")