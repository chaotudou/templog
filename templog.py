import time
import subprocess
from datetime import datetime

# open the file to write to
templog=open('kitchen','w')

#the main sensor reading loop
while True:
    sensor_reading=subprocess.getoutput("pcsensor")
    data=sensor_reading.split(' ')
    temp_only=str(data[4])
    temp=temp_only.rstrip('C')
    try:
        tempf=float(temp)
    except ValueError:
        continue
    if tempf==1.0:
        continue
    else:
        sensor_data=tempf
        thetime=datetime.now(tz=None)
        templog.write(str(thetime)+' '+str(sensor_data)+"\n")
        # delay between stream posts
        time.sleep(600)
