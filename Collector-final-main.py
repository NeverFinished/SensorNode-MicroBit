
from microbit import *
import radio
import time

radio.config(group=23, power=7, length=32, queue=8) # TODO more queue?
radio.on()
ts = time.ticks_ms()
node_ts = []

print("GW")

for i in range(25):
    node_ts.append(time.ticks_ms())

while True:
    details = radio.receive_full()
    if details:
        msg, rssi, timestamp = details;
        msg = msg[3:]
        msg = msg.decode('utf-8')
        id = ord(msg[0])-65
        node_ts[id] = time.ticks_ms()
        print(msg, rssi, sep=' ')
        ts = time.ticks_ms()
    if (time.ticks_diff(time.ticks_ms(), ts)>500):
        ts = time.ticks_ms()
        print("nop")
    for id in range(25):
        age = time.ticks_ms() - node_ts[id]
        val = 0
        if (age < 1000):
            val = max(0, 9 - int(age / 100))
        display.set_pixel(id % 5, int(id / 5), val) # fade-out when not seen for a time

    #sleep(100)
