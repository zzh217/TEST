import threading  
import time
def function(a):
    for i in range(1,10):
      print 3 
      print a
      print("`````````````````````````````````")
      time.sleep(3)
def running(x, y):  
    for i in range(x, y):  
        print (i) 
        print("!!!!!!!!!!!!")
        time.sleep(1)
for i in range(3): 
        t1 = threading.Thread(target=running, args=(1 * i, 10 * (i + 1)))  
        t2 = threading.Thread(target=function, args=("1"))  
        t2.start()
        t1.start()
        t2.join() 
        t1.join() 
        
