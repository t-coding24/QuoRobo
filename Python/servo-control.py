import webiopi
import time
import wiringpi2 as wiringpi
 
SERVO_PAN  = 17
SERVO_TILT = 18
 
# SERVO_PAN  (Left)90 ... 0 ... -90(Right)
# SERVO_TILT (Down)90 ... 0 ... -90(UP)
SERVO_PAN_TRIM  = 12 # degree
SERVO_TILT_TRIM =  0 # degree
 
SERVO_PAN_LEFT_LIMIT  =  60 # degree
SERVO_PAN_RIGHT_LIMIT = -60 # degree
SERVO_TILT_DOWN_LIMIT =  40 # degree
SERVO_TILT_UP_LIMIT   = -40 # degree
 
##### SERVO SPECIFICATION #####
SERVO_ANGLE_MIN = -90 # degree
SERVO_ANGLE_MAX =  90 # degree
SERVO_PULSE_MIN = 0.5 # ms
SERVO_PULSE_MAX = 2.4 # ms
SERVO_CYCLE     =  20 # ms
###############################
 
#### WIRINGPI SPECIFICATION ####
PWM_WRITE_MIN = 0
PWM_WRITE_MAX = 1024
################################
 
SERVO_DUTY_MIN = SERVO_PULSE_MIN/SERVO_CYCLE
SERVO_DUTY_MAX = SERVO_PULSE_MAX/SERVO_CYCLE
 
SERVO_PAN_DUTY_MIN  =  (SERVO_DUTY_MAX - SERVO_DUTY_MIN) / (SERVO_ANGLE_MAX - SERVO_ANGLE_MIN) * ((SERVO_PAN_LEFT_LIMIT +SERVO_PAN_TRIM)  - SERVO_ANGLE_MIN) + SERVO_DUTY_MIN
SERVO_PAN_DUTY_MAX  =  (SERVO_DUTY_MAX - SERVO_DUTY_MIN) / (SERVO_ANGLE_MAX - SERVO_ANGLE_MIN) * ((SERVO_PAN_RIGHT_LIMIT+SERVO_PAN_TRIM)  - SERVO_ANGLE_MIN) + SERVO_DUTY_MIN
SERVO_TILT_DUTY_MIN =  (SERVO_DUTY_MAX - SERVO_DUTY_MIN) / (SERVO_ANGLE_MAX - SERVO_ANGLE_MIN) * ((SERVO_TILT_DOWN_LIMIT+SERVO_TILT_TRIM) - SERVO_ANGLE_MIN) + SERVO_DUTY_MIN
SERVO_TILT_DUTY_MAX =  (SERVO_DUTY_MAX - SERVO_DUTY_MIN) / (SERVO_ANGLE_MAX - SERVO_ANGLE_MIN) * ((SERVO_TILT_UP_LIMIT  +SERVO_TILT_TRIM) - SERVO_ANGLE_MIN) + SERVO_DUTY_MIN
 
SERVO_PAN_PWM_WRITE_MIN  = PWM_WRITE_MAX * SERVO_PAN_DUTY_MIN
SERVO_PAN_PWM_WRITE_MAX  = PWM_WRITE_MAX * SERVO_PAN_DUTY_MAX
SERVO_TILT_PWM_WRITE_MIN = PWM_WRITE_MAX * SERVO_TILT_DUTY_MIN
SERVO_TILT_PWM_WRITE_MAX = PWM_WRITE_MAX * SERVO_TILT_DUTY_MAX
 
def getServoPanPWMvalue(val):
  # This function returns 0 ... 1024
  pwm_value = int((SERVO_PAN_PWM_WRITE_MAX - SERVO_PAN_PWM_WRITE_MIN) * val + SERVO_PAN_PWM_WRITE_MIN)
  return pwm_value
 
def getServoTiltPWMvalue(val):
  # This function returns 0 ... 1024
  pwm_value = int((SERVO_TILT_PWM_WRITE_MAX - SERVO_TILT_PWM_WRITE_MIN) * val + SERVO_TILT_PWM_WRITE_MIN)
  return pwm_value
 
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(SERVO_PAN, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pinMode(SERVO_TILT, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(375) # 50Hz
wiringpi.pwmWrite(SERVO_PAN, getServoPanPWMvalue(0.5))
wiringpi.pwmWrite(SERVO_TILT, getServoTiltPWMvalue(0.5))
 
webiopi.setDebug()
 
def setup():
  webiopi.debug("Script with macros - Setup")
 
def loop():
  webiopi.sleep(5)
 
def destroy():
  webiopi.debug("Script with macros - Destroy")
 
@webiopi.macro
def setHwPWMforPan(duty, commandID):
  wiringpi.pwmWrite(SERVO_PAN, getServoPanPWMvalue(float(duty)))
 
@webiopi.macro
def setHwPWMforTilt(duty, commandID):
  wiringpi.pwmWrite(SERVO_TILT, getServoTiltPWMvalue(float(duty)))
