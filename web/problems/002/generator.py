from random import randint


def generate():
    prob = randint(10, 90)
    L = []
    for i in range(1, 21):
        flag = randint(1, 100)
        if flag < prob:
            L += [i]
    R = []
    while L != []:
        index = randint(0, len(L) - 1)
        R += [L[index]]
        L = L[:index] + L[index + 1:]

    return R


for i in range(1, 101):
    filename = str(i)
    asd = open(filename, "w")
    s = ""
    L = generate()
    s += str(len(L)) + "\n"
    for j in range(0, len(L) - 1):
        s += str(L[j]) + " "
    if L != []:
        s += str(L[-1])
    else:
        print "hey bu bos :" + str(i)
    s += "\n"
    asd.write(s)
    asd.close()
