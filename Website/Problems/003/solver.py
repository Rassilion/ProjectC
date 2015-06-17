for i in range(1, 101):
    print i
    asd=open("inp/"+str(i), "r")
    s=asd.read()
    s=s[:-1]
    n=int(s)
    print n
    if n%100!=0:
        if n%4==0:
            s="EVET"+"\n"
        else:
            s="HAYIR"+"\n"
    else:
        if n%400==0:
            s="EVET"+"\n"
            print "400e bolunme!!!"
        else:
            s="HAYIR"+"\n"
            print "100 e bolnmede hayir"

    asd.close()
    asd=open("out/"+str(i), "w")
    asd.write(s)
    asd.close()
