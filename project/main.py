#!/usr/bin/env pybricks-micropython
from pybricks import robotics
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor, TouchSensor
from pybricks.parameters import Port, Stop, Direction, Button
from pybricks.parameters import Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
from pybricks import ev3brick as brick

import sys
import threading as th
import time
import __init__

""" Funktioner """
def main(): 
    """ Temp """
    #color_button_change()
    #check_pallet(3, 1, False)
    # while True:
        # Left_area('hej')
        #crane_motor.run_angle(100, -500, Stop.HOLD, False)
        # drive_to_correct_colour()
        #pickup_pallet()

    color_button_change()

    while True:
        # Left_area('hej')
        #crane_motor.run_angle(100, -500, Stop.HOLD, False)
        drive_to_correct_colour()
        # pickup_pallet()

def rgb_to_color(color, last_color=None):
    if max(color) == color[0]:
        result = 'red'
        if color[1]*1.3 > color[0]:
            result = 'brown'
    elif max(color) == color[1]:
        result = 'green'
    elif max(color) == color[2]:
        result = 'blue'
        if color[0]*1.8 > color[2]:
            result = 'purple'
    elif max(color) < 10:
        result = 'black'
    else:
        result = last_color
    return result

def Left_area(curent_color):
    """ Temp """
    global timer_area
    if color_sensor.color() == curent_color:#Temp color
        timer_area=0
    else:
        timer_area+=1
    if timer_area >= 200:
        print_text_to_screen(40, 50, "Robot has left the area", 5)
    #print(timer_area)

# def left_area(areaColor):
#     if ColorSensor == areaColor:
#         print('Robot has left sprcific area')

def returnToSpecArea(areaColor):
    """ Temp """
    groundColor = color_sensor.color()
    turnSpeed = 90
    
    # Kör runt i en cirkel som blir större tills färgsensorn hittar rätt färg
    while groundColor != areaColor:
        robot.drive(50, turnSpeed)
        turnSpeed -= 1
        groundColor = color_sensor.color()
    return "Tillbaka!"

def ExitSpecArea(areaColor):
    """ Temp """
    groundColor = color_sensor.color()
    turnSpeed = 90

    # Kör runt i en cirkel som blir större tills färgsensorn hittar en ny färg
    while groundColor == areaColor:
        robot.drive(50, turnSpeed)
        turnSpeed -= 0.1
        groundColor = color_sensor.color()
    return "Ute!"

def pickup_pallet():
    """ Temp """
    global is_holding
    #Här måste den först identifiera att den kan plocka upp, vänta på specifikationer

    # Checkar så att den inte redan har lyft upp objektet och ifall objektet är på "gaffeln"
    if not is_holding:
        #sätter graderna på 0 för att förenkla mätandet sedan

        #Lyfter tills kranen har lyft objektet 45 grader upp eller 
        #tills den tappar objektet
        while crane_motor.angle() < 100:
            
            #cycle = 100  
            crane_motor.dc(100)
            print(crane_motor.angle())
        crane_motor.hold()
        wait(2000)
        #crane_motor.run(0)
        print(touch_sensor.pressed())
        #Om den fortfarande håller objektet registreras det
        if touch_sensor.pressed():
            is_holding = True
            #Om den tappade objektet går den ned igen
        else:
            while crane_motor.angle() >= 0:
                crane_motor.run_angle(100, -500, Stop.HOLD, False)
                crane_motor.hold()
    #Ser till så att den håller uppe lasten när den väl har plockat upp 

def check_pallet(tries, direction, second_try):

    if tries > 0:
        robot.drive(10, 0)

        if color_sensor.reflection <= 10:
            robot.straight(-10)
            robot.turn(direction * -90)
            robot.straight(7)
            robot.turn(direction * 90)

            check_pallet(tries - 1, direction, second_try)
        elif touch_sensor.pressed():
            #kollar om det finns en pall på eller inte och agerar motsvarande
            #if ultrasonic.distance() < 30:
                #pick_up_elevated
            #else:
            pickup_pallet()
            #åker tillbaka hur vet jag inte
    elif tries == 0 and not second_try:
        robot.turn(-90)
        #roboten kör fram tillräckligt nära för att kunna starta checkpallet igen
        check_pallet(1, -1,True)
    elif tries == 0 and second_try:
            robot.turn(180)
            robot.straight(50)
            robot.turn(90)


def liftdown_pallet():
    """ Temp """
    if is_holding and touch_sensor.pressed():

        return
    return

# def motors_perform(action, speed_modifier):
#     """ Temp """
#     if action == "hold":
#         robot.drive(0,0)
#     elif action == "forward":
#         # motor_right.run(360 * speed_modifier)
#         # motor_left.run(360 * speed_modifier)
#         robot.drive(36 * speed_modifier,0)
#     elif action == "left":
#         motor_right.run(180 * speed_modifier)
#         motor_left.run(-180 * speed_modifier)
#     elif action == "right":
#         motor_right.run(-180 * speed_modifier)
#         motor_left.run(180 * speed_modifier) 

def collisionavoidence():
    """ Temp """
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
    """ Temp """
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
    """ Folow a line with one sensor """ # are going to give more ditail
    speed_modifier = collisionavoidence()
    correction = (detect_colorline() - color_sensor.reflection()) * 1.65 # Öka för att svänga mer # changed the av to detect_colorline so that it sould run nicely on all colour.

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
    current_color_detected = color_sensor.color()
    new_linereflection = color_reflection[current_color_detected]

    return (new_linereflection + dark) / 2

def drive_to_correct_colour():
    """ Temp """
    temp = Color.YELLOW
    current_color = color_sensor.color
    if current_color != color_sensor.color:
        if color_sensor.color() == temp:
            drive() # ska svänga. vet ej om den kommer att göra det automatisk eller fall man ska hårdkåda den delen.
        else:
            robot.drive(speed, 0)
            wait(100)
            drive()
    else:
        drive()


""" Variabler """
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
<<<<<<< HEAD
speed = 50
light = 80
dark = 20
avg_reflection = (light + dark) / 2
=======
speed = 300
dark = 36
>>>>>>> ff3844f00f6ea83e21bb54d87daa625973fd2dd2

color_to_fetch = Color.RED 

#from left to right, (clear), (black), (Blue), (Green), (Yellow), (Red), (White), (Brown)
color_reflection = {Color.BLACK: 9, Color.BLUE: 0, Color.GREEN: 3, Color.YELLOW: 59, Color.RED: 39, Color.WHITE: 100, Color.BROWN: 5}
possible_colors = [Color.BLACK, Color.BLUE]

current_color_reflection = 0
color_background_reflection = 9
timer_area = 0

red = ['red', (51,18,16), (36, 10, 9)]
green = ['green', (7,31,5), (5,23,4)]
my_colors = [red, green]

""" if Main """
if __name__ == '__main__':
    sys.exit(main())

