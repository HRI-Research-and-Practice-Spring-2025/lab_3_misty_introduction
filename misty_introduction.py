import sys, os, time
sys.path.append(os.path.join(os.path.join(os.path.dirname(__file__), '..'), 'Python-SDK'))

from mistyPy.Robot import Robot
from mistyPy.Events import Events

if len(sys.argv) != 2:
    print("Usage: python misty_introduction.py <Misty's IP Address>")
    sys.exit(1)

ip_address = sys.argv[1]
misty = Robot(ip_address)

misty.speak("Hi!")

# TODO: Complete Misty's introduction