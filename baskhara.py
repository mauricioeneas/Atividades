
import math

def main ():
    

    print("Vamos calcular a formula de Baskhara ")
    a = int(input("Digite o valor de a : "))
    b = int(input("Digite o valor de b : "))
    c = int(input("Digite o valor de c : "))

    x = (b**2)-(4*a*c)

    if x <0:
        print("esta equação não possui raízes reais")
    else:
        x = math.sqrt(x)
        x1 = ((-b)+x)/(2*a)
        x2 = ((-b)-x)/(2*a)
#        print("o resultado desta equação é: ",x1," e ",x2)

        if x2 < x1:
            print("as raízes da equação são",x2,"e",x1)
        if x2 > x1:
            print("as raízes da equação são",x1,"e",x2)
        if x1 == x2:
            print("a raiz desta equação é",x1)

main ()
