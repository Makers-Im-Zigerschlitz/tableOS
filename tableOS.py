import imp
import os
import time
from inputs import get_gamepad

#Settings
PluginFolder = "./apps"
MainModule = "__init__"
TableWidth = 10
TableHeight = 10
pixels = [[[255 for x in range(3)] for x in range(10)] for x in range(20)]
brightness = 1.0
tableIP = [0,0,0,0]
spidev = file("/dev/spidev0.0", "wb")


#Variables
apps = []

# Draws the matrix as is
def draw(image):
        for row in image:
                for pixel in row:
                        for color in pixel:
                                c = int(color*brightness)
                                spidev.write(chr(c & 0xFF))
        spidev.flush()
        time.sleep(0.001)


# Draws the Matrix starting at the topleft and going down in a snake-pattern
def drawsnake(image):
	for row in range(0,20):
		if row%2==0:
			for pixel in range(0,10):
				for color in range(0,3):
					c=int(image[row][pixel][color]*brightness)
					spidev.write(chr(c & 0xFF))
		else:
			for pixel in range(9,-1,-1):
				for color in range(0,3):
					c=int(image[row][pixel][color]*brightness)
					spidev.write(chr(c & 0xFF))			
        spidev.flush()
        time.sleep(0.001)


def getPlugins():
    plugins = []
    possibleplugins = os.listdir(PluginFolder)
    for i in possibleplugins:
        location = os.path.join(PluginFolder, i)
        if not os.path.isdir(location) or not MainModule + ".py" in os.listdir(location):
            continue
        info = imp.find_module(MainModule, [location])
        plugins.append({"name": i, "info": info})
    return plugins
apps_meta = getPlugins()

def loadPlugin(plugin):
	try:
		return imp.load_module(plugin["name"], *plugin["info"])
	finally:
		fp = plugin["info"][0]
		if fp:
			fp.close()
os.system('cls' if os.name == 'nt' else 'clear')
print("""\033[1;32;40m\
 _        _     _       _____ _____ 
| |      | |   | |     |  _  /  ___|
| |_ __ _| |__ | | ___ | | | \ `--. 
| __/ _` | '_ \| |/ _ \| | | |`--. \\
| || (_| | |_) | |  __/\ \_/ /\__/ /
 \__\__,_|_.__/|_|\___| \___/\____/  by 'Makers im Zigerschlitz'""")
print
print("Repository: http://github.com/makersimzigerschlitz")
print
print
print("\033[1;33;40mtableOS started.")
print
print("\033[1;37;40mApps installed: ")
for i in apps_meta:
	apps.append(loadPlugin(i))

for j in apps:
	print(" - "+j.AppName+" (Version: "+j.AppVersion+", Author: "+j.AppAuthor+")")

selApp = 0
drawsnake(apps[selApp].AppImage)
while 1:
	events = get_gamepad()
	for event in events:
		if event.ev_type =='Key':
			if (event.code == 'BTN_THUMB' and event.state==1):
				apps[selApp].run()
		if event.ev_type == 'Absolute':
			if ((event.code =='ABS_X' and event.state==255) or (event.code=='ABS_Y' and event.state ==0)):
				selApp+=1
				if selApp>=len(apps):
					selApp-=len(apps)
				drawsnake(apps[selApp].AppImage)
			if ((event.code =='ABS_X' and event.state==0) or (event.code=='ABS_Y' and event.state ==255)):
				selApp-=1
				if selApp<0:
					selApp+=len(apps)
				drawsnake(apps[selApp].AppImage)


