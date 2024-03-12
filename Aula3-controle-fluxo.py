print("Diga me, sim(s) ou não(n)?")

resposta =  int(input()) # python espera una entradas do usuário

if resposta == 1:

 print("resposta positiva :)")

elif resposta == 2:

 print("resposta negativa :(")

else:

 print("reposta desconhecida :/")

 # se numero for multiplo de 3 print FIZZ. multiplo de 3: 6 % 3 == 0
 # se numero for multiplo de 5 print FIZZ
 # se numero for multiplo de 5 e de 3 print FIZZBUZZ
 # se não for multiplo de 3 nem de 5 imprimi o proprio numero 