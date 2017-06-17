import sys
from scipy import misc

x = input("Dateipfad und Dateinamen des Bilds")
arr = misc.imread(x)
all = arr.tolist()

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

print all

sys.stdout = orig_stdout
f.close()
exit()
