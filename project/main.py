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
motor_left = Motor(Port.C)
motor_right = Motor(Port.B)
crane_motor = Motor(Port.A)
robot = DriveBase(motor_left, motor_right, wheel_diameter= 56,axle_track= 118)
Light_sensor = ColorSensor(Port.S3)
ultrasonic  = UltrasonicSensor(Port.S4)
touch_sensor = TouchSensor(Port.S1)

### Jeff ###
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

### stop ###

#Sebbes trashpile

def pickup():
    #Här måste den först identifiera att den kan plocka upp, vänta på specifikationer

    #Checkar så att den inte redan har lyft upp objektet och ifall objektet är på "gaffeln"
    if not isHolding and not touch_sensor.pressed():
        #sätter graderna på 0 för att förenkla mätandet sedan
        crane_motor.resetAngle(0)
        ev3.speaker.beep()
        #Lyfter tills kranen har lyft objektet 45 grader upp eller 
        #tills den tappar objektet
        while crane_motor.angle() < 45 and touch_sensor.pressed:
            crane_motor.run(10)

        #Om den fortfarande håller objektet registreras det
        if touch_sensor.pressed:
            isHolding = True
            #Om den tappade objektet går den ned igen
        else:
            while crane_motor.angle() > 5:
                crane_motor.run(-10)

    #Ser till så att den håller uppe lasten när den väl har plockat upp 

    if isHolding:
        crane_motor.brake()

def main():
    return 0

if __name__ == '__main__':
    sys.exit(main())
