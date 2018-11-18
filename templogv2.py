import time
import subprocess
from datetime import datetime

# ask user to name and create a file
#file=input("Where are you measuring temperature?")
file=str("kitchen")
templog=open(file,'w')

# how long to record temperatures for
#days=input("How long to record temperature for (days)?")
days=2
days=float(days)

# sampling interval for temperatures
#delay=input("How long to delay between temperature readings (seconds)?")
delay=600
delay=float(delay)

# limit the script to the defined time period
secday=float(24*60*60)
incre=secday/delay
period=secday*days
current=float(0)

# the main sensor reading loop
while current<period:
    try:
        tempf=float(str(((subprocess.getoutput("pcsensor")).split(' '))[4]).rstrip('C'))
    except ValueError:
        continue
    if tempf==1.0:
        continue
    else:
        templog.write(str(datetime.now(tz=None))+' '+str(tempf)+"\n")
        print(tempf)
        current=current+delay
        # delay between temperature readings
        time.sleep(delay)
templog.close()
