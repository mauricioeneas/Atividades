
import math

def main():

    x1 = int(input("Insira um numero para x1: "))
    y1 = int(input("Insira um numero para y1: "))
    x2 = int(input("Insira um numero para x2: "))
    y2 = int(input("Insira um numero para y2: "))

    d = math.sqrt(((x1 - x2)**2)+ ((y1-y2)**2))

    if d >=10:
        print("longe")
    else:
        print("perto")


main()
