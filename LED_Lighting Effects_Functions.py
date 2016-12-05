#================================================#
#         LED Lighting Effects Functions         #
#================================================#

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

#Define the colors
RED = 11 ; ORANGE = 13 ; YELLOW = 15 ; GREEN = 16
BLUE = 18 ; VIOLET = 22 ; PINK = 29 ;WHITE = 31

#Setup the pins
def pin_setup():
    GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(RED,GPIO.OUT)
    GPIO.setup(ORANGE,GPIO.OUT)
    GPIO.setup(YELLOW,GPIO.OUT)
    GPIO.setup(GREEN,GPIO.OUT)
    GPIO.setup(BLUE,GPIO.OUT)
    GPIO.setup(VIOLET,GPIO.OUT)
    GPIO.setup(PINK,GPIO.OUT)
    GPIO.setup(WHITE,GPIO.OUT)

sec = 0
cycles = 0
flashes = 0

def setup(patterns, choice_list):
    pin_setup()
    all_off()
    print "Which pattern(s) would you like to see?"
    print
    for key in patterns:
        print "%r: " % key, patterns[key]
    print
    
    choice = raw_input("> ")
    try:
        while choice != '':
            if choice == 'all':
                choice_list.append('all')
            elif int(choice) not in range(0,len(patterns)):
                print "Please enter valid numbers only. %r was not registered." % choice
            elif type(int(choice)) == int:
                choice_list.append(choice)
            
            if 'all' in choice_list or len(choice_list) == len(patterns)-1:
                break
            choice = raw_input("> ")
    
        global sec, cycles, flashes 
        sec = float(raw_input("How many milliseconds between changes? "))/1000
        cycles = int(raw_input("How many cycles would you like to see? "))
        if '3' in choice_list or 'all' in choice_list or '8' in choice_list:
            flashes = int(raw_input("How many flashes would you like? "))
        print
            
    except ValueError:
        print "Please enter valid numbers only."
        GPIO.cleanup()
        print
    
def all_on():
    GPIO.output(RED,True)
    GPIO.output(ORANGE,True)
    GPIO.output(YELLOW,True)
    GPIO.output(GREEN,True)
    GPIO.output(BLUE,True)
    GPIO.output(VIOLET,True)
    GPIO.output(PINK,True)
    GPIO.output(WHITE,True)
        
def all_off():
    GPIO.output(RED,False)
    GPIO.output(ORANGE,False)
    GPIO.output(YELLOW,False)
    GPIO.output(GREEN,False)
    GPIO.output(BLUE,False)
    GPIO.output(VIOLET,False)
    GPIO.output(PINK,False)
    GPIO.output(WHITE,False)
    
def cascade_down():
    GPIO.output(RED,True) ; sleep(sec)
    GPIO.output(RED,False)
    GPIO.output(ORANGE,True) ; sleep(sec)    
    GPIO.output(ORANGE,False)
    GPIO.output(YELLOW,True) ; sleep(sec)       
    GPIO.output(YELLOW,False)
    GPIO.output(GREEN,True) ; sleep(sec)        
    GPIO.output(GREEN,False)
    GPIO.output(BLUE,True) ; sleep(sec)        
    GPIO.output(BLUE,False)
    GPIO.output(VIOLET,True) ; sleep(sec)        
    GPIO.output(VIOLET,False)
    GPIO.output(PINK,True) ; sleep(sec)         
    GPIO.output(PINK,False)
    GPIO.output(WHITE,True) ; sleep(sec)         
    GPIO.output(WHITE,False) ; sleep(sec)

def cascade_up():
    GPIO.output(WHITE,True) ; sleep(sec)
    GPIO.output(WHITE,False)
    GPIO.output(PINK,True) ; sleep(sec)
    GPIO.output(PINK,False)
    GPIO.output(VIOLET,True) ; sleep(sec)
    GPIO.output(VIOLET,False)
    GPIO.output(BLUE,True) ; sleep(sec)
    GPIO.output(BLUE,False)
    GPIO.output(GREEN,True) ; sleep(sec)
    GPIO.output(GREEN,False)
    GPIO.output(YELLOW,True) ; sleep(sec)
    GPIO.output(YELLOW,False)
    GPIO.output(ORANGE,True) ; sleep(sec)
    GPIO.output(ORANGE,False)
    GPIO.output(RED,True) ; sleep(sec)
    GPIO.output(RED,False) ; sleep(sec)

def flash_x_times(number_of_flashes):
    for x in range(0,number_of_flashes):
        all_on() ; sleep(sec)
        all_off() ; sleep(sec)

