from random import randint

def randPal():
	return randint(0,1)==1

def palGen(n):
	s=""
	for i in range(n):
		s+=str(randint(1, 9))
	if randPal():
		s=s+str(randint(1, 9))+s[::-1]
	else:
		s=s+s[::-1]
		
	return s

for i in range(1, 21):
	asd=open("inp/"+str(i), "w")
	
	s=palGen(4)
	
	if randPal():
		i=randint(0, len(s)-1)
		s=s[:i]+str(randint(1,9))+s[i+1:]
		
	s+="\n"
	asd.write(s)
	asd.close()
	

for i in range(21, 101):
	asd=open("inp/"+str(i), "w")
	
	s=palGen(randint(20, 45))
	
	if randPal():
		i=randint(0, len(s)-1)
		s=s[:i]+str(randint(1,9))+s[i+1:]
	s+="\n"
	asd.write(s)
	asd.close()
	

