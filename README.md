![image](https://github.com/mcds04/Afrocodigod-If/assets/100251166/9e07476e-18c3-43bc-96a1-c7c242a9ed2f)

🚀 Afrocodigos---Aula---Módulo-1 🚀

🌠 [Aulas do Projeto Afrocódigo]

🧑‍💻 Professor Felipe de Moraes- 🌱Ecossistema 🐍PYTHON🐍

🌠 [afrocódigos] 🌠

EXERCÍCIO C:\projetos\Afrocodigod If\Aula3-controle-fluxo3.py

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

🌠 EXERCÍCIO COMPLEMENTARES🌠 

C:\projetos\Afrocodigod If\Aula3-controle-fluxo2.py

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FIZZBUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ") # Saida = saida + palavra(i)
    else:
        print(i)

🌠 EXERCÍCIO COMPLEMENTARES🌠 

C:\projetos\Afrocodigod If\Aula3-controle-fluxo.py

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

