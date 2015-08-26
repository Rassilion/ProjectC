def isPalindrome(s):
	if s[-1]=="\n":
		s=s[:len(s)-1]
	n=len(s)
	for i in range(n):
		if s[i]!=s[n-1-i]:
			return False
	return True

for i in range(1, 101):
	asd=open("inp/"+str(i), "r")
	s=asd.read()
	asd.close()
	asd=open("out/"+str(i), "w")
	if isPalindrome(s):
		asd.write("EVET\n")
		print i, "EVET"
	else:
		asd.write("HAYIR\n")
		print i, "HAYIR"
	asd.close()
	
	
