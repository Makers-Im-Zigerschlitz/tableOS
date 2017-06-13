import imp
import os

#Settings
PluginFolder = "./apps"
MainModule = "__init__"
TableWidth = 10
TableHeight = 10

#Variables
apps = []

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
print("""\
 _        _     _       _____ _____ 
| |      | |   | |     |  _  /  ___|
| |_ __ _| |__ | | ___ | | | \ `--. 
| __/ _` | '_ \| |/ _ \| | | |`--. \\
| || (_| | |_) | |  __/\ \_/ /\__/ /
 \__\__,_|_.__/|_|\___| \___/\____/  by 'Makers im Zigerschlitz'""")
print
print("Repository: http://github.com/makersimzigerschlitz")
print
print("tableOS started.")
print("Apps installed: ")
for i in apps_meta:
	apps.append(loadPlugin(i))

for j in apps:
	print(" - "+j.AppName+" (Version: "+j.AppVersion+", Author: "+j.AppAuthor+")")

x = input("Welches App soll gestartet werden?")
drawsnake(apps[x].AppImage);

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
