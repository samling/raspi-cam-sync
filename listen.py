from picamera import PiCamera
import pigpio
import RPi.GPIO as GPIO
import time

camera = PiCamera()
camera.resolution = (640, 480)
INPUT_PIN=11
pi = pigpio.pi('localhost')

def handler(pin):
    millis=int(round(time.time() * 1000))
    camera.capture("%s.jpg" % millis)
    print("Change detected in pin", INPUT_PIN)
    print(millis)

def main():
    camera.start_preview()
    print("Warming up camera...")
    time.sleep(2)

    for g in range(0,32):
        print("gpio {} is {}".format(g, pi.read(g)))

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(INPUT_PIN,GPIO.IN)

    GPIO.add_event_detect(INPUT_PIN,GPIO.BOTH)
    GPIO.add_event_callback(INPUT_PIN, handler)

    while True:
        print("Waiting for input from pin", INPUT_PIN)
        time.sleep(1)

    GPIO.cleanup()

if __name__=="__main__":
    main()
