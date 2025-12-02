import serial, time

ser = serial.Serial("COM9", 115200, timeout=1)

t0 = time.time()
while time.time() - t0 < 10:
    line = ser.readline()
    if line:
        print("RECV:", line.decode(errors='ignore').strip())

ser.close()
