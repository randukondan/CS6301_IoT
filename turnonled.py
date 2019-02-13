import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.IN)
try:
	GPIO.output(20,GPIO.HIGH);
	while(GPIO.input(16)):
		GPIO.output(21,GPIO.LOW);
except:
	GPIO.cleanup();
