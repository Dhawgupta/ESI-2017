from sense_hat import SenseHat
from time import sleep
from random import randint
import serial
ard = serial.Serial('/dev/ttyACM0',9600)
s = SenseHat()
r = [255,0,0]
e = [0,0,0]
g = [0,255,0]

arrow_d =[
r,r,r,r,e,e,e,e,
r,r,e,e,e,e,e,e,
r,e,r,e,e,e,e,e,
r,e,e,r,e,e,e,e,
e,e,e,e,r,e,e,e,
e,e,e,e,e,r,e,e,
e,e,e,e,e,e,r,e,
e,e,e,e,e,e,e,r
]
arrow_l =[
e,e,e,e,e,e,e,e,
e,e,r,e,e,e,e,e,
e,r,e,e,e,e,e,e,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
e,r,e,e,e,e,e,e,
e,e,r,e,e,e,e,e,
e,e,e,e,e,e,e,e,
]
whole = [
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
]
warning = [
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
]
def ultrasonic_sensor_values():
    ard.write('a')
    a = ord(ard.read())
    #print a	
    sleep(0.05)
    ard.write('b')
    b = ord(ard.read())
    #print b	
    sleep(.05)
    ard.write('c')
    c = ord(ard.read())
    #print c
    sleep(.05)
    ard.write('d')
    d = ord(ard.read())
    #print d	
    sleep(.05)
    return [a,b,c,d]
def read_hat_sensor():
    temp = s.get_temperature()
    hum = s.get_humidity()
    pre = s.get_pressure()
    ort = s.get_orientation()
    pitch = ort['pitch']
    roll = ort['roll']
    yaw = ort['yaw']
    acceleration = s.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    #x=round(x, 0)
    #y=round(y, 0)
    #z=round(z, 0)
    return [temp,pre,hum,pitch,roll,yaw,x,y,z]

while True:
    filename = '~/Baja_Sensor_readings.txt'
    s.set_pixels(whole)
    s.set_rotation(0)
    distance = ultrasonic_sensor_values()    
    print distance
    #for i,j in zip(range(4), distance):
    i = distance.index(min(distance))
    j = min(distance)
    if j < 10:
        s.set_pixels(arrow_d)
        s.set_rotation(90*i)
        sleep(0.5)
    [temp,pre,hum,pitch,roll,yaw,x,y,z] = read_hat_sensor()

    print roll
    if (roll >30 and roll <180 ) or (roll <= 330 and roll >= 200):
        s.set_rotation(90)
        s.set_pixels(warning)
        
        sleep(1)
        
        
    files = open(filename, 'w')
    files.write(pitch)
    files.write('\n')
    files.write(roll)
    files.write('\n')
    files.write(yaw)
    files.write('\n')
    
    for i in range(4):
        files.write(distance[i])
        files.write('\n')
    
    files.write(x)
    files.write('\n')
    files.write(y)
    files.write('\n')
    files.write(z)
    files.write('\n')
    files.close()
    
        
