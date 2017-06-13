# App Information
AppName = "GetIP"
AppAuthor = "Mike Zweifel"
AppVersion = "0.1"
AppImage = [[[ 51   0 255]
  [ 61   0 255]
  [ 70   0 255]
  [ 80   0 255]
  [ 89   0 255]
  [ 98   0 255]
  [108   0 255]
  [117   0 255]
  [127   0 255]
  [136   0 255]
  [146   0 255]
  [155   0 255]
  [164   0 255]
  [174   0 255]
  [183   0 255]
  [193   0 255]
  [202   0 255]
  [212   0 255]
  [221   0 255]
  [231   0 255]]

 [[ 51   0 255]
  [ 61   0 255]
  [ 70   0 255]
  [ 80   0 255]
  [ 89   0 255]
  [ 98   0 255]
  [108   0 255]
  [117   0 255]
  [127   0 255]
  [136   0 255]
  [146   0 255]
  [155   0 255]
  [164   0 255]
  [174   0 255]
  [183   0 255]
  [193   0 255]
  [202   0 255]
  [212   0 255]
  [221   0 255]
  [231   0 255]]

 [[ 51   0 255]
  [ 61   0 255]
  [ 70   0 255]
  [ 80   0 255]
  [ 89   0 255]
  [ 98   0 255]
  [108   0 255]
  [117   0 255]
  [127   0 255]
  [136   0 255]
  [146   0 255]
  [155   0 255]
  [164   0 255]
  [174   0 255]
  [183   0 255]
  [193   0 255]
  [202   0 255]
  [212   0 255]
  [221   0 255]
  [231   0 255]]

 [[ 51   0 255]
  [ 61   0 255]
  [ 70   0 255]
  [ 80   0 255]
  [ 89   0 255]
  [ 98   0 255]
  [108   0 255]
  [117   0 255]
  [127   0 255]
  [136   0 255]
  [146   0 255]
  [155   0 255]
  [164   0 255]
  [174   0 255]
  [183   0 255]
  [193   0 255]
  [202   0 255]
  [212   0 255]
  [221   0 255]
  [231   0 255]]

 [[ 51   0 255]
  [ 61   0 255]
  [ 70   0 255]
  [ 80   0 255]
  [ 89   0 255]
  [ 98   0 255]
  [108   0 255]
  [117   0 255]
  [127   0 255]
  [136   0 255]
  [146   0 255]
  [155   0 255]
  [164   0 255]
  [174   0 255]
  [183   0 255]
  [193   0 255]
  [202   0 255]
  [212   0 255]
  [221   0 255]
  [231   0 255]]

 [[ 51   0 255]
  [ 61   0 255]
  [ 70   0 255]
  [ 80   0 255]
  [ 89   0 255]
  [ 98   0 255]
  [108   0 255]
  [117   0 255]
  [127   0 255]
  [136   0 255]
  [146   0 255]
  [155   0 255]
  [164   0 255]
  [174   0 255]
  [183   0 255]
  [193   0 255]
  [202   0 255]
  [212   0 255]
  [221   0 255]
  [231   0 255]]

 [[ 51   0 255]
  [ 61   0 255]
  [ 70   0 255]
  [ 80   0 255]
  [ 89   0 255]
  [ 98   0 255]
  [108   0 255]
  [117   0 255]
  [127   0 255]
  [136   0 255]
  [146   0 255]
  [155   0 255]
  [164   0 255]
  [174   0 255]
  [183   0 255]
  [193   0 255]
  [202   0 255]
  [212   0 255]
  [221   0 255]
  [231   0 255]]

 [[ 51   0 255]
  [ 61   0 255]
  [ 70   0 255]
  [ 80   0 255]
  [ 89   0 255]
  [ 98   0 255]
  [108   0 255]
  [117   0 255]
  [127   0 255]
  [136   0 255]
  [146   0 255]
  [155   0 255]
  [164   0 255]
  [174   0 255]
  [183   0 255]
  [193   0 255]
  [202   0 255]
  [212   0 255]
  [221   0 255]
  [231   0 255]]

 [[ 51   0 255]
  [ 61   0 255]
  [ 70   0 255]
  [ 80   0 255]
  [ 89   0 255]
  [ 98   0 255]
  [108   0 255]
  [117   0 255]
  [127   0 255]
  [136   0 255]
  [146   0 255]
  [155   0 255]
  [164   0 255]
  [174   0 255]
  [183   0 255]
  [193   0 255]
  [202   0 255]
  [212   0 255]
  [221   0 255]
  [231   0 255]]

 [[ 51   0 255]
  [ 61   0 255]
  [ 70   0 255]
  [ 80   0 255]
  [ 89   0 255]
  [ 98   0 255]
  [108   0 255]
  [117   0 255]
  [127   0 255]
  [136   0 255]
  [146   0 255]
  [155   0 255]
  [164   0 255]
  [174   0 255]
  [183   0 255]
  [193   0 255]
  [202   0 255]
  [212   0 255]
  [221   0 255]
  [231   0 255]]]
