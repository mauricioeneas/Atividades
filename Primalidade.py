
def éPrimo (x):
    fator = 2
    while x % fator != 0 and fator < x/2:
        fator = fator + 1
        
    if x % fator == 0:
        return False
    else:
        return True



n = int(input("Digite um número:"))


if éPrimo(n) or n == 2:
    print("primo")
else:
     print("não primo")
