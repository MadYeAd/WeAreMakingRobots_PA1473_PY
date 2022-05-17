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

    drive_to_pickup()



#------- Start David -------
# Koden fungerar i simulatorn men måste antagligen justeras för verkligheten

# Bestämmer färg från inmatad rgb

def Rgb_to_color(rgb):
    if rgb[0] <=100 and rgb[0] >=65 and rgb[1] <=100 and rgb[1] >=86 and rgb[2] <=100 and rgb[2] >=95:
        return 'white'
    elif rgb[0] <=10 and rgb[0] >=0 and rgb[1] <=10 and rgb[1] >=0 and rgb[2] <=10 and rgb[2] >=0:
        return 'black'
    elif rgb[0] <=17 and rgb[0] >=7 and rgb[1] <=16 and rgb[1] >6 and rgb[2] <=47 and rgb[2] >=37:
        return 'purple'
    elif rgb[0] <=14 and rgb[0] >=4 and rgb[1] <=54 and rgb[1] >=44 and rgb[2] <=27 and rgb[2] >=17:
        return 'green'
    elif rgb[0] <=22 and rgb[0] >=12 and rgb[1] <=25 and rgb[1] >=15 and rgb[2] <=21 and rgb[2] >=11:
        return 'brown'
    elif rgb[0] <=75 and rgb[0] >=65 and rgb[1] <=30 and rgb[1] >=20 and rgb[2] <=44 and rgb[2] >=34:
        return 'red'
    elif rgb[0] <=15 and rgb[0] >=5 and rgb[1] <=32 and rgb[1] >=22 and rgb[2] <=56 and rgb[2] >=42:
        return 'blue'
    else:
        return 'white'

# Tar sig tillbaka till banan från warehouse
def exit_warehouse():

    # (Start 1) Åker rakt fram till kanten av warehouset
    rgb = color_sensor.rgb()
    color = Rgb_to_color(rgb)
    while color != 'white':
        robot.drive(30, 0)
        rgb = color_sensor.rgb()
        color = Rgb_to_color(rgb)
    # (Slut 1)

    # (Start 2) Åker i bågar längst kanten av warehouset tills den hittar linjen
    exit = False
    while not exit:

        # (Start 3) Åker i en båge tills färgen inte längre är vid
        while color == 'white':
            robot.drive(30, 40) # !!! Värdena här kan behöva justeras !!!
            rgb = color_sensor.rgb()
            color = Rgb_to_color(rgb)
        # (Slut 3)

        # (Start 4) Kör rakt fram 100 gånger. För att se om den är vid banan
        for i in range(100): # !!! rangen kan behöva justeras !!!
            rgb = color_sensor.rgb()
            color = Rgb_to_color(rgb)
            # Blir färgen vit är den vid banan och 'exit' blir True
            if color == 'white':
                exit = True
                print(exit)
            robot.drive(30,0)
        # (Slut 4)

        # (Start 5) Är 'exit' False så är den inte vid banan och 
        # vänder då 180 grader för att vändas mot kanten av warehouset igen
        if not exit:
            robot.turn(180) # !!! Graderna kan behöva justeras !!!
            # Kör till kanten av warehouset efter att ha vänt
            while color != 'white':
                robot.drive(30, 0)
                rgb = color_sensor.rgb()
                color = Rgb_to_color(rgb)
        # (Slut 5)
    robot.stop()
    # (Slut 2)

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

def misplaced_item():
    global is_holding
    if touch_sensor.pressed() and not is_holding:
        print_text_to_screen(40,50,'Misplaced item', 30)

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
            #cycle = 100  
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
                    robot.turn(direction * -123)
                    robot.straight(180)
                    robot.turn(direction * 123)
                elif ultrasonic_sensor.distance() < distance:
                    drive_to_pickup()
                    has_picked_up = True
                    
                
                if has_picked_up:
                    x = tries

def drive_to_pickup():
    while touch_sensor.pressed() == False:
        robot.drive(100, 0)
    robot.drive(0, 0)
    if touch_sensor.pressed() and ultrasonic_sensor.distance() < 400:
        pick_up_elevated()
    elif touch_sensor.pressed() and ultrasonic_sensor.distance() > 400:
        pickup_pallet()

