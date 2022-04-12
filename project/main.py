#!/usr/bin/env pybricks-micropython
from pybricks import robotics
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor, TouchSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
import sys
import __init__

ev3 = EV3Brick()
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
crane_motor = Motor(Port.A)
robot = DriveBase(left_motor, right_motor, wheel_diameter= 56,axle_track= 118)
Light_sensor = ColorSensor(Port.S3)
ultrasonic  = UltrasonicSensor(Port.S4)
touch_sensor = TouchSensor(Port.S1)


def main():
    return 0

if __name__ == '__main__':
    sys.exit(main())
