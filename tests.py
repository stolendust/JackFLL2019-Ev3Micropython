#---------------------------------------------
# unit test cases + tools of testing the robot
# JackRobot Studio, 11/10/2019
#---------------------------------------------
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase

import unittest

from libs.config import ROBOT 
from libs import log

class TestBasic(unittest.TestCase):
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

class TestRobot(unittest.TestCase):
    def setUp(self):
        # log basic envionment information
        log.log_robot_config()
        log.log_robot_info()

    # max speed is up to many conditions, floor, load, size of wheels, battery, etc. 
    # so maxt speed has to been got through testing, this it is
    def test_max_speed(self):
        log.info('--- test_max_speed ---')
        SPEED_STEP, MIN_TEST_TIME, CHECK_INTERVAL = 50, 16000, 250
        max_speed, speed_left= 0, SPEED_STEP
        motor_right, motor_left = Motor(ROBOT['drive_motor_port_left']), Motor(ROBOT['drive_motor_port_right'])
        motor_left.reset_angle(0)
        motor_right.reset_angle(0)

        robot = DriveBase(motor_left, motor_right, ROBOT['wheel_diameter'], ROBOT['wheel_axle_track'])

        watch = StopWatch()
        robot.drive(speed_left, 0)
        angle_left, angle_right = 0,0

        while True:
            run_time = watch.time()
            old_speed = speed_left
            speed_left = motor_left.speed()

            # timeout 
            if run_time >= MIN_TEST_TIME:
                log.info('reach max test time, speed_left=%d, max_speed=%d' % (speed_left, max_speed))
                break

            # found higher speed reached
            if speed_left > max_speed:
                print('motor angle: left=%d, right=%d' % (motor_left.angle(), motor_right.angle()))
                print('motor speed: left=%d, right=%d' % (motor_left.speed(), motor_right.speed()))

                # stop and run more time with higher speed
                robot.stop()
                watch.reset()

                motor_left.reset_angle(0)
                motor_right.reset_angle(0)
                angle_left, angle_right = 0,0

                max_speed = speed_left
                speed_left += SPEED_STEP 
            
                print('drive one more time, speed_left=%d, max_speed=%d' % (speed_left, max_speed ))
                robot.drive(speed_left, 0)
                continue

            # continue
            a_l = motor_left.angle()
            a_r = motor_right.angle()
            angle_left += a_l 
            angle_right += a_r
            #print('angle/total angle:    %d/%d - %d/%d' % (a_l, angle_left, a_r, angle_right))
            steering = (abs(angle_left-angle_right) // 10) * 10  
            if steering > 30:
                steering = 30
            if angle_left > angle_right:
                steering = 0 - steering
            if abs(angle_left - angle_right) > 10:
                print('delta/total/steering: %3d/%3d/%3d' % (a_l - a_r,angle_left-angle_right, steering))
                motor_left.reset_angle(0)
                motor_right.reset_angle(0)
                robot.drive((motor_left.speed() + motor_right.speed()) / 2, steering)
            else:
                print('.')

            wait(CHECK_INTERVAL) # wait one second to let motor reach higher speed

        print('motor speed: left=%d, right=%d' % (motor_left.speed(), motor_right.speed()))
        print('total motor angle: left=%d, right=%d' % (angle_left, angle_right))
        log.info('test_max_speed: battery=%d, max_speed=%d' % (brick.battery.voltage(), max_speed))
        robot.stop()

if __name__ == '__main__':
    unittest.main()

