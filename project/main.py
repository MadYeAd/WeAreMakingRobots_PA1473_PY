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
    destination='white'
    destination = input('destenation  ')
    while True:

        
    #     input()
    #     rgb = color_sensor.rgb()
    #     color = Rgb_to_color(rgb)
    #     print(rgb, color)

    # while True:
    # print(color_sensor.reflection())

        # # print(color_sensor.rgb())
        current_color = Rgb_to_color(color_sensor.rgb())
        print(current_color)
        # # print_text_to_screen(0,0,'',1)
        # destination = 'blue'
        if current_color == 'brown':
            print('Roundabout')                                        # måste kanske säga till den att sbäna lite.
            drive_to_correct_color(destination)
            while current_color != destination:
                print('half done')
                current_color = Rgb_to_color(color_sensor.rgb())
                robot.drive(20,-10)
                # print(current_color)
                
        print('done')
        drive()

    #exit_warehouse()
    
    # while True:
    #     collisionavoidence()
    # enterspecarea('red')
    
    #destination = 'red'
    #current_color_rgb = color_sensor.rgb()
    #current_color = rgb_to_color(current_color_rgb)
    #if current_color == 'brown':
        #drive_to_correct_color(destination)

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

    ##pickup_procedure(3, -1, 2000)

    #drive_to_pickup()
    # pickup_procedure(3, 1, 550)
    return 0
    # check_pallet(3, -1)
    #pickup_procedure(3, 1, 550)




#------- Start David -------
# Koden fungerar i simulatorn men måste antagligen justeras för verkligheten

# Bestämmer färg från inmatad rgb

def Rgb_to_color(rgb):#Fix num
    if rgb[0] <=100 and rgb[0] >=60 and rgb[1] <=100 and rgb[1] >=65 and rgb[2] <=100 and rgb[2] >=95:
        return 'white'
    elif rgb[0] <=10 and rgb[0] >=0 and rgb[1] <=10 and rgb[1] >=0 and rgb[2] <=10 and rgb[2] >=0:
        return 'black'
    elif rgb[0] <=17 and rgb[0] >=7 and rgb[1] <=16 and rgb[1] >6 and rgb[2] <=43 and rgb[2] >=26:
        return 'purple'
    elif rgb[0] <=15 and rgb[0] >=5 and rgb[1] <=41 and rgb[1] >=31 and rgb[2] <=22 and rgb[2] >=12:
        return 'green'
    elif rgb[0] <=20 and rgb[0] >=10 and rgb[1] <=20 and rgb[1] >=10 and rgb[2] <=21 and rgb[2] >=9:
        return 'brown'
    elif rgb[0] <=59 and rgb[0] >=40 and rgb[1] <=24 and rgb[1] >=14 and rgb[2] <=35 and rgb[2] >=25:
        return 'red'
    elif rgb[0] <=15 and rgb[0] >=5 and rgb[1] <=26 and rgb[1] >=16 and rgb[2] <=49 and rgb[2] >=33:
        return 'blue'
    elif rgb[0] <=22 and rgb[0] >=11 and rgb[1] <=25 and rgb[1] >=3 and rgb[2] <=21 and rgb[2] >=3:
        return 'brown' #Yellow
    else:
        return 'white'


def exit_warehouse(dest):

    if dest == 'red':
        side = -1
    else: 
        side = 1

    robot.turn(90*side)

    rgb = color_sensor.rgb()
    color = Rgb_to_color(rgb)
    while color != 'white':
        robot.drive(30, 0)
        rgb = color_sensor.rgb()
        color = Rgb_to_color(rgb)
        print(rgb, color)
    ev3.speaker.beep()
    thread_text(text=color)

    exit = False
    while not exit:
        rgb = color_sensor.rgb()
        color = Rgb_to_color(rgb)
        print(rgb,color)
        if color == 'white':
            robot.drive(30,20*side)
        elif color == dest:
            exit = True
        else:
            robot.drive(30,-40*side)

    robot.stop()


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

