import RPi.GPIO as GPIO
from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def index():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(12, GPIO.OUT)

    p = GPIO.PWM(12, 50)

    p.start(7.5)

    p.ChangeDutyCycle(7.5) # turn towards 90 degree
    time.sleep(1) # sleep 1 second
    p.ChangeDutyCycle(5) # turn towards 0 degree
    time.sleep(0.4) # sleep 1 second
    p.ChangeDutyCycle(7.5) # turn towards 90 degree
    time.sleep(1) # sleep 1 second

    p.stop()
    GPIO.cleanup()
    
    return 'Hello world'
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='42069')