def both_ends_cascade():
    GPIO.output(RED,True)
    GPIO.output(WHITE,True) ; sleep(sec)
    
    GPIO.output(RED,False)
    GPIO.output(WHITE,False)
    GPIO.output(ORANGE,True)
    GPIO.output(PINK,True) ; sleep(sec)
    
    GPIO.output(ORANGE,False)
    GPIO.output(PINK,False)
    GPIO.output(YELLOW,True)
    GPIO.output(VIOLET,True) ; sleep(sec)
    
    GPIO.output(YELLOW,False)
    GPIO.output(VIOLET,False)
    GPIO.output(GREEN,True)
    GPIO.output(BLUE,True) ; sleep(sec)
    
    GPIO.output(GREEN,False)
    GPIO.output(BLUE,False)
    GPIO.output(YELLOW,True)
    GPIO.output(VIOLET,True) ; sleep(sec)
    
    GPIO.output(YELLOW,False)
    GPIO.output(VIOLET,False)
    GPIO.output(ORANGE,True)
    GPIO.output(PINK,True) ; sleep(sec)
    
    GPIO.output(ORANGE,False)
    GPIO.output(PINK,False)
    GPIO.output(RED,True)
    GPIO.output(WHITE,True) ; sleep(sec)
    
    GPIO.output(RED,False)
    GPIO.output(WHITE,False) ; sleep(sec)
    
def skip_down():
    GPIO.output(RED,True) ; sleep(sec)
    GPIO.output(RED,False)
    GPIO.output(YELLOW,True) ; sleep(sec)
    GPIO.output(YELLOW,False)
    GPIO.output(ORANGE,True) ; sleep(sec)
    GPIO.output(ORANGE,False)
    GPIO.output(GREEN,True) ; sleep(sec)
    GPIO.output(GREEN,False)
    GPIO.output(YELLOW,True) ; sleep(sec)
    GPIO.output(YELLOW,False)
    GPIO.output(BLUE,True) ; sleep(sec)
    GPIO.output(BLUE,False)
    GPIO.output(GREEN,True) ; sleep(sec)
    GPIO.output(GREEN,False)
    GPIO.output(VIOLET,True) ; sleep(sec)
    GPIO.output(VIOLET,False)
    GPIO.output(BLUE,True) ; sleep(sec)
    GPIO.output(BLUE,False)
    GPIO.output(PINK,True) ; sleep(sec)
    GPIO.output(PINK,False)
    GPIO.output(VIOLET,True) ; sleep(sec)
    GPIO.output(VIOLET,False)
    GPIO.output(WHITE,True) ; sleep(sec)
    GPIO.output(WHITE,False);sleep(sec)

def skip_up():
     GPIO.output(WHITE,True) ; sleep(sec)
     GPIO.output(WHITE,False)
     GPIO.output(VIOLET,True) ; sleep(sec)
     GPIO.output(VIOLET,False)
     GPIO.output(PINK,True) ; sleep(sec)
     GPIO.output(PINK,False)
     GPIO.output(BLUE,True) ; sleep(sec)
     GPIO.output(BLUE,False)
     GPIO.output(VIOLET,True) ; sleep(sec)
     GPIO.output(VIOLET,False)
     GPIO.output(GREEN,True) ; sleep(sec)
     GPIO.output(GREEN,False)
     GPIO.output(BLUE,True) ; sleep(sec)
     GPIO.output(BLUE,False)
     GPIO.output(YELLOW,True) ; sleep(sec)
     GPIO.output(YELLOW,False)
     GPIO.output(GREEN,True) ; sleep(sec)
     GPIO.output(GREEN,False)
     GPIO.output(ORANGE,True) ; sleep(sec)
     GPIO.output(ORANGE,False)
     GPIO.output(YELLOW,True) ; sleep(sec)
     GPIO.output(YELLOW,False)
     GPIO.output(RED,True) ; sleep(sec)
     GPIO.output(RED,False);sleep(sec)

