#!/usr/bin/env python3                                                                                

import speech_recognition as sr  
import sys, paramiko
from multiprocessing import Process




turnOn = "python /home/pi/CS6301_IoT/turnonled.py"
turnOf = "python /home/pi/CS6301_IoT/turnoffled.py"

client = None
def invokePi(command):
    try:
        username = "pi"
        password = "raspberry"
        port = 22
        hostname = "group1.local"
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy)
        
        client.connect(hostname, port=port, username=username, password=password)

        stdin, stdout, stderr = client.exec_command(command)
        for line in stdout:
            print(line.rstrip())
        for line in stderr:
            print(line.rstrip())

    finally:
        client.close()
    
    return

# get audio from the microphone         
listen = True
command = None
lastProcess = None
r = sr.Recognizer()
while (listen): 
    #global lastProcess                                                                  
    with sr.Microphone() as source:                                                                       
        print("Speak now: ")                                                                                   
        audio = r.listen(source)   

    try:
        input = r.recognize_google(audio)
        print(input)
        if(input == "exit"):
            if lastProcess:
                lastProcess.terminate()
            listen = False
            
        elif input == "turn on the light":
            if lastProcess:
                lastProcess.terminate()
            command = turnOn
            lastProcess = Process(target=invokePi, args=(command,))
            lastProcess.start()
            
        elif input == "turn off the light":
            if lastProcess:
                lastProcess.terminate()
            command = turnOf
            lastProcess = Process(target=invokePi, args=(command,))
            lastProcess.start()
        else:
            print("Bad input try again")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

if lastProcess:
    lastProcess.terminate()
print("Exited")
