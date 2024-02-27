import sys

sys.set_int_max_str_digits(0)

n1 = int(input("Quantos números da sequência de fibonnaci você quer ver: "))


def functionSequencia():
    sequencia = 1
    anterior = 1    
    for n in range(n1):
        print("\n\n",sequencia+anterior)
        sequencia = sequencia+anterior
        anterior = sequencia-anterior    

if __name__ == "__main__":
    functionSequencia()

