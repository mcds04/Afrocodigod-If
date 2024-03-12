multiplos = int(input("Diga me un número: ")) # python espera una entradas do usuário

if multiplos % 15 == 0:
    print("FIZZBUZZ")
elif multiplos % 5 == 0:
    print("BUZZ")
elif multiplos % 3 == 0:
    print("FIZZ")
else:
    print(multiplos)
'''

'''EXERCICIO PARA PROXIMA QUARTA'''
for multiplos in range(1, 16): # o python espera
    if multiplos % 15 == 0:
        print("FIZZBUZZ")
    elif multiplos % 5 == 0:
        print("BUZZ")
    elif multiplos % 3 == 0:
        print("FIZZ")
    else:
        print(multiplos)


'''verifica todos os números de 1 a 15 e imprime “FIZZ” se o número for múltiplo de 3, “BUZZ” 
se for múltiplo de 5 e “FIZZBUZZ” se for múltiplo de ambos. 
Se o número não for múltiplo de 3 nem de 5, ele simplesmente imprime o próprio número'''