def pickup_pallet():
    """ Temp """
    print("jag har gått in i funktionen")
    global is_holding
    #Här måste den först identifiera att den kan plocka upp, vänta på specifikationer

    # Checkar så att den inte redan har lyft upp objektet och ifall objektet är på "gaffeln"
    if not is_holding:
        #sätter graderna på 0 för att förenkla mätandet sedan
        print("jag vet att jag inte håller något")
        #Lyfter tills kranen har lyft objektet 45 grader upp eller 
        #tills den tappar objektet
    
        amount_of_tries = [-3,-2,-1]
        while crane_motor.angle() < 150 and amount_of_tries[-1] != amount_of_tries[-2]:
            print("jag har börjat lyfta")
            cycle = 100  
            crane_motor.dc(100)
            print(crane_motor.angle())
            amount_of_tries.append(crane_motor.angle())
            print(amount_of_tries)
            print(amount_of_tries[-1],amount_of_tries[-2])
        
        crane_motor.hold()
        #crane_motor.run(0)
        print(touch_sensor.pressed())
        #Om den fortfarande håller objektet registreras det
        if touch_sensor.pressed():
            is_holding = True
            #Om den tappade objektet går den ned igen
        # else:
        #     while crane_motor.angle() >= 0:
        #         crane_motor.run_angle(100, -500, Stop.HOLD, False)
        #         crane_motor.hold()
        crane_motor.hold()
        
        wait(5000)
    #Ser till så att den håller uppe lasten när den väl har plockat upp 

def pickup_procedure(tries, direction, distance):
    has_picked_up = False
    for x in range(tries):
                if ultrasonic_sensor.distance() > distance:
                    robot.turn(direction * -turn_rate)
                    robot.straight(180)
                    robot.turn(direction * turn_rate)
                elif ultrasonic_sensor.distance() < distance:
                    drive_to_pickup()
                    has_picked_up = True
                    
                
                if has_picked_up:
                    x = tries
    if direction == 1:
        exit_warehouse('blue')
    elif direction == -1:
        exit_warehouse('red')
    

def drive_to_pickup():
    while touch_sensor.pressed() == False:
        robot.drive(100, 0)
    robot.drive(0, 0)
    if touch_sensor.pressed() and ultrasonic_sensor.distance() < 340:
        pick_up_elevated()
    elif touch_sensor.pressed() and ultrasonic_sensor.distance() > 340:
        pickup_pallet()

def pick_up_elevated():
    fork_length = 100
    #backar
    robot.straight(fork_length * -1)
    #höjer kran
    #while crane_motor.angle() < 100:
     #       print("jag har börjat lyfta")
      #      #cycle = 100  
       #     crane_motor.dc(35)
    crane_motor.run_target(40, 100, then=Stop.HOLD, wait = True)
    crane_motor.hold()
    #kör in och plockar upp när den rör touchsensorn
    robot.straight(fork_length)
    
    #while crane_motor.angle() < 150:
     #       print("jag har börjat lyfta 2")
            #cycle = 100  
      #      crane_motor.dc(100)
    #backar ut och sänker den
    #crane_motor.hold()

    crane_motor.run_target(40, 150, then=Stop.HOLD, wait = True)

    robot.straight((fork_length + 20)*-1)
    #while crane_motor.angle() > 130:
            #print("jag har börjat sänka")
            #cycle = 100  
            #crane_motor.dc(-50)
    crane_motor.run_target(40, 130, then=Stop.HOLD, wait = True)
    
    
    #return to track

def reset_angle():
    while crane_motor.angle() > 0:
            #cycle = 100  
            crane_motor.dc(-50)

