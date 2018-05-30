import os
import random
X=0
y=0
while(y!=99):
	f=random.randint(0,99)
	if(f==1):
		X=X+1
	y=y+1
print((X/y)*100,"%")