import RPi.GPIO as GPIO
import time
from datetime import datetime
from pixels import Pixels
###############

BUTTON  = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)
pixels = Pixels()

while True:
    state = GPIO.input(BUTTON)
    if state:
        pixels.wakeup()
        record(duration=5)
        pixels.off()
    time.sleep(0.2)
    
###############
def get_file_name():
    now = datetime.now()
    year = str(now.year)
    month = str(now.month)
    day = str(now.day)
    hour = str(now.hour)
    minute = str(now.minute)
    second = str(now.second)
    file_name = year+'-'+month+'-'+day+'_'+hour+'-'+minute+'-'+second+'.wav'
    return file_name
#############
def record(duration):
    file_name = get_file_name()
    arecord -D plughw:1,0 -d duration file_name
############
    
