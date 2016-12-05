#================================================#
#          LED Lighting Effects Driver           #
#================================================#

import RPi.GPIO as GPIO
from time import sleep
import LED_Patterns_Functions
GPIO.setmode(GPIO.BOARD)
    
patterns = {1:"Cascade Down",
            2:"Cascade Up",
            3:"Flash [X] Times",
            4:"Both Ends Cascade",
            5:"Skip Down",
            6:"Skip Up",
            7:"Bounce",
            8:"Middle Out",
            9:"Scroll Down",
            10:"Scroll Up",
            11:"Explode",
            'all':"All Functions"
}
choices = []
    
print "Welcome to the LED Patterns program."
print "At any time, press CTRL-C to quit."
print

try:
    LED_Patterns_Functions.setup(patterns, choices)
    if GPIO.input(36): pass
    print "You chose to execute: "
    if 'all' in choices: print patterns['all']
    else:
        for x in choices:
            print patterns[int(x)]
    print
    print "Would you like a delay between cycles? 'yes' or 'no'"
    delay = raw_input("> ")
    print "Press the start button to begin the display"     
    while True:
        if GPIO.input(36):
            for x in range(LED_Patterns_Functions.cycles):
                if '1' in choices or 'all' in choices:
                    LED_Patterns_Functions.cascade_down()
                if '2' in choices or 'all' in choices:
                    LED_Patterns_Functions.cascade_up()
                if '3' in choices or 'all' in choices:
                    LED_Patterns_Functions.flash_x_times(LED_Patterns_Functions.flashes)
                if '4' in choices or 'all' in choices:
                    LED_Patterns_Functions.both_ends_cascade()
                if '5' in choices or 'all' in choices:
                    LED_Patterns_Functions.skip_down()
                if '6' in choices or 'all' in choices:
                   LED_Patterns_Functions.skip_up()
                if '7' in choices or 'all' in choices:
                    LED_Patterns_Functions.bounce()
                if '8' in choices or 'all' in choices:
                    LED_Patterns_Functions.middle_out(LED_Patterns_Functions.flashes)
                if '9' in choices or 'all' in choices:
                    LED_Patterns_Functions.scroll_down()
                if '10' in choices or 'all' in choices:
                    LED_Patterns_Functions.scroll_up()
                if '11' in choices or 'all' in choices:
                    LED_Patterns_Functions.explode()
                if delay == 'yes': sleep(LED_Patterns_Functions.sec*3)
                
except KeyboardInterrupt:
    print 
    print "PROGRAM TERMINATED: forced abort"
    GPIO.cleanup()
    
except RuntimeError:
    print "Program terminating due to failed setup."
