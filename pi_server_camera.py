#!/usr/bin/env python
# -*- coding: cp1252 -*-
import socket
import os
import subprocess
import RPi.GPIO as GPIO
import time
from sensor import distance
from socket import AF_INET, SOCK_STREAM
HOST = '' 
PORT = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(PORT)



def stopcar(x):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    mode=GPIO.getmode()

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(29,GPIO.OUT)
    GPIO.setup(31,GPIO.OUT)
    GPIO.setup(33,GPIO.OUT)
    GPIO.setup(37,GPIO.OUT)
  

    GPIO.output(29,False)
    GPIO.output(31,False)
    GPIO.output(33,False)
    GPIO.output(37,False)
    time.sleep(x)
    GPIO.cleanup()






def forwardcar(x):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    mode=GPIO.getmode()

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(29,GPIO.OUT)
    GPIO.setup(31,GPIO.OUT)
    GPIO.setup(33,GPIO.OUT)
    GPIO.setup(37,GPIO.OUT)
  

    GPIO.output(29,True)
    GPIO.output(31,False)
    GPIO.output(33,True)
    GPIO.output(37,False)
    time.sleep(x)
    GPIO.cleanup()



def reversecar(x):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    mode=GPIO.getmode()

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(29,GPIO.OUT)
    GPIO.setup(31,GPIO.OUT)
    GPIO.setup(33,GPIO.OUT)
    GPIO.setup(37,GPIO.OUT)
 
    
    GPIO.output(29,False)
    GPIO.output(31,True)
    GPIO.output(33,False)
    GPIO.output(37,True)
    time.sleep(x)
    GPIO.cleanup()

def leftcar(x):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    mode=GPIO.getmode()

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(29,GPIO.OUT)
    GPIO.setup(31,GPIO.OUT)
    GPIO.setup(33,GPIO.OUT)
    GPIO.setup(37,GPIO.OUT)
 
 
    GPIO.output(29,False)
    GPIO.output(31,False)
    GPIO.output(33,False)
    GPIO.output(37,True)
    time.sleep(x)
    GPIO.cleanup()

def rightcar(x):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    mode=GPIO.getmode()

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(29,GPIO.OUT)
    GPIO.setup(31,GPIO.OUT)
    GPIO.setup(33,GPIO.OUT)
    GPIO.setup(37,GPIO.OUT)
 

    GPIO.output(29,False)
    GPIO.output(31,True)
    GPIO.output(33,False)
    GPIO.output(37,False)
    time.sleep(x)
    GPIO.cleanup()





def right():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setwarnings(False)
    pwm = GPIO.PWM(18,50)
    pwm.start(7.5)
    for i in range(180,0,-1):
        DC =1./20.*(i)+2
        pwm.ChangeDutyCycle(DC)
        time.sleep(0.05)
    GPIO.cleanup()


def gun_right():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setwarnings(False)
    pwm = GPIO.PWM(16,50)
    pwm.start(7.5)
    for i in range(180,0,-1):
        DC =1./20.*(i)+2
        pwm.ChangeDutyCycle(DC)
        time.sleep(0.05)
    GPIO.cleanup()



def left():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setwarnings(False)
    pwm = GPIO.PWM(18,50)
    pwm.start(7.5)
  
    for i in range(0,180):
        DC =1./20.*(i)+2
        pwm.ChangeDutyCycle(DC)
        time.sleep(0.05)
    GPIO.cleanup()

def gun_left():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setwarnings(False)
    pwm = GPIO.PWM(16,50)
    pwm.start(7.5)
  
    for i in range(0,180):
        DC =1./20.*(i)+2
        pwm.ChangeDutyCycle(DC)
        time.sleep(0.05)
    GPIO.cleanup()




def mid():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setwarnings(False)
    pwm = GPIO.PWM(18,50)
    pwm.start(7.5)
  
    for i in range(0,180):
        DC = 7.5
        pwm.ChangeDutyCycle(DC)
        time.sleep(0.05)
    GPIO.cleanup()

def gun_mid():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setwarnings(False)
    pwm = GPIO.PWM(16,50)
    pwm.start(7.5)
  
    for i in range(0,180):
        DC = 7.5
        pwm.ChangeDutyCycle(DC)
        time.sleep(0.05)
    GPIO.cleanup()




def cam():
    proc = subprocess.Popen(['sudo service motion start'], shell=True)
    broc = subprocess.Popen(['sudo motion'], shell=True)


while True:
    print('listening to client...')

    cam()
    
    conn, addr = s.accept()
    data=conn.recv(1024)
    print(data)
    parseData=data.decode('utf8').split("|")
    
    if (parseData[0]=="forward"):
        reply="forward"
        conn.sendall(reply.encode())
        conn.close()


        #coding for forward button goes here

        forwardcar(2)
        



        
    elif(parseData[0]=="back"):
        reply="back"
        conn.sendall(reply.encode())
        conn.close()


        #coding for back button goes here

        reversecar(2)


        
    elif(parseData[0]=="left"):
        reply="left"
        conn.sendall(reply.encode())
        conn.close()



        #coding for left button goes here


        leftcar(2)


        

        
    elif(parseData[0]=="right"):
        reply="right"
        conn.sendall(reply.encode())
        conn.close()


        #coding for right button goes here


        rightcar(2)


        
    elif(parseData[0]=="camera"):


        #coding for getting the ip for camera goes here and return it in reply variable


        reply="http://192.168.0.106:8081/" #this reply variable needs to be changed with camera 1 ip
        conn.sendall(reply.encode())
        conn.close()
    elif(parseData[0]=="MoveCameraToLeft"):
        reply="cameraLeft"
        conn.sendall(reply.encode())
        conn.close()


        #coding for moving camera left goes here

        left()




        
    elif(parseData[0]=="MoveCameraToMiddle"):
        reply="cameraMiddle"
        conn.sendall(reply.encode())
        conn.close()



        #coding for moving camera middle goes here

        mid()




        
    elif(parseData[0]=="MoveCameraToRight"):
        reply="cameraRight"
        conn.sendall(reply.encode())
        conn.close()




        #coding for moving camera right goes here

        right()




        
    elif(parseData[0]=="MoveGunToLeft"):
        reply="gunLeft"
        conn.sendall(reply.encode())
        conn.close()



        #coding for moving gun left goes here


        gun_left()


        
    elif(parseData[0]=="MoveGunToMiddle"):
        reply="gunMiddle"
        conn.sendall(reply.encode())
        conn.close()



        #coding for moving gun middle goes here

        gun_mid()





        
    elif(parseData[0]=="MoveGunToRight"):
        reply="gunRight"
        conn.sendall(reply.encode())
        conn.close()



        #coding for moving gun right goes here


        gun_right()

    else:
        pass

    curDis = distance('cm')
    print('curdis is',curDis)
    if curDis < 4:
        reversecar(0.5)



    
