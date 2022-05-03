#!/usr/bin/env pybricks-micropython
from pybricks import robotics
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor, TouchSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.messaging import BluetoothMailboxServer, TextMailbox

from pybricks import ev3brick as brick
from pybricks.parameters import Button, Color

import sys
import threading as th
import time
import __init__

ev3 = EV3Brick()
motor_left = Motor(Port.C, positive_direction = Direction.COUNTERCLOCKWISE, gears = [12, 20])
motor_right = Motor(Port.B, positive_direction = Direction.COUNTERCLOCKWISE, gears = [12, 20])
crane_motor = Motor(Port.A)
robot = DriveBase(motor_left, motor_right, wheel_diameter= 47,axle_track= 128)
color_sensor = ColorSensor(Port.S3)
ultrasonic_sensor  = UltrasonicSensor(Port.S4)
touch_sensor = TouchSensor(Port.S1)

is_holding = False

mod = 1 

light = 90
dark = 60
avg_reflection = (light + dark) / 2
speed = 300

color_to_fetch = Color.RED 

#change color hsv value after measurement and reflectionColor.BLUE = ()
#Color.GREEN = ()
#Color.YELLOW = ()
#Color.RED = ()
#Color.WHITE = ()
#Color.BROWN = ()
no_color = (0,0,0,0)
#from left to right, (clear), (black), (Blue), (Green), (Yellow), (Red), (White), (Brown)
color_reflection = [(0, 0),(1, 0), (2, 0), (3, 3), (4, 39), (5, 39), (6, 100), (7, 5)]


detectable_colors = (Color.BLACK, Color.BLUE, Color.GREEN, Color.YELLOW, Color.RED, Color.WHITE, Color.BROWN)

current_color_reflection = 0
color_background_reflection = 9

timer_area = 0

def Left_area(curent_color):
    global timer_area
    if color_sensor.color() == 'Color.RED':#Temp color
        timer_area=0
    else:
        timer_area+=1
    if timer_area >= 200:
        thread_text(40, 50, "Robot has left the area", 2)
    print(timer_area)

# def left_area(areaColor):
#     if ColorSensor == areaColor:
#         print('Robot has left sprcific area')

def returnToSpecArea(areaColor):
    groundColor = color_sensor.color()
    turnSpeed = 90
    
    # Kör runt i en cirkel som blir större tills färgsensorn hittar rätt färg
    while groundColor != areaColor:
        robot.drive(50, turnSpeed)
        turnSpeed -= 1
        groundColor = color_sensor.color()
    return "Tillbaka!"

def ExitSpecArea(areaColor):
    groundColor = color_sensor.color()
    turnSpeed = 90

    # Kör runt i en cirkel som blir större tills färgsensorn hittar en ny färg
    while groundColor == areaColor:
        robot.drive(50, turnSpeed)
        turnSpeed -= 0.1
        groundColor = color_sensor.color()
    return "Ute!"

def pickup_pallet():
    global is_holding
    #Här måste den först identifiera att den kan plocka upp, vänta på specifikationer

    # Checkar så att den inte redan har lyft upp objektet och ifall objektet är på "gaffeln"
    if not is_holding and touch_sensor.pressed():
        #sätter graderna på 0 för att förenkla mätandet sedan

        #Lyfter tills kranen har lyft objektet 45 grader upp eller 
        #tills den tappar objektet
        while crane_motor.angle() > -360 and touch_sensor.pressed():
            
            crane_motor.run_angle(200, 500, Stop.COAST, False)
        crane_motor.run(0)
        
        #Om den fortfarande håller objektet registreras det
        if touch_sensor.pressed():
            is_holding = True
            #Om den tappade objektet går den ned igen
        else:
            while crane_motor.angle() <= 1:
                crane_motor.run_angle(200, 500, Stop.COAST, False)
            crane_motor.run(0)
    #Ser till så att den håller uppe lasten när den väl har plockat upp 

def liftdown_pallet():
    if is_holding and touch_sensor.pressed():

        return
    return

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
        thread_text(40,50,'Decreasing speed1', 1)
        return 0.8
        
    elif ultrasonic_sensor.distance() < 150 and ultrasonic_sensor.distance() > 120:
        thread_text(40,50,'Decreasing speed2', 1)
        return 0.6 

    elif ultrasonic_sensor.distance() < 120 and ultrasonic_sensor.distance() > 100:
        thread_text(40,50,'Decreasing speed3', 1)
        return 0.4

    elif ultrasonic_sensor.distance() < 100 and ultrasonic_sensor.distance() > 70:
        thread_text(40,50,'Decreasing speed4', 1)
        return 0.2

    elif ultrasonic_sensor.distance() < 70:
        thread_text(40,50,'Full stop!', 1)
        return 0.0
        
    else:
        return 1

def color_change(color):
    color_to_fetch = color

def color_button_change():
    """ Color fetcher/changer with the help of the buttons. """
    button = brick.buttons()

    if Button.LEFT in button:
        color_change(Color.RED)
        thread_text(40, 50, "Fetching Blue Item", 2)
    elif Button.RIGHT in button: 
        color_change(Color.BLUE)
        thread_text(40, 50, "Fetching Blue Item", 2)

def thread_text(x_position = 40, y_position = 50, text = "", seconds_on_screen = 0.5):
    """Threaded operation that print a text to the middle of the screen. It does not interupt any other functions."""

    th.Thread(target=print_text_to_screen, args=(x_position, y_position, text, seconds_on_screen)).start()

def print_text_to_screen(x_position, y_position, text, seconds_on_screen):
    """Printing text to screen while stopping any on going operation until it has removed the text from the screen"""

    ev3.screen.draw_text(x_position, y_position, text)
    time.sleep(seconds_on_screen)
    ev3.screen.clear()

def drive():
    speed_modifier = collisionavoidence()
    
    correction = (avg_reflection - color_sensor.reflection()) * 1.65 # Öka för att svänga mer

    if correction >= 6 or correction <=-4: # 6(a) är hur långt in på linjen och -4(b) är när den svänger in mot linjen
        speed_modifier *= 0.2
        if correction <=-4:# #Ska vara överäns med if-satsen (b)
            mod=correction*(-2)#Öka om skarpare ytterkurver
        else:
            mod = correction*3.5#Öka om skarpare innerkurvor
        modifier=0.55-(mod/1000) # öka första variablenför att minska föränding av hastighet
        
        speed_modifier -= modifier

    if speed_modifier < 0:
        mod_speed = speed * (speed_modifier*(-1))
    else:
        mod_speed = speed * (speed_modifier)
    mod_speed = speed * -speed_modifier

    robot.drive(mod_speed , correction)

def detect_colorline():
    color_sensor.color()

    new_linereflection = color_reflection[color_sensor.color()]

    return (new_linereflection + light) / 2

def main(): 
    #color_button_change()
    pickup_pallet()
    #while True:
    #    Left_area('hej')
    #    
    #    drive()

if __name__ == '__main__':
    sys.exit(main())
