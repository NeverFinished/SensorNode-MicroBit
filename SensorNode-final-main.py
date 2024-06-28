# Imports go at the top
from microbit import *
import radio

label = "A"

radio.config(group=23, power=7, length=32)
radio.on()

#uart.init(baudrate=115200)
#uart.write()

pin0.set_touch_mode(pin1.CAPACITIVE)
pin1.set_touch_mode(pin1.CAPACITIVE)
pin2.set_touch_mode(pin1.CAPACITIVE)

old_bA = 0
old_bB = 0

# little iir lowpass
flt_ax = 0
flt_ay = 0
flt_az = 0

display.show(label)

while True:
    ax = accelerometer.get_x()
    ay = accelerometer.get_y()
    az = accelerometer.get_z()
    flt_ax = (3*flt_ax) + ax
    flt_ax = int(flt_ax / 4)
    flt_ay = (3*flt_ay) + ay
    flt_ay = int(flt_ay / 4)
    flt_az = (3*flt_az) + az
    flt_az = int(flt_az / 4)    
    tp = temperature()
    #heading = compass.heading() # needs calib
    #dll = display.read_light_level() # not useable under the cover
    #asl = microphone.sound_level() # makes no sense in noisy room, is a bit fishy
    tmp_bA = int(button_a.is_pressed())
    tmp_bB = int(button_b.is_pressed())
    bA = old_bA + tmp_bA
    bB = old_bB + tmp_bB
    old_bA = tmp_bA
    old_bB = tmp_bB
    #p0 = int(pin0.is_touched()) # noone will find out for these
    #p1 = int(pin1.is_touched())
    #p2 = int(pin2.is_touched())
    tl = int(pin_logo.is_touched())
    #print(ax, ay, az, tp, dll, asl, bA, bB, p0, p1, p2, sep=" ")
    msg = "{} {} {} {} {} {} {} {}".format(label, flt_ax, flt_ay, flt_az, tp, bA, bB, tl)
    print(msg)
    radio.send(msg)
    sleep(100)
