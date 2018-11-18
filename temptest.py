import subprocess

while True:
    # read data from temper usb sensor
    sensor_reading=subprocess.getoutput("pcsensor")

    #extract single temperature reading from the sensor

    data=sensor_reading.split(' ') #Split the string and define temperature
    temp_only=str(data[4]) #knocks out celcius reading from line
    temp=temp_only.rstrip('C') #Removes the character "C" from the string to allow for plotting

    # calibrate temperature reading
    temp_C = temp

    # convert regular error message to number
    if temp_C == "temporarily":
            temp_C = 0.0

    # convert value to float
    try:
    	temp_C = float(temp_C)
    except ValueError:
    	continue # skips to next iteration

    # check to see if non-float
    check = isinstance(temp_C, float)

    #write out 0.0 as a null value if non-float
    if check == True:
            temp_C = temp_C
    else:
            temp_C = 0.0

    print (temp_C)
