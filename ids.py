import csv
import numpy as np 

b=np.loadtxt(r'songs.csv',dtype=str,delimiter=',',skiprows=1,usecols=(1,))

f = open('ids.txt','a') 

for item in b:
	f.write(item)
	f.write('\n')

f.close()
