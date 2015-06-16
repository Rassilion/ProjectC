for i in range(1, 101):
    asd=open("inp/"+str(i), "r")
    s=asd.read()
    j=0
    while s[j]!="\n":
        j+=1
    s=s[j+1:]
    s=s[:-1]
    L=s.split(" ")
    R=[]
    for index in range(1, 21):
        if str(index) not in L:
            R+=[index]

    s=""
    L=R
    asdf=open("out/"+str(i), "w")
    for j in range(0, len(L)-1):
        s+=str(L[j])+" "
    if L!=[]:
        s+=str(L[-1])
    else:
         print "hey bu bos :" +str(i)
    s+="\n"
    asdf.write(s)
    asdf.close()