def bounce():
    GPIO.output(RED,True) ; sleep(sec)
    GPIO.output(RED,False)
    GPIO.output(WHITE,True) ; sleep(sec)
    GPIO.output(WHITE,False)
    GPIO.output(ORANGE,True) ; sleep(sec)
    GPIO.output(ORANGE,False)
    GPIO.output(PINK,True) ; sleep(sec)
    GPIO.output(PINK,False)
    GPIO.output(YELLOW,True) ; sleep(sec)
    GPIO.output(YELLOW,False)
    GPIO.output(VIOLET,True) ; sleep(sec)
    GPIO.output(VIOLET,False)
    GPIO.output(GREEN,True) ; sleep(sec)
    GPIO.output(GREEN,False)
    GPIO.output(BLUE,True) ; sleep(sec)
    GPIO.output(BLUE,False)
    GPIO.output(YELLOW,True) ; sleep(sec)
    GPIO.output(YELLOW,False)
    GPIO.output(VIOLET,True) ; sleep(sec)
    GPIO.output(VIOLET,False)
    GPIO.output(ORANGE,True) ; sleep(sec)
    GPIO.output(ORANGE,False)
    GPIO.output(PINK,True) ; sleep(sec)
    GPIO.output(PINK,False)
    GPIO.output(RED,True) ; sleep(sec)
    GPIO.output(RED,False)
    GPIO.output(WHITE,True) ; sleep(sec)
    GPIO.output(WHITE,False)

def middle_out(flashes):
    for x in range(flashes):
        GPIO.output(GREEN,True)
        GPIO.output(BLUE,True) ; sleep(sec)
        GPIO.output(GREEN,False)
        GPIO.output(BLUE,False)
        GPIO.output(YELLOW,True)
        GPIO.output(VIOLET,True) ; sleep(sec)
        GPIO.output(YELLOW,False)
        GPIO.output(VIOLET,False)
        GPIO.output(ORANGE,True)
        GPIO.output(PINK,True) ; sleep(sec)
        GPIO.output(ORANGE,False)
        GPIO.output(PINK,False)
        GPIO.output(RED,True)
        GPIO.output(WHITE,True) ; sleep(sec)
        GPIO.output(RED,False)
        GPIO.output(WHITE,False)

def scroll_down():
    GPIO.output(RED,True) ; sleep(sec)
    GPIO.output(ORANGE,True) ; sleep(sec)
    GPIO.output(YELLOW,True) ; sleep(sec)
    GPIO.output(GREEN,True) ; sleep(sec)
    GPIO.output(BLUE,True) ; sleep(sec)
    GPIO.output(VIOLET,True) ; sleep(sec)
    GPIO.output(PINK,True) ; sleep(sec)
    GPIO.output(WHITE,True) ; sleep(sec)
    
    GPIO.output(RED,False) ; sleep(sec)
    GPIO.output(ORANGE,False) ; sleep(sec)
    GPIO.output(YELLOW,False) ; sleep(sec)
    GPIO.output(GREEN,False) ; sleep(sec)
    GPIO.output(BLUE,False) ; sleep(sec)
    GPIO.output(VIOLET,False) ; sleep(sec)
    GPIO.output(PINK,False) ; sleep(sec)
    GPIO.output(WHITE,False) ; sleep(sec)
    
def scroll_up():
    GPIO.output(WHITE,True) ; sleep(sec)
    GPIO.output(PINK,True) ; sleep(sec)
    GPIO.output(VIOLET,True) ; sleep(sec)
    GPIO.output(BLUE,True) ; sleep(sec)
    GPIO.output(GREEN,True) ; sleep(sec)
    GPIO.output(YELLOW,True) ; sleep(sec)
    GPIO.output(ORANGE,True) ; sleep(sec)
    GPIO.output(RED,True) ; sleep(sec)

    GPIO.output(WHITE,False) ; sleep(sec)
    GPIO.output(PINK,False) ; sleep(sec)
    GPIO.output(VIOLET,False) ; sleep(sec)
    GPIO.output(BLUE,False) ; sleep(sec)
    GPIO.output(GREEN,False) ; sleep(sec)
    GPIO.output(YELLOW,False) ; sleep(sec)
    GPIO.output(ORANGE,False) ; sleep(sec)
    GPIO.output(RED,False) ; sleep(sec)

def explode():
    GPIO.output(GREEN,True) ; sleep(sec)
    GPIO.output(BLUE,True) ; sleep(sec)
    GPIO.output(YELLOW,True) ; sleep(sec)
    GPIO.output(VIOLET,True) ; sleep(sec)
    GPIO.output(ORANGE,True) ; sleep(sec)
    GPIO.output(PINK,True) ; sleep(sec)
    GPIO.output(RED,True) ; sleep(sec)
    GPIO.output(WHITE,True) ; sleep(sec)
    
    GPIO.output(GREEN,False) ; sleep(sec)
    GPIO.output(BLUE,False) ; sleep(sec)
    GPIO.output(YELLOW,False) ; sleep(sec)
    GPIO.output(VIOLET,False) ; sleep(sec)
    GPIO.output(ORANGE,False) ; sleep(sec)
    GPIO.output(PINK,False) ; sleep(sec)
    GPIO.output(RED,False) ; sleep(sec)
    GPIO.output(WHITE,False) ; sleep(sec)