def check_pallet(tries, direction):
    robot.turn(-turn_rate * direction)
    robot.straight(70)
    robot.turn(turn_rate * direction)
    robot.straight(150)
    robot.turn(direction * -turn_rate)

    if ultrasonic_sensor.distance() < 550:
        drive_to_pickup()
    else:
        
        robot.turn(direction* turn_rate)
        robot.straight(240)
        robot.turn(direction * -turn_rate)
        if ultrasonic_sensor.distance() < 550:
            drive_to_pickup()
            
        else:
            robot.turn(direction* turn_rate)
            robot.straight(-240)
            pickup_procedure(tries, direction, 550)
            #åker tillbaka, hur vet jag inte

def navigate_white():
    robot.straight(40)
    robot.turn(124)
    pickup_procedure(5, 1, 700)
    if touch_sensor.pressed() == False:
        robot.turn(248)
        pickup_procedure(5, 1, 700)
    
    if touch_sensor.pressed() == False:
        robot.straight(100)
        robot.turn(124)
        pickup_procedure(6, -1, 1000)

def test_distance():
    
    print(ultrasonic_sensor.distance())
        

def secified_colur(colur):  #in dropof and delevery
    if colur==1:#orange
        return 'left'
    else:
        return 'right'


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
    """ change the speed depending how close objekt is """
    # print(ultrasonic_sensor.distance())
    if ultrasonic_sensor.distance() < 450 and ultrasonic_sensor.distance() > 400:
        thread_text(40,50,'D-speed1', 1)
        return 0.8
        
    elif ultrasonic_sensor.distance() < 400 and ultrasonic_sensor.distance() > 350:
        thread_text(30,50,'D-speed2', 1)
        return 0.6 

    elif ultrasonic_sensor.distance() < 350 and ultrasonic_sensor.distance() > 300:
        thread_text(30,50,'D-speed3', 1)
        return 0.4

    elif ultrasonic_sensor.distance() < 300 and ultrasonic_sensor.distance() > 250:
        thread_text(30,50,'D-speed4', 1)
        return 0.2

    elif ultrasonic_sensor.distance() < 250:
        thread_text(30,50,'Full stop!', 1)
        return 0.0
    else:
        return 1

def color_button_change():
    """ Color fetcher/changer with the help of the buttons. """
    button = brick.buttons()

    if Button.LEFT in button:
        #change color to red
        drive_to_correct_color("red")
        thread_text(10, 50, "Fetching Red Item", 2)
    elif Button.RIGHT in button: 
        drive_to_correct_color("blue")
        thread_text(10, 50, "Fetching Blue Item", 2)

def thread_text(x_position = 40, y_position = 50, text = "", seconds_on_screen = 0.5):
    """Threaded operation that print a text to the middle of the screen. It does not interupt any other functions."""

    th.Thread(target=print_text_to_screen, args=(x_position, y_position, text, seconds_on_screen)).start()

def print_text_to_screen(x_position, y_position, text, seconds_on_screen):
    """Printing text to screen while stopping any on going operation until it has removed the text from the screen"""

    ev3.screen.draw_text(x_position, y_position, text)
    time.sleep(seconds_on_screen)
    ev3.screen.clear()

def hold_fork():
    crane_motor.run_target(20, 40, then=Stop.HOLD, wait=False)

def misplaced_item():
    global is_holding
    if touch_sensor.pressed() and not is_holding:
        print_text_to_screen(40,50,'Misplaced item', 30)
        emergency_mode()

    if ultrasonic_sensor.distance() > 100:
        return 

def abort_collection():

    return

def emergency_mode():
    #return to warehouse 
    robot.straight(-150)
    robot.turn(90)

    drive()
    current_color = Rgb_to_color(color_sensor.color)

    if current_color == "brown":
        drive_to_correct_color("green")

