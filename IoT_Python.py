import RPi.GPIO as IO       
import time                          
IO.setwarnings(False)         
x=1
b0 =0                                    
b1 =0
b2 =0
b3 =0
b4 =0
b5 =0
b6 =0
b7 =0
IO.setmode (IO.BCM)            
IO.setup(4,IO.IN)                   
IO.setup(17,IO.IN)
IO.setup(27,IO.IN)
IO.setup(22,IO.IN)
IO.setup(5,IO.IN)
IO.setup(6,IO.IN)
IO.setup(13,IO.IN)
IO.setup(19,IO.IN)
while 1:
    if (IO.input(19) == True):
        time.sleep(0.001)
        if (IO.input(19) == True):
            b7=1                                      

    if (IO.input(13) == True):
        time.sleep(0.001)
        if (IO.input(13) == True):
            b6=1                                     

    if (IO.input(6) == True):
        time.sleep(0.001)
        if (IO.input(6) == True):
            b5=1                                     

    if (IO.input(5) == True):
        time.sleep(0.001)
        if (IO.input(5) == True):
            b4=1                                     

    if (IO.input(22) == True):
        time.sleep(0.001)
        if (IO.input(22) == True):
            b3=1                                     

    if (IO.input(27) == True):
        time.sleep(0.001)
        if (IO.input(27) == True):
            b2=1                                    
 
  if (IO.input(17) == True):
        time.sleep(0.001)
        if (IO.input(17) == True):
            b1=1                                    

    if (IO.input(4) == True):
        time.sleep(0.001)
        if (IO.input(4) == True):
            b0=1                                   
    
    x = (1*b0)+(2*b1)
    x = x+(4*b2)+(8*b3)
    x = x+(16*b4)+(32*b5)
    x = x+(64*b6)+(128*b7)                    
    print ('x = ')                                              
    b0=b1=b2=b3=b4=b5=b6=b7=0        
    time.sleep(1)                                   
