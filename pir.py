import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN)

try:
	time.sleep(2)
	while True:
		if GPIO.input(21):
			print("Motion Detected!")
			time.sleep(2)
		time.sleep(0.1)

except:
	GPIO.cleanup()
