import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.IN)
GPIO.setup(21, GPIO.OUT)

try:
	time.sleep(3);
	while True:
		if GPIO.input(14): 
			GPIO.output(21,GPIO.HIGH);
			time.sleep(2);
			GPIO.output(21,GPIO.LOW);

except:
	GPIO.cleanup();
