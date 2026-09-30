import serial
import cv2
import time
import socket
import time

host = '192.168.43.109'
port = 5560


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate
count =0
color="undefined"

def Clock_Wise():
 global count
 count=0
 while(count<255):
                
                GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.LOW))
                sleep(0.005)
                GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
                sleep(0.005)
                GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.LOW))
                sleep(0.005)
                GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
                sleep(0.005)
                
                count=count+1
  


def Anti_Clock_Wise():
 global count
 count=0
 while(count<255):
            GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
            sleep(0.005)
            GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
            sleep(0.005)
            GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
            sleep(0.005)
            GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
            sleep(0.005)
            count+=1

def Half_Clock_Wise():
 global count
 count=0
 while(count<131):
                GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.LOW))
                sleep(0.005)
                GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
                sleep(0.005)
                GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.LOW))
                sleep(0.005)
                GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
                sleep(0.005)
                
                count=count+1


def Quarter_Clock_Wise():
 global count
 count=0
 while(count<72):
                GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.LOW))
                sleep(0.005)
                GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
                sleep(0.005)
                GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.LOW))
                sleep(0.005)
                GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
                sleep(0.005)
                
                count=count+1
def Half_Anti_Clock_Wise():
 global count
 count=0
 while(count<131):
            GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
            sleep(0.005)
            GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
            sleep(0.005)
            GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
            sleep(0.005)
            GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
            sleep(0.005)
            count+=1



def Quarter_Anti_Clock_Wise():
 global count
 count=0
 while(count<72):
            GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
            sleep(0.005)
            GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
            sleep(0.005)
            GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
            sleep(0.005)
            GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
            sleep(0.005)
            count+=1



def Back():
 Clock_Wise()
 time.sleep(5)
 Anti_Clock_Wise()

def Right():
 Half_Clock_Wise()
 time.sleep(3)
 Half_Anti_Clock_Wise()
 

def Left():
 Half_Anti_Clock_Wise()
 time.sleep(3)
 Half_Clock_Wise()
  
def F_R():
 Quarter_Clock_Wise()
 time.sleep(5)
 Quarter_Anti_Clock_Wise()

def F_L():
 Quarter_Anti_Clock_Wise()
 time.sleep(5)
 Quarter_Clock_Wise()
 

def B_R():
 Half_Clock_Wise()
 Quarter_Clock_Wise()
 time.sleep(5)
 Quarter_Anti_Clock_wiseClock_Wise()

 Half_Anti_Clock_Wise()
 
  

def B_L():
 Half_Anti_Clock_wiseClock_Wise()
 Quarter_Anti_Clock_wiseClock_Wise()
 time.sleep(5)
 Quarter_Clock_wiseClock_Wise()

 Half_Clock_Wise()
 









def detect_color(cap):
    LIMIT = 10
    start = time.time()
    while time.time() - start <= LIMIT:
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        height, width, _ = frame.shape

        cx, cy = int(width / 2), int(height / 2)

        pixel_center = hsv_frame[cy, cx]
        hue_value, sat_value, val_value = pixel_center

        color = "Undefined"
        if hue_value < 5:
            color = "RED"
        elif sat_value <= 10 and val_value <= 255:
            color = "WHITE"
        elif val_value <= 50:
            color = "BLACK"
        elif hue_value < 22:
            color = "ORANGE"
        elif hue_value < 33:
            color = "YELLOW"
        elif hue_value < 78:
            color = "GREEN"
        elif hue_value < 131:
            color = "BLUE"
        elif hue_value < 170:
            color = "VIOLET"

        else:
            color = "RED"

        pixel_center_bgr = frame[cy, cx]
        b, g, r = [int(i) for i in pixel_center_bgr]

        #cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
        #cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)

        cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break


capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)


while True:
    detect_color(capture)
    received_data = ser.read()              #read serial port
    sleep(0.03)
    if(received_data):
    
     data_left = ser.inWaiting()             #check for remaining byte
     received_data += ser.read(data_left)
     received_data=received_data.decode()
     
     if(received_data==0):     #go
          command = 'GET'
  
          s.send(str.encode(command))
          reply = s.recv(1024)
          reply=reply.decode('utf-8')
          time.sleep(0.3)
          if(reply)
      
     
     elif(received_data==1):  #BACK 
      BACK()
     elif(received_data==2):   #RIGHT
      RIGHT()
     elif(received_data==3):   #left
      Left()
     elif(received_data==4):   #f_r
      F_R() 
     
     elif(received_data==5):   #f_l
      F_L()
     elif(received_data==6):    #B_r
      B_R()
     elif(received_data==7):   #B_l
      B_l()
capture.release()
cv2.destroyAllWindows()



'''

import serial
import time

ser = serial.Serial ("/dev/ttyS0", 9600)    
while True:
    data=48
    
    #data=data.encode()
    ser.write(chr(data).encode())
    time.sleep(0.5)
'''
'''
import serial
from time import sleep

ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate
while True:

    received_data = ser.read()              #read serial port
    sleep(0.03)
    if(received_data):
     data_left = ser.inWaiting()             #check for remaining byte
     received_data += ser.read(data_left)
     print (received_data.decode())                   #print received data
     
'''