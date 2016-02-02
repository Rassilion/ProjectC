from random import randint

for i in range(1, 101):
    asd = open("inp/" + str(i), "w")
    asd.write(str(randint(1, 999999999)) + "\n")
