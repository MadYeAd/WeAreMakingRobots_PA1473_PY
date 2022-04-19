#!/usr/bin/env pybricks-micropython
from asyncio.windows_events import NULL
from turtle import right
from pybricks import robotics
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor, TouchSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.messaging import BluetoothMailboxServer, TextMailbox

from pybricks import ev3brick as brick
from pybricks.parameters import Button, Color
from threading import Timer

import sys
import __init__


ev3 = EV3Brick()
motor_left = Motor(Port.C, positive_direction = Direction.COUNTERCLOCKWISE, gears = [12, 20])
motor_right = Motor(Port.B, positive_direction = Direction.COUNTERCLOCKWISE, gears = [12, 20])
crane_motor = Motor(Port.A)
robot = DriveBase(motor_left, motor_right, wheel_diameter= 47,axle_track= 128)
light_sensor = ColorSensor(Port.S3)
ultrasonic_sensor  = UltrasonicSensor(Port.S4)
touch_sensor = TouchSensor(Port.S1)

is_holding = False

light = 100
dark = 9
reflection = (light + dark) / 2
speed = 250

color_to_fetch = Color.RED 

light_red = 20
light_yellow = 20

def leftArea(areaColor):
    if ColorSensor == areaColor:
        print('Robot has left sprcific area')

def returnToSpecArea(areaColor):
    groundColor = light_sensor.color()
    turnSpeed = 90
    
    # Kör runt i en cirkel som blir större tills färgsensorn hittar rätt färg
    while groundColor != areaColor:
        robot.drive(50, turnSpeed)
        turnSpeed -= 1
        groundColor = light_sensor.color()
    return "Tillbaka!"

def ExitSpecArea(areaColor):
    groundColor = light_sensor.color()
    turnSpeed = 90

    # Kör runt i en cirkel som blir större tills färgsensorn hittar en ny färg
    while groundColor == areaColor:
        robot.drive(50, turnSpeed)
        turnSpeed -= 0.1
        groundColor = light_sensor.color()
    return "Ute!"

    ### SLUT DAVID ###

def pickup():
    global is_holding
    #Här måste den först identifiera att den kan plocka upp, vänta på specifikationer

    # Checkar så att den inte redan har lyft upp objektet och ifall objektet är på "gaffeln"
    if not is_holding and touch_sensor.pressed():
        #sätter graderna på 0 för att förenkla mätandet sedan

        #Lyfter tills kranen har lyft objektet 45 grader upp eller 
        #tills den tappar objektet
        while crane_motor.angle() > -90 and touch_sensor.pressed():
            
            crane_motor.run(-100)
        crane_motor.run(0)
        
        #Om den fortfarande håller objektet registreras det
        if touch_sensor.pressed():
            is_holding = True
            #Om den tappade objektet går den ned igen
        else:
            while crane_motor.angle() <= 1:
                crane_motor.run(100)
            crane_motor.run(0)

    #Ser till så att den håller uppe lasten när den väl har plockat upp 

def motors_perform(action, speed_modifier):
    if action == "hold":
        robot.drive(0,0)
    elif action == "forward":
        # motor_right.run(360 * speed_modifier)
        # motor_left.run(360 * speed_modifier)
        robot.drive(36 * speed_modifier,0)
    elif action == "left":
        motor_right.run(180 * speed_modifier)
        motor_left.run(-180 * speed_modifier)
    elif action == "right":
        motor_right.run(-180 * speed_modifier)
        motor_left.run(180 * speed_modifier) 

def collisionavoidence():
    if ultrasonic_sensor.distance() < 200 and ultrasonic_sensor.distance() > 150:
        return 0.8
        #motors_perform("forward", 0.4)
        #print('Decreasing speed1')
    elif ultrasonic_sensor.distance() < 150 and ultrasonic_sensor.distance() > 120:
        return 0.6
        #motors_perform("forward", 0.3)
        #print('Decreasing speed2')
    elif ultrasonic_sensor.distance() < 120 and ultrasonic_sensor.distance() > 100:
        return 0.4
        #motors_perform("forward", 0.2)
        #print('Decreasing speed3')
    elif ultrasonic_sensor.distance() < 100 and ultrasonic_sensor.distance() > 70:
        return 0.2
        #motors_perform("forward", 0.1)
        #print('Decreasing speed4')
    elif ultrasonic_sensor.distance() < 70:
        return 0.0
        #motors_perform("hold", 0)
        print('Full stop')  
    else:
        return 1
        #motors_perform("forward", 0.5)

def color_change(color):
    color_to_fetch = color

def color_button_change():
    """ 
    Color fetcher/changer with the help of the buttons.
    """
    button = brick.buttons()

    if Button.LEFT in button:
        color_change(Color.RED)
        print_text_to_screen(40, 50, "Fetching Red Item")
    elif Button.RIGHT in button: 
        color_change(Color.BLUE)
        print_text_to_screen(40, 50, "Fetching Blue Item")

def print_text_to_screen(x_position, y_position, text, time_on_screen):
    """
    Print a text in the middle of the screen
    """
    ev3.screen.draw_text(x_position, y_position, text)
    
    clear_screen = Timer(time_on_screen, ev3.screen.draw_text(0,0,0))
    clear_screen()

def set_colorpanel(color_to_display, time_to_last = 0):
    """If time_to_last is set to 0, the light will stay on"""
    ev3.light.on(color_to_display)

    clear_light = Timer(time_to_last, ev3.light.off)

def main(): 
    # while crane_motor.angle() > -180:
    #     print(crane_motor.angle())
    #     crane_motor.run(-360)
    # crane_motor.run(0)
    
    # while crane_motor.angle() < 90:
    #     crane_motor.run(100)
    # crane_motor.run(0)

    while True:
        # drive_sensor.reflection() > 0: # om sensorn inte ser helt sv
        speed_modifier = collisionavoidence()
        mod_speed = speed * speed_modifier
        correction = (reflection - light_sensor.reflection()) * 2
        
        if correction >= 4 or correction <=-4:
            speed_modifier *= 0.5
            if correction <=-4:
                mod*=-1
            else:
                mod = correction
            modifier=0.5-(mod/100)
            
            speed_modifier *= modifier
        print(correction)

        robot.drive(mod_speed , -correction)
        
if __name__ == '__main__':
    sys.exit(main())
