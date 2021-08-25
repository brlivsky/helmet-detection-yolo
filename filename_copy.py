import os
cwd = os.path.dirname(os.path.realpath(__file__))
f = open("train.txt","a+")
for(dirname, dirs, files) in os.walk('.'):
	for filename in files:
		if filename.endswith('.jpg'):
			f.write(cwd+"\\"+filename+"\n")
f.close()

