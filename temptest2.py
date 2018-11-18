import subprocess
import time

while True:
    sensor_reading=subprocess.getoutput("pcsensor")
    data=sensor_reading.split(' ') #Split the string and define temperature
    temp_only=str(data[4]) #knocks out celcius reading from line
    temp=temp_only.rstrip('C') #Removes the character "C" from the string to allow for plotting
    try:
    	tempf = float(temp)
    except ValueError:
    	continue # skips to next iteration
    print (tempf)
    time.sleep(5)
