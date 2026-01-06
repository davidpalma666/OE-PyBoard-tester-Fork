
tutorial
https://www.kevsrobots.com/learn/micropython








**************************************************************************************************
OK  OK
# main.py -- put your code here!

# main.py -- put your code here!
from pyb import Pin, ADC, LED, UART, delay
import pyb
import select


# --- Setup ---
red_led = LED(1)  # Red LED
green_led = LED(2)  # Green LED
yellow_led = LED(3)  # Yellow LED
blue_led = LED(4)  # Blue LED
LEDs = [red_led,green_led,yellow_led,blue_led]


#blue_led.intensity(128) 



#generic IOs setup
X1=pyb.Pin(pyb.Pin.board.X1, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X2=pyb.Pin(pyb.Pin.board.X2, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X3=pyb.Pin(pyb.Pin.board.X3, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X4=pyb.Pin(pyb.Pin.board.X4, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X5=pyb.Pin(pyb.Pin.board.X5, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X6=pyb.Pin(pyb.Pin.board.X6, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X7=pyb.Pin(pyb.Pin.board.X7, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X8=pyb.Pin(pyb.Pin.board.X8, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X9=pyb.Pin(pyb.Pin.board.X9, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X10=pyb.Pin(pyb.Pin.board.X10, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X11=pyb.Pin(pyb.Pin.board.X11, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X12=pyb.Pin(pyb.Pin.board.X12, pyb.Pin.IN, pyb.Pin.PULL_DOWN)

Y1=Pin(Pin.board.Y1, Pin.IN, Pin.PULL_DOWN)
Y2=pyb.Pin(pyb.Pin.board.Y2, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y3=pyb.Pin(pyb.Pin.board.Y3, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y4=pyb.Pin(pyb.Pin.board.Y4, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y5=pyb.Pin(pyb.Pin.board.Y5, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y6=pyb.Pin(pyb.Pin.board.Y6, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y7=pyb.Pin(pyb.Pin.board.Y7, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y8=pyb.Pin(pyb.Pin.board.Y8, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y9=pyb.Pin(pyb.Pin.board.Y9, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y10=pyb.Pin(pyb.Pin.board.Y10, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y11=pyb.Pin(pyb.Pin.board.Y11, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y12=pyb.Pin(pyb.Pin.board.Y12, pyb.Pin.IN, pyb.Pin.PULL_DOWN)


IOs=[X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,
        Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10,Y11,Y12]


"""
with open('out.txt', 'w') as f:
    print('Hello there', file=f)

with open('out.txt', 'a') as f:
    print(k, file=f)
"""

#process cycle
yellow_led.on()
blue_led.off()


for k in range(23):
    #IOs setup & cycle
    IOs[k].init(Pin.OUT_PP)
    IOs[k].high()
    delay(500)

    IOs[k].init(IOs[k].IN, IOs[k].PULL_DOWN)
    delay(500)    

yellow_led.off()
blue_led.on()



# --- Main Loop ---
while False:

    #start processing
    yellow_led.off()
    blue_led.on()



    #IOs setup & cycle

    # for k in range(23):    
        # IOs[k].init(Pin.OUT_PP)
        # IOs[k].high()
        # delay(500)
        # IOs[k].init(IOs[k].IN, IOs[k].PULL_DOWN)
        # delay(500)    
    
    
    #end processing
    #blue_led.off()
    blue_led.off()
    yellow_led.on()
    
    delay(1000)







**************************************************************************************************
OK  OK


# main.py -- put your code here!
from pyb import Pin, ADC, LED, UART, delay
import pyb
import select


# --- Setup ---
red_led = LED(1)  # Red LED
green_led = LED(2)  # Green LED
yellow_led = LED(3)  # Yellow LED
blue_led = LED(4)  # Blue LED
LEDs = [red_led,green_led,yellow_led,blue_led]


#blue_led.intensity(128) 



#generic IOs setup
X1=pyb.Pin(pyb.Pin.board.X1, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X2=pyb.Pin(pyb.Pin.board.X2, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X3=pyb.Pin(pyb.Pin.board.X3, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X4=pyb.Pin(pyb.Pin.board.X4, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X5=pyb.Pin(pyb.Pin.board.X5, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X6=pyb.Pin(pyb.Pin.board.X6, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X7=pyb.Pin(pyb.Pin.board.X7, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X8=pyb.Pin(pyb.Pin.board.X8, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X9=pyb.Pin(pyb.Pin.board.X9, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X10=pyb.Pin(pyb.Pin.board.X10, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X11=pyb.Pin(pyb.Pin.board.X11, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X12=pyb.Pin(pyb.Pin.board.X12, pyb.Pin.IN, pyb.Pin.PULL_DOWN)

Y1=Pin(Pin.board.Y1, Pin.IN, Pin.PULL_DOWN)
Y2=pyb.Pin(pyb.Pin.board.Y2, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y3=pyb.Pin(pyb.Pin.board.Y3, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y4=pyb.Pin(pyb.Pin.board.Y4, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y5=pyb.Pin(pyb.Pin.board.Y5, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y6=pyb.Pin(pyb.Pin.board.Y6, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y7=pyb.Pin(pyb.Pin.board.Y7, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y8=pyb.Pin(pyb.Pin.board.Y8, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y9=pyb.Pin(pyb.Pin.board.Y9, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y10=pyb.Pin(pyb.Pin.board.Y10, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y11=pyb.Pin(pyb.Pin.board.Y11, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y12=pyb.Pin(pyb.Pin.board.Y12, pyb.Pin.IN, pyb.Pin.PULL_DOWN)


IOs=[X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,
        Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10,Y11,Y12]

k=1

with open('out.txt', 'w') as f:
    print('Hello there', file=f)

with open('out.txt', 'a') as f:
    print('Hello there 2', file=f)

with open('out.txt', 'a') as f:
    print(k, file=f)




# --- Main Loop ---     
while True:
    #start processing
    blue_led.on()
    
    #file output
    print(k, file=f)

    
    #IOs setup & cycle
    IOs[12].init(Pin.OUT_PP)
    IOs[12].high()
    delay(1000)
    #IOs[12].low()
    
    Y1.init(Y1.IN, Y1.PULL_DOWN)
    delay(1000)
    
    
    #end processing
    blue_led.off()
    delay(200)
    















**************************************************************************************************
OK  OK

# main.py -- put your code here!
from pyb import Pin, ADC, LED, UART, delay
import pyb
import select


# --- Setup ---
red_led = LED(1)  # Red LED
green_led = LED(2)  # Green LED
yellow_led = LED(3)  # Yellow LED
blue_led = LED(4)  # Blue LED
LEDs = [red_led,green_led,yellow_led,blue_led]


#blue_led.intensity(128) 



#generic IOs setup
X1=pyb.Pin(pyb.Pin.board.X1, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X2=pyb.Pin(pyb.Pin.board.X2, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X3=pyb.Pin(pyb.Pin.board.X3, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X4=pyb.Pin(pyb.Pin.board.X4, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X5=pyb.Pin(pyb.Pin.board.X5, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X6=pyb.Pin(pyb.Pin.board.X6, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X7=pyb.Pin(pyb.Pin.board.X7, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X8=pyb.Pin(pyb.Pin.board.X8, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X9=pyb.Pin(pyb.Pin.board.X9, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X10=pyb.Pin(pyb.Pin.board.X10, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X11=pyb.Pin(pyb.Pin.board.X11, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X12=pyb.Pin(pyb.Pin.board.X12, pyb.Pin.IN, pyb.Pin.PULL_DOWN)

Y1=Pin(Pin.board.Y1, Pin.IN, Pin.PULL_DOWN)
Y2=pyb.Pin(pyb.Pin.board.Y2, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y3=pyb.Pin(pyb.Pin.board.Y3, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y4=pyb.Pin(pyb.Pin.board.Y4, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y5=pyb.Pin(pyb.Pin.board.Y5, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y6=pyb.Pin(pyb.Pin.board.Y6, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y7=pyb.Pin(pyb.Pin.board.Y7, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y8=pyb.Pin(pyb.Pin.board.Y8, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y9=pyb.Pin(pyb.Pin.board.Y9, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y10=pyb.Pin(pyb.Pin.board.Y10, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y11=pyb.Pin(pyb.Pin.board.Y11, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y12=pyb.Pin(pyb.Pin.board.Y12, pyb.Pin.IN, pyb.Pin.PULL_DOWN)


IOs=[X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,
        Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10,Y11,Y12]

k=1



with open('out.txt', 'w') as f:
    print('Hello there', file=f)

with open('out.txt', 'a') as f:
    print('Hello there 2', file=f)

with open('out.txt', 'a') as f:
    print(k, file=f)

# --- Main Loop ---     
while True:
    #start processing
    blue_led.on()
    
    #file output

    
    #IOs setup & cycle
    IOs[12].init(Pin.OUT_PP)
    IOs[12].high()
    delay(1000)
    #IOs[12].low()
    
    Y1.init(Y1.IN, Y1.PULL_DOWN)
    delay(1000)
    
    
    #end processing
    blue_led.off()
    delay(200)
    




 **************************************************************************************************
OK  OK

k=10

with open('out.txt','w') as f:
    print('Hello world', file=f)
    print(k+1,file=f)

# --- Main Loop ---
while True:
    #blue on: test starting
    blue_led.on()
    
    #file writing

    
    # IO redefined as output & setted high
    IOs[12].init(Pin.OUT_PP)
    IOs[12].high()
    delay(1000)
    
    # IO redefined as input & setted PDown
    IOs[12].init(IOs[12].IN, IOs[12].PULL_DOWN)
    delay(1000)
    
    
    #blue off: test ended
    blue_led.off()
    delay(200)
    





**************************************************************************************************
?????????????????????


# --- Setup ---
red_led = LED(1)  # Red LED
green_led = LED(2)  # Green LED
yellow_led = LED(3)  # Yellow LED
blue_led = LED(4)  # Blue LED
LEDs = [red_led,green_led,yellow_led,blue_led]


#blue_led.intensity(128) 




#generic IOs setup
X1=pyb.Pin(pyb.Pin.board.X1, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X2=pyb.Pin(pyb.Pin.board.X2, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X3=pyb.Pin(pyb.Pin.board.X3, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X4=pyb.Pin(pyb.Pin.board.X4, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X5=pyb.Pin(pyb.Pin.board.X5, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X6=pyb.Pin(pyb.Pin.board.X6, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X7=pyb.Pin(pyb.Pin.board.X7, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X8=pyb.Pin(pyb.Pin.board.X8, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X9=pyb.Pin(pyb.Pin.board.X9, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X10=pyb.Pin(pyb.Pin.board.X10, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X11=pyb.Pin(pyb.Pin.board.X11, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
X12=pyb.Pin(pyb.Pin.board.X12, pyb.Pin.IN, pyb.Pin.PULL_DOWN)

Y1=Pin(Pin.board.Y1, Pin.IN, Pin.PULL_DOWN)
Y2=pyb.Pin(pyb.Pin.board.Y2, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y3=pyb.Pin(pyb.Pin.board.Y3, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y4=pyb.Pin(pyb.Pin.board.Y4, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y5=pyb.Pin(pyb.Pin.board.Y5, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y6=pyb.Pin(pyb.Pin.board.Y6, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y7=pyb.Pin(pyb.Pin.board.Y7, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y8=pyb.Pin(pyb.Pin.board.Y8, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y9=pyb.Pin(pyb.Pin.board.Y9, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y10=pyb.Pin(pyb.Pin.board.Y10, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y11=pyb.Pin(pyb.Pin.board.Y11, pyb.Pin.IN, pyb.Pin.PULL_DOWN)
Y12=pyb.Pin(pyb.Pin.board.Y12, pyb.Pin.IN, pyb.Pin.PULL_DOWN)


IOs=[X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,
        Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10,Y11,Y12]
        
        
        
        
        





 

**************************************************************************************************
OK  OK

# --- Main Loop ---

while True:
    #blue on: test starting
    blue_led.on()
    
    # IO redefined as output & setted high
    IOs[12].init(Pin.OUT_PP)
    IOs[12].high()
    delay(1000)
    
    # IO redefined as input & setted PDown
    IOs[12].init(IOs[12].IN, IOs[12].PULL_DOWN)
    delay(1000)
    
    
    #blue off: test ended
    blue_led.off()
    delay(200)
    








**************************************************************************************************
OK  OK
# --- Main Loop ---

while True:
    blue_led.on()
    
    IOs[12].init(Pin.OUT_PP)
    IOs[12].high()
    delay(1000)
    #IOs[12].low()
    
    IOs[12].init(IOs[12].IN, IOs[12].PULL_DOWN)
    delay(1000)
    
    
    
    
    
    delay(200)
    blue_led.off()
    delay(200)
 

    

**************************************************************************************************
OK  OK
# --- Main Loop ---     

while True:
    blue_led.on()
    
    IOs[12].init(Pin.OUT_PP)
    IOs[12].high()
    delay(1000)
    #IOs[12].low()
    
    Y1.init(Y1.IN, Y1.PULL_DOWN)
    delay(1000)
    
    delay(200)
    blue_led.off()
    delay(200)
    