def drive():
    """ Folow a line with one sensor
    blue =19
    red = 76
    purple = 16
    brown = 23
    green = 13
    """
  # are going to give more ditail
    
    global speed

    speed_modifier = collisionavoidence()
    # print(Rgb_to_color(color_sensor.rgb()))
    if not Rgb_to_color(color_sensor.rgb()) == 'white':
        colorline = detect_colorline()
    else:
        colorline = 85
    # print(colorline)
    correction = (colorline - color_sensor.reflection()) * 2.00 # Öka för att svänga mer # changed the av to detect_colorline so that it sould run nicely on all colour.
    print(color_sensor.reflection())
    print(correction)
    
    # correction = (colorline - color_sensor.reflection()) * 1.65 # Öka för att svänga mer # changed the av to detect_colorline so that it sould run nicely on all colour.
    if touch_sensor.pressed() and not is_holding:
        print_text_to_screen(40,50,'Missplased item', 30)

    if correction >= 6 or correction <=-4: # 6(a) är hur långt in på linjen och -4(b) är när den svänger in mot linjen
        speed_modifier *= 0.2
        if correction <=-4:# #Ska vara överäns med if-satsen (b)
            mod=correction*(-1.7) #Öka om skarpare ytterkurver
        else:
            mod = correction*(2.5) #Öka om skarpare innerkurvor
        modifier=0.55-(mod/1000) # öka första variablenför att minska föränding av hastighet
        
        speed_modifier -= modifier
    else:
        correction=0
    if speed_modifier < 0:
        mod_speed = speed * (speed_modifier*(-1))
    else:
        mod_speed = speed * (speed_modifier)
    # mod_speed = speed * -speed_modifier 

    robot.drive(mod_speed , -correction)

# def reflection_on_color():
#     """ this is temp and i might remove funtion"""
#     current_color = Rgb_to_color(color_sensor.rgb())
#     global dark 
#     global light 
#     if current_color == 'red':
#         dark = 90
#         light = 100
#     elif current_color == 'blue':
#         dark = 19
#         light = 50

def detect_colorline():
    new_linereflection = color_reflection_dict[Rgb_to_color(color_sensor.rgb())]

    return (new_linereflection + dark) / 2


# def detect_colorline():
#     color = color_sensor.rgb()
#     new_linereflection = color_reflection_dict[Rgb_to_color(color)]

#     return (new_linereflection + background_color) / 2

def get_colorlineAVG(color):
    if color in color_background_reflection.keys():
        return (color_reflection_dict[color] + background_color) / 2
    else: 
        print()
        return 

def right_wharhouse(colur):
    if colur=='red':
        drive_to_correct_color('red')
        
    else:
        drive_to_correct_color('blue')

def drive_to_correct_color(destination):
    
     
    

    going = True
    while going: 
        current_color_rgb = color_sensor.rgb()
        current_color = Rgb_to_color(current_color_rgb)
        # print(current_color)
        if current_color == destination: #sljdhfkjsdh
            print('im turning')
            # robot.drive(-50,0)
            # wait(700)
            # robot.drive(50, -90)
            robot.turn(-90)
            # wait(1300)
            going = False 
        elif current_color == 'brown':
            ti=0
            while ti <= 10 and not current_color == destination:
                current_color_rgb = color_sensor.rgb()
                current_color = Rgb_to_color(current_color_rgb)
                print(current_color)
                print('ti',ti)
                print('follow line')
                drive()
                if current_color == 'white':
                    ti+=1
                else:
                    ti=0
                
        elif current_color == 'white':
            # print('im outside')
            robot.drive(20,20)
        else:
            print("going past line")
            robot.drive(100, 0)
            wait(100)  #sjkdhfsjdjhf
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
turn_rate = 128

mod = 1 
speed = 100
dark = 30
light = 50

background_color = 1

destination = 'red'

color_to_fetch = Color.RED 

#from left to right, (clear), (black), (Blue), (Green), (Yellow), (Red), (White), (Brown)

color_reflection_dict = {"black": 9, "blue": 17, "green": 13, "red": 93, "white": 100, "brown": 24, "purple": 15}

current_color_reflection = 0
color_background_reflection = 9
timer_area = 0

# colorline = get_colorlineAVG("green")
#colorline = get_colorlineAVG("green")

""" if Main """
if __name__ == '__main__':
    sys.exit(main())

