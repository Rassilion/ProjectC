for i in range(1, 47):
    asd=open("inp/"+str(i), "r")
    s=asd.read()[:-1]
    asd.close
    asd=open("out/"+str(i), "w")
    a=0
    b=1
    for j in range(int(s)):
        temp=b
        b=a+b
        a=temp
    asd.write(str(a)+"\n")
    asd.close()