import socket
import fcntl
import struct
import math, sys
import time
import colorsys

pixels = [[[255 for x in range(3)] for x in range(10)] for x in range(20)]
numMatrix = [[0 for x in range(30)] for x in xrange(8)]
numMatrix = [[0,1,0,0,1,0,0,1,0,1,1,0,1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1,0],[1,0,1,1,1,0,1,0,1,0,0,1,1,0,1,1,0,0,1,0,0,0,0,1,1,0,1,1,0,1],[1,0,1,0,1,0,0,0,1,0,0,1,1,0,1,1,0,0,1,0,0,0,0,1,1,0,1,1,0,1],[1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,1,1,0,1,1,0,0,1,0,0,1,0,0,1,1],[1,0,1,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,0,1],[1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0,0,1,0,1,0,0,1],[1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0,0,1,0,1,0,0,1],[0,1,0,1,1,1,1,1,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0,0,0,1,0,1,1,0]]
brightness = 0.0
spidev = file("/dev/spidev0.0", "wb")

def drawsnake():
	for row in range(0,20):
		if row%2==0:
			for pixel in range(0,10):
				for color in range(0,3):
					c=int(pixels[row][pixel][color]*brightness)
					spidev.write(chr(c & 0xFF))
		else:
			for pixel in range(9,-1,-1):
				for color in range(0,3):
					c=int(pixels[row][pixel][color]*brightness)
					spidev.write(chr(c & 0xFF))			
        spidev.flush()
        time.sleep(0.001)
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def run():
	global pixels
	global brightness
	global numMatrix

	brightness = 1
	pixels = [[[0 for x in range(3)] for x in range(10)] for x in range(20)]

	try:
		wlan = get_ip_address("wlan0").split('.')
		print "wlan0: ",wlan
		for zahl in wlan:
			z= zahl.zfill(3)
			zahleins = int(z[0])
			for x in range (1,9):
				for y in range (1,4):
					if numMatrix[(x-1)][(zahleins*3)+(y-1)]==1:
						pixels[y][9-x]=[255,0,0]
					else:
						pixels[y][9-x]=[0,0,0]
			if zahl >9:
				zahlzwei = int(z[1])
				for x in range (1,9):
					for y in range (1,4):
						if numMatrix[(x-1)][(zahlzwei*3)+(y-1)]==1:
							pixels[y+4][9-x]=[255,0,0]
						else:
							pixels[y+4][9-x]=[0,0,0]
			if zahl >99:
				zahldrei = int(z[2])
				for x in range (1,9):
					for y in range (1,4):
						if numMatrix[(x-1)][(zahldrei*3)+(y-1)]==1:
							pixels[y+8][9-x]=[255,0,0]
						else:
							pixels[y+8][9-x]=[0,0,0]
			drawsnake()
			time.sleep(1.5)
	except:
		print "wlan0:  not connected."
	try:
		eth = get_ip_address("eth0").split('.')
		print "eth0:  ",eth
		for zahl in eth:
			z= zahl.zfill(3)
			zahleins = int(z[0])
			for x in range (1,9):
				for y in range (1,4):
					if numMatrix[(x-1)][(zahleins*3)+(y-1)]==1:
						pixels[y][9-x]=[0,255,0]
					else:
						pixels[y][9-x]=[0,0,0]
			if zahl >9:
				zahlzwei = int(z[1])
				for x in range (1,9):
					for y in range (1,4):
						if numMatrix[(x-1)][(zahlzwei*3)+(y-1)]==1:
							pixels[y+4][9-x]=[0,255,0]
						else:
							pixels[y+4][9-x]=[0,0,0]
			if zahl >99:
				zahldrei = int(z[2])
				for x in range (1,9):
					for y in range (1,4):
						if numMatrix[(x-1)][(zahldrei*3)+(y-1)]==1:
							pixels[y+8][9-x]=[0,255,0]
						else:
							pixels[y+8][9-x]=[0,0,0]
			drawsnake()
			time.sleep(1.5)

	except:
		print "eth0:   not connected."
	pixels = [[[0 for x in range(3)] for x in range(10)] for x in range(20)]
	drawsnake()


if __name__ == '__main__':
	run()
