# Import mavutil
#from pymavlink import mavutil

# Create the connection
# Need to provide the serial port and baudrate
#master = mavutil.mavlink_connection('udpout:localhost:14550', source_system=1)-#master#mavutil.mavlink_connection("/dev/ttyACM0", baud=57600)
#mavutil.mavlink_connection('udpout:192.168.43.54:14550')
# Restart the ArduSub board !
#master.reboot_autopilot()
#print("connected")

import time
# Import mavutil
from pymavlink import mavutil

def wait_conn():
    """
    Sends a ping to stabilish the UDP communication and awaits for a response
    """
    msg = None
    while not msg:
        master.mav.ping_send(
            int(time.time() * 1e6), # Unix time in microseconds
            0, # Ping number
            0, # Request ping of all systems
            0 # Request ping of all components
        )
        msg = master.recv_match()
        time.sleep(0.5)

# Create the connection
#  Companion is already configured to allow script connections under the port 9000
# Note: The connection is done with 'udpout' and not 'udpin'.
#  You can check in http:192.168.1.2:2770/mavproxy that the communication made for 9000
#  uses a 'udp' (server) and not 'udpout' (client).
master = mavutil.mavlink_connection('udpout:192.168.1.100:14550')

# Send a ping to start connection and wait for any reply.
#  This function is necessary when using 'udpout',
#  as described before, 'udpout' connects to 'udpin',
#  and needs to send something to allow 'udpin' to start
#  sending data.
wait_conn()

# Get some information !
while True:
    try:
        print(master.recv_match().to_dict())
    except:
        pass
    time.sleep(0.1)

