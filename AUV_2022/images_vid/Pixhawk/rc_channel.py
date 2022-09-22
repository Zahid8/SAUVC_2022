# Import mavutil
from pymavlink import mavutil

# Create the connection
master = mavutil.mavlink_connection("/dev/ttyACM0", baud=57600)
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# Create a function to send RC values
# More information about Joystick channels
# here: https://www.ardusub.com/operators-manual/rc-input-and-output.html#rc-inputs
def set_rc_channel_pwm(channel_id, pwm=1500):
    """ Set RC channel pwm value
    Args:
        channel_id (TYPE): Channel ID
        pwm (int, optional): Channel pwm value 1100-1900
    """
    if channel_id < 1 or channel_id > 18:
        print("Channel does not exist.")
        return

    # Mavlink 2 supports up to 18 channels:
    # https://mavlink.io/en/messages/common.html#RC_CHANNELS_OVERRIDE
    rc_channel_values = [65535 for _ in range(18)]
    rc_channel_values[channel_id - 1] = pwm
    master.mav.rc_channels_override_send(
        master.target_system,                # target_system
        master.target_component,             # target_component
        *rc_channel_values)                  # RC channel list, in microseconds.


# Set some roll
# set_rc_channel_pwm(2, 1500)
while (2<3):
	set_rc_channel_pwm(3, 1700)   # 1,2 lEFT RIGHT
#set_rc_channel_pwm(3, 1550)   # Move Forward/ Backword
#set_rc_channel_pwm(3, 1600)

#set_rc_channel_pwm(1, 1500)  # 5->1100  pITCH
#set_rc_channel_pwm(2, 1500)   # 3,4,6
#set_rc_channel_pwm(3, 1500)  # 5-> 1900






# Set some yaw
# set_rc_channel_pwm(4, 1600)

# # The camera pwm value sets the servo speed of a sweep from the current angle to
# #  the min/max camera angle. It does not set the servo position.
# # Set camera tilt to 45º (max) with full speed
# set_rc_channel_pwm(8, 1900)

# # Set channel 12 to 1500us
# # This can be used to control a device connected to a servo output by setting the
# # SERVO[N]_Function to RCIN12 (Where N is one of the PWM outputs)
# set_rc_channel_pwm(12, 1500)
