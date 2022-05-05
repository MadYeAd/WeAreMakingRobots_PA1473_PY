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
    # enterspecarea('red')
    """ Temp """
    # print(touch_sensor.pressed())

    #color_button_change()
    # check_pallet(2, -1, False)
    # while True:
        # Left_area('hej')
        #crane_motor.run_angle(100, -500, Stop.HOLD, False)
        # drive_to_correct_colour()
        #pickup_pallet()


    # while True:
    #     color_button_change()
        # Left_area('hej')
        #crane_motor.run_angle(100, -500, Stop.HOLD, False)
        # drive_to_correct_colour()
        # pickup_pallet()


def rgb_to_color(color, last_color=None): 
    
    #Den här borde fungera

    if max(color) == color[0]:
        result = 'red'
        if color[1]*1.5 > color[0]:
            result = 'brown'
    elif max(color) == color[1]:
        result = 'green'
        if color[0]*2 > color[1]:
            result = 'brown'
    elif max(color) == color[2]:
        result = 'blue'
        if color[2] < 30:
            result = 'purple'
    elif max(color) < 10:
        result = 'black'
    else:
        result = 'White'
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

def pick_up_elevated():
    fork_length = 100
    #backar
    robot.straight(fork_length * -1)
    #höjer kran
    crane_motor.run_angle(30, 300, Stop.COAST)
    #kör in och plockar upp när den rör touchsensorn
    robot.drive(100)
    if touch_sensor.pressed:
        robot.drive(0)
        crane_motor.run_angle(30, 320, Stop.COAST)
    #backar ut och sänker den
    robot.straight((fork_length + 10)*-1)
    crane_motor.run_angle(30, 250, Stop.COAST)
    #return to track


def check_pallet(tries, direction, second_try):
    robot.straight(70)
    robot.turn(direction * -120)

    if ultrasonic_sensor.distance() < 1500:
        robot.drive(200, 0)
        if touch_sensor.pressed() and ultrasonic_sensor.distance() < 400:
            pick_up_elevated()
        elif touch_sensor.pressed and ultrasonic_sensor.distance() > 400:
            pickup_pallet()
    else:
        
        robot.turn(direction* 120)
        robot.straight(180)
        robot.turn(direction * -120)
        if ultrasonic_sensor.distance() < 1500:
            robot.drive(200, 0)
            if touch_sensor.pressed() and ultrasonic_sensor.distance() < 400:
                pick_up_elevated()
            elif touch_sensor.pressed and ultrasonic_sensor.distance() > 400:
                pickup_pallet()
            
        else:
            robot.turn(direction* 120)
            robot.straight(-180)
            for x in range(tries):
                if ultrasonic_sensor.distance() > 1500:
                    robot.turn(direction * -120)
                    robot.straight(180)
                    robot.turn(direction * 120)
                elif ultrasonic_sensor.distance() < 1500:
                    robot.drive(200, 0)
                    if touch_sensor.pressed() and ultrasonic_sensor.distance() < 400:
                        pick_up_elevated()
                    elif touch_sensor.pressed and ultrasonic_sensor.distance() > 400:
                        pickup_pallet()


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
        thread_text(10, 50, "Fetching Red Item", 2)
    elif Button.RIGHT in button: 
        color_change(Color.BLUE)
        thread_text(10, 50, "Fetching Blue Item", 2)

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
    color = color_sensor.rgb()
    current_color_detected = rgb_to_color(color)
    new_linereflection = color_reflection_dict[current_color_detected]

    return (new_linereflection + dark) / 2

def drive_to_correct_color(current_color):
    """ Temp """
    print("im in drive to correct colour")
    temp = 'red'
    current_color = color_sensor.rgb()
    current_color = rgb_to_color(current_color)
    if current_color != color_sensor.color:
        if color_sensor.color() == temp:
            print("i need to turn now")
            robot.turn(-90)
            drive() # ska svänga. vet ej om den kommer att göra det automatisk eller fall man ska hårdkåda den delen. # måst hårdkoda.
        else:
            print("going past line")
            robot.straight(20)
            drive()
    else:
        print("i folow line now")
        drive()

def enterspecarea(destination):
    ev3.speaker.beep()
    color = color_sensor.rgb()
    result = rgb_to_color(color)
    while result != 'brown':
        drive()
        color = color_sensor.rgb()
        result = rgb_to_color(color, result)
    robot.turn(-120)
    while result != destination:
        if result != 'brown':
            robot.straight(20)
            print(result)
        drive()
        color = color_sensor.rgb()
        result = rgb_to_color(color, result)
    robot.turn(-120)
    while result != 'black':
        drive()
        color = color_sensor.rgb()
        result = rgb_to_color(color, result)
    return 'done'


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
speed = 50
dark = 36

color_to_fetch = Color.RED 

#from left to right, (clear), (black), (Blue), (Green), (Yellow), (Red), (White), (Brown)

color_reflection_dict = {"black": 9, "blue": 0, "green": 3, "yellow": 59, "red": 39, "white": 100, "brown": 5, "purple": 10}
possible_color = ["black", "blue"] #...

current_color_reflection = 0
color_background_reflection = 9
timer_area = 0

red = ['red', (51,18,16), (36, 10, 9)]
green = ['green', (7,31,5), (5,23,4)]
my_colors = [red, green]

current_color = rgb_to_color()

""" if Main """
if __name__ == '__main__':
    sys.exit(main())

