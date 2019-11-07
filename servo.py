import RPi.GPIO as GPIO
from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def index():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(10, GPIO.OUT)

    GPIO.output(10, HIGH)

    GPIO.setup(12, GPIO.OUT)

    p = GPIO.PWM(12, 50)

    p.start(10)

    p.ChangeDutyCycle(10) # turn towards 90 degree
    time.sleep(1) # sleep 1 second
    p.ChangeDutyCycle(5) # turn towards 0 degree
    time.sleep(0.4) # sleep 1 second
    p.ChangeDutyCycle(10) # turn towards 90 degree
    time.sleep(1) # sleep 1 second

    GPIO.output(10, LOW)


    p.stop()
    GPIO.cleanup()
    
    return 'started pc'

@app.route('/reset')
def reset():
    GPIO.setmode(GPIO.BOARD)

    
    GPIO.setup(10, GPIO.OUT)

    GPIO.output(10, HIGH)

    GPIO.setup(12, GPIO.OUT)

    p = GPIO.PWM(12, 50)

    p.start(10)
    p.ChangeDutyCycle(8.5)
    time.sleep(1)
    p.ChangeDutyCycle(10)
    time.sleep(1)

    GPIO.output(10, LOW)

    p.stop()
    GPIO.cleanup()

    return 'servo reset'
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='42069')
