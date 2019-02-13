# CS6301_IoT

Connect pins as per the code.


**pir.py** is to test the PIR, code directly from the manual.

**relaytest.py** switches on and off the LED at a specific frequency.

**pirlight.py** switches on the LED for a specific time when motion is detected and then waits for the next instance of motion.  
*For pirlight.py:  
The input pin is the connection from the PIR sensor.  
The output pin is the connection to the relay.*

To run speech file on ubuntu machine
sudo apt-get install libportaudio-dev
sudo apt-get install python-dev
sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
git clone http://people.csail.mit.edu/hubert/git/pyaudio.git
cd pyaudio
sudo python setup.py install
sudo pip3 install SpeechRecognition
