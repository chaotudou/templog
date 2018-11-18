import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure
import time
import subprocess
from datetime import datetime
from signal import signal, SIGPIPE, SIG_DFL 

username = 'tudou'
api_key = '1fby1hgodx'
stream_token = 'lvzad24rmt'

py.sign_in(username, api_key)

trace1 = Scatter(
    x=[],
    y=[],
    stream=dict(
        token=stream_token,
        maxpoints=1000
    )
)

layout = Layout(
    title=''
)

fig = Figure(data=[trace1], layout=layout)

print(py.plot(fig, filename='Lounge Temperature Data'))

# initialize the stream
stream = py.Stream(stream_token)
stream.open()

#open file to backing up data
#f=open("lounge","w")

#the main sensor reading loop
while True:
    signal(SIGPIPE,SIG_DFL) 
    sensor_reading=subprocess.getoutput("pcsensor")
    data=sensor_reading.split(' ')
    temp_only=str(data[4])
    temp=temp_only.rstrip('C')
    try:
        tempf=float(temp)
    except ValueError:
        continue
    sensor_data=tempf
    thetime=datetime.now(tz=None)
    stream.write({'x':thetime,'y':sensor_data})
    #write out data to file for archiving
    #f.write('thetime'+' '+'sensor_data'+"\n")
    # delay between stream posts
    time.sleep(300)
