#!/usr/bin/env pybricks-micropython
from pybricks import robotics
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor, TouchSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
import sys
import __init__

motor_left = Motor(Port.C)
motor_right = Motor(Port.B)

###Jeff
ultrasonic = UltrasonicSensor(Port.S4)


def motors_perform(action, speed_modifier):     # Temp want input...
    if action == "hold":
        motor_right.hold()
        motor_left.hold()
    elif action == "forward":
        motor_right.run(360 * speed_modifier)
        motor_left.run(360 * speed_modifier)
    elif action == "left":
        motor_right.run(180 * speed_modifier)
        motor_left.run(-180 * speed_modifier)
    elif action == "right":
        motor_right.run(-180 * speed_modifier)
        motor_left.run(180 * speed_modifier) 

#

def colisionavoidenc():
    if ultrasonic.distance() < 200 and ultrasonic.distance() > 150:
        motors_perform("forward", 0.4)
        print('Decreasing speed1')
    elif ultrasonic.distance() < 150 and ultrasonic.distance() > 120:
        motors_perform("forward", 0.3)
        print('Decreasing speed2')
    elif ultrasonic.distance() < 120 and ultrasonic.distance() > 100:
        motors_perform("forward", 0.2)
        print('Decreasing speed3')
    elif ultrasonic.distance() < 100 and ultrasonic.distance() > 70:
        motors_perform("forward", 0.1)
        print('Decreasing speed4')
    elif ultrasonic.distance() < 70:
        motors_perform("hold", 0)
        print('Full stop')    
    else:
        motors_perform("forward", 0.5)

###

def main():
    return 0

if __name__ == '__main__':
    sys.exit(main())
