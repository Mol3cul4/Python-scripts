#Decomposicao em fatores primos

def main():

    n = int(input("Digite um numero (>1): "))

    fator = 2 # primeiro fator
    while n != 1:
        # conta a multiplicidade de fator em n
        mult = 0;
        while n%fator == 0:
            n = n / fator;
            mult = mult + 1;

        # imprime a multiplicidade do fator
        if mult != 0:
            print("fator %d multiplicidade %d" %(fator, mult))

        fator = fator + 1

#-------------------------------------------------------
main() # chamada da func principal
