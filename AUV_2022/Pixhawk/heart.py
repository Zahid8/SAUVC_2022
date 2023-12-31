
from pymavlink import mavutil
import serial
import time
master= mavutil.mavlink_connection("/dev/ttyACM0", baud=57600)
master.wait_heartbeat()


def arm():
    master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1, 0, 0, 0, 0, 0, 0)
    # # wait until arming confirmed (can manually check with master.motors_armed())
    print("Waiting for the vehicle to arm")
    master.motors_armed_wait()
    print('Armed!')


arm()

while True:
    MAVLink.heartbeat_send()
    time.sleep(0.5)
	
