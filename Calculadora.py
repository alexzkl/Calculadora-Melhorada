# Calculadora-Melhorada
print ( 'Olá, bem vindo a minha calculadora!' )
num1  =  int ( input ( 'Qual tabuada você precisa?: ' ))
passo  =  intervalo ( 1 , 10 + 1 )
a  = ( 's' )
b  = ( 'n' )
para  i  em  passo :
    print ( '{} x {:2} = {}' . format ( num1 , i , num1  *  i ))
print ( 'Reponda com s ou n, a próxima pergunta ' )
per  =  input ( 'Precisa de outra tabuada?' )
se  por  ==  a :
    imprimir ( num1 )
elif  por  ==  b :
    print ( 'Obrigado por usar minha calculadora!!' )
mais :
    print ( 'Não entendi, reponda só com s ou n:' )
