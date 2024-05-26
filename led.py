import serial
import time

# Replace 'COM11' with the correct port name
port_name = 'COM11'
baud_rate = 9600

try:
    ser = serial.Serial(port_name, baud_rate)
    time.sleep(2)  # Wait for Arduino to initialize
    print(f"Connected to {port_name}")

    # Test turning LED on
    ser.write(b'1')
    time.sleep(2)
    # Test turning LED off
    ser.write(b'0')
    ser.close()
    print("LED test completed")
except serial.SerialException as e:
    print(f"Could not open port {port_name}: {e}")
