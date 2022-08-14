# Calculadora-Melhorada
print('Olá, bem vindo a minha calculadora!')
# Pedindo ao usuário o número da tabuada que deseja
num1 = int(input('Qual tabuada você precisa?: '))
#  Definindo o intravalo/range
passo = range(1,10+1)
# Criando as váriavel para o input per/pergunta 
a = ('s')
b = ('n')
# Defininfo o for 
for i in passo:
    print('{} x {:2} = {}'.format(num1, i, num1 * i))
# Fazendo as perguntas ao usuário
print('Reponda com s ou n, a próxima pergunta ')
per = input('Precisa de outra tabuada? ')
# Definindo os ifs
if per == a:
    print(num1)
elif per == b:
    print('Obrigado por usar minha calculadora!!')
else:
    print('Não entendi, reponda só com s ou n:')
