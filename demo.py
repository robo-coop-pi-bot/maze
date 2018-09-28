#!/usr/bin/python3

import time
from pibotlibrary import Motors,Led,Ultrasonic,Keyboard,Pins

sensor = Ultrasonic()

distance = sensor.Distance()
print(str(distance))

# Initialise motor interface setting a default speed of 50%, a trim
# of zero (how much faster or slower to drive the right hand motors),
# and enable diagnostic output.
motor = Motors(debug=True,speed=50,trim=0)

# OR

# Initialise motor interface using all defaults: speed = 50%, trim = 0,
# and diagnostic output off.
# motor = Motors()

# Move forward at current speed for two seconds
motor.SetSpeed(75)
motor.SetTrim(-5)
motor.Backward()
motor.SpinLeft()
time.sleep(0.8)
motor.TurnRight()
time.sleep(0.8)
motor.TurnLeft()
time.sleep(0.8)
motor.TurnRight()
time.sleep(0.8)
motor.TurnLeft()
time.sleep(0.8)
motor.TurnRight()
time.sleep(0.8)
motor.TurnLeft()
time.sleep(0.8)
motor.TurnRight()
time.sleep(0.8)
motor.TurnLeft()
time.sleep(0.8)
motor.TurnRight()
time.sleep(0.8)
motor.TurnLeft()
time.sleep(0.8)
motor.Stop()

# Other motor methods are:

# motor.Backward()       Move backwards
# TurnLeft()             Curve to left (Left motors stop, right motors move)
# TurnRight()            Curve to right
# SpinLeft()             Turn on the spot (left motors back, right forward)
# SpinRight()
#
# SetSpeed(speed)        Set speed as percentage (0 - 100)
# SetTrim(diff)          Set right motors to be 'diff' faster then left motors
#                        to adjust to get straight line (diff may be negative).
#
# Drive(left,Right,time) Set left and right motor speeds (+ve or -ve) and length
#                        of time (in seconds) - time is optional

motor.Shutdown()



