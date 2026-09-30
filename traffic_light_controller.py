import RPi.GPIO as GPIO
import time
from threading import Timer,Thread,Event

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


for i in range(1,13):
  GPIO.setup(i,GPIO.OUT)



green=[1,4,7,10]
yellow=[2,5,8,11]
red=[3,6,9,12]

count=1
Traffic_Sign_Now=1

class perpetualTimer():

   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
      self.thread.start()

   def cancel(self):
      self.thread.cancel()




 

def TrafficLight(ID,color,state):
 if color == "green" and state=="HIGH":
  GPIO.output(green[ID-1],GPIO.HIGH)
 elif color == "green" and state=="LOW":
  GPIO.output(green[ID-1],GPIO.LOW)
 elif color == "yellow" and state=="HIGH":
  GPIO.output(yellow[ID-1],GPIO.HIGH)
 elif color == "yellow" and state=="LOW":
  GPIO.output(yellow[ID-1],GPIO.LOW)
 elif color == "red" and state=="HIGH":
  GPIO.output(red[ID-1],GPIO.HIGH)
 elif color == "red" and state=="LOW":
  GPIO.output(red[ID-1],GPIO.LOW)

def All_Traffic_Off():
 for i in range (1,5):
  TrafficLight(i,"green","LOW")
  TrafficLight(i,"yellow","LOW")
  TrafficLight(i,"red","HIGH")
  
def Task_Traffic_Light():
 global count
 global Traffic_Sign_Now
 if count>=1 and count <= 20:
  TrafficLight(Traffic_Sign_Now,"green","HIGH")
  TrafficLight(Traffic_Sign_Now,"red","LOW")
  count=count+1
 elif count >=21 and count <=25:
  TrafficLight(Traffic_Sign_Now,"green","LOW")
  TrafficLight(Traffic_Sign_Now,"yellow","HIGH")
  count=count+1

 elif count> 25:
  TrafficLight(Traffic_Sign_Now,"green","LOW")
  TrafficLight(Traffic_Sign_Now,"yellow","LOW")
  TrafficLight(Traffic_Sign_Now,"red","HIGH")
  count=1
  Traffic_Sign_Now=Traffic_Sign_Now+1
  if Traffic_Sign_Now==5:
   Traffic_Sign_Now=1
  
  
All_Traffic_Off()
t = perpetualTimer(1,Task_Traffic_Light)
t.start()