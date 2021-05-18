#Libraries
import RPi.GPIO as GPIO
import time
import pyrebase
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
 
#set GPIO Pins
GPIO_TRIGGER = 16
GPIO_ECHO = 18
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

config = {
  "apiKey": "nOMe92cdX2LXQ1uXywPrxvYvZisJUvW06B6l83LD",
  "authDomain": "doorbell-308316.firebaseapp.com",
  "databaseURL": "https://doorbell-308316-default-rtdb.firebaseio.com",
  "storageBucket": "doorbell-308316.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
 
 
def distance():
   #set the trigger to HIGH
    GPIO.output(GPIO_TRIGGER, GPIO.HIGH)
    #sleep 0.00001 s and the set the trigger to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, GPIO.LOW)

    #save the start and stop times
    start = time.time()
    stop = time.time()
    #modify the start time to be the last time until #the echo becomes HIGH
    while GPIO.input(GPIO_ECHO) == 0:

           start = time.time()
    #modify the stop time to be the last time until #the echo becomes LOW
    while GPIO.input(GPIO_ECHO) == 1:

           stop = time.time()
    #get the duration of the echo pin as HIGH

    duration = stop - start
    #calculate the distance
    distance = 34300/2 * duration

    #the reading can be erroneous, and we will print
    #the distance only if it is lower than the specified value
    
    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            if dist < 3400:
                print ("Measured Distance = %.1f cm" % dist)
            
            data = {
              "distance": dist
            }
            db.child("Distance").push(data)
            time.sleep(3)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()