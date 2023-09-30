import time
from gpiozero import DistanceSensor

pintrigger = 17
pinecho = 18
sensor = DistanceSensor(echo=pinecho, trigger=pintrigger)
print("Ultrasonic Measurement")
try:
    while True:
        print("Distance: %.1f cm" % (sensor.distance * 100))

except KeyboardInterrupt:
    exit()