def pick_up_elevated():
    fork_length = 100
    #backar
    robot.straight(fork_length * -1)
    #höjer kran
    while crane_motor.angle() < 100:
            print("jag har börjat lyfta")
            #cycle = 100  
            crane_motor.dc(35)
    crane_motor.hold()
    #kör in och plockar upp när den rör touchsensorn
    robot.straight(fork_length)
    
    while crane_motor.angle() < 150:
            print("jag har börjat lyfta 2")
            #cycle = 100  
            crane_motor.dc(100)
    #backar ut och sänker den
    crane_motor.hold()
    robot.straight((fork_length + 20)*-1)
    while crane_motor.angle() > 130:
            print("jag har börjat sänka")
            #cycle = 100  
            crane_motor.dc(-50)
    
    
    #return to track

def specified_color(colur):  #in dropof and delevery
    if colur==1:#orange
        return 'left'
    else:
        return 'right'

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
            elif touch_sensor.pressed() and ultrasonic_sensor.distance() > 400:
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
                    elif touch_sensor.pressed() and ultrasonic_sensor.distance() > 400:
                        pickup_pallet()

def collisionavoidence():
    """ Temp """
    
    if ultrasonic_sensor.distance() < 400 and ultrasonic_sensor.distance() > 350:
        thread_text(30,50,'D-speed1', 1)
        return 0.8
        
    elif ultrasonic_sensor.distance() < 350 and ultrasonic_sensor.distance() > 300:
        thread_text(30,50,'D-speed2', 1)
        return 0.6 

    elif ultrasonic_sensor.distance() < 300 and ultrasonic_sensor.distance() > 250:
        thread_text(30,50,'D-speed3', 1)
        return 0.4

    elif ultrasonic_sensor.distance() < 250 and ultrasonic_sensor.distance() > 230:
        thread_text(30,50,'D-speed4', 1)
        return 0.2

    elif ultrasonic_sensor.distance() < 230:
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
    

def thread_hold (speed, target_angle):
    """Threaded operation for holding the fork in place"""

    th.Thread(target=hold_fork, args=(speed, target_angle)).start()

def hold_fork(speed, target_angle):
    """Needs testing"""

    crane_motor.run_target(speed, target_angle, then=Stop.HOLD, wait=False)

def drive():
    """ Folow a line with one sensor """ # are going to give more ditail
    global collerline
    global speed
    speed_modifier = collisionavoidence()
    if not Rgb_to_color(color_sensor.rgb()) == 'white':
        collerline= detect_colorline()
    
    correction = (collerline - color_sensor.reflection()) * 1.65 # Öka för att svänga mer # changed the av to detect_colorline so that it sould run nicely on all colour.
    if touch_sensor.pressed() and not is_holding:
        print_text_to_screen(40,50,'Missplased item', 30)

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
    mod_speed = speed * speed_modifier #temp to positive

    robot.drive(mod_speed , correction)

def detect_colorline():
    color = color_sensor.rgb()
    current_color_detected = Rgb_to_color(color)
    new_linereflection = color_reflection_dict[current_color_detected]

    return (new_linereflection + dark) / 2

def right_wharhouse(colur):
    if colur=='red':
        drive_to_correct_color('red')
        
    else:
        drive_to_correct_color('blue')

# Sugestion: put a while-loop in drive_to_correct_color and use that funcion always in the roundabout 
# and hard code in how it should do it since we know how big the roundabout is?

# def drive_to_correct_color_temp(current_color):
#     """ Temp """
#     print("im in drive to correct colour")
#     temp = 'red'
#     current_color = color_sensor.rgb()
#     current_color = rgb_to_color(current_color)
#     if current_color != color_sensor.color:
#         if color_sensor.color() == temp:
#             print("i need to turn now")
#             robot.drive(speed, -90)
#             wait(100)
#             drive() # ska svänga. vet ej om den kommer att göra det automatisk eller fall man ska hårdkåda den delen. # måst hårdkoda.
#         else:
#             print("going past line")
#             robot.drive(speed, 0)
#             wait(100)
#             drive()
#     else:
#         print("i folow line now")
#         drive()

def drive_to_correct_color(destination):
    going = True
    while going:
        current_color_rgb = color_sensor.rgb()
        current_color = Rgb_to_color(current_color_rgb)
        if current_color == destination:
            print('im turning')
            robot.drive(-50,0)
            wait(900)
            robot.drive(50, -90)
            wait(1700)
            going = False 
        if current_color == 'brown':
            drive()
        else:
            if current_color == 'white':
                robot.drive(50,20)
            else:
                print("going past line")
                robot.drive(100, 0)
                wait(100)
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


collerline=55

""" if Main """
if __name__ == '__main__':
    sys.exit(main())

