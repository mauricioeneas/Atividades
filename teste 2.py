def main ():

    #primeira referência
    decrescente = True

    anterior = int(input("Digite o primeiro número da sequencia: "))
    valor = 1
    #enquanto valor for diferente de zero e decrescente "True"
    while valor != 0 and decrescente:
         valor = int(input("Digite o proximo número da sequência: "))
#se o valor for maior que o anterior, descrescente é falso
         if valor > anterior:
             decrescente = False
#anterior se transforma em valor
         anterior = valor


#depois do comando while, a condição para descrescente falso ou verdadeiro
    if decrescente:
        print("A sequência está em ordem decrescente! :-) ")
    else:
        print("A sequência não está em ordem decrescente! :-( ")


main ()
            
