import serial
import time


MAX_BUFF_LEN = 255
SETUP = False
port = None

prev = time.time()

while(not SETUP):
	try:				 
		port = serial.Serial("COM4", 115200, timeout=1)

	except:
		if(time.time() - prev > 2):
			print("No serial detected, please plug your uController")
			prev = time.time()

	if(port is not None):
		SETUP = True


def read_ser(num_char = 1):
	string = port.read(num_char)
	return string.decode()

def write_ser(cmd):
	cmd = cmd + '\n'
	port.write(cmd.encode())

while(1):
	string = read_ser(MAX_BUFF_LEN)
	if(len(string)):
		print(string)

	cmd = input()
	if(cmd):
		write_ser(cmd)