#x = int(input('digite um valor' ))
#if(x == 0):
#    print('valor nulo ')
#else:
# if(x > 0):
#      print('positivo')
#   else: 
#        print('negativo')
        
        #Exercício 2
        
#nota1 = int(input('Digite a primeira nota: '))
#nota2 = int(input('Digite a segunda nota: '))

#media = int(nota1 + nota2)/2

#mediastr = str(media)

#(print('A media é ' + mediastr))

#if( media >= 6 ):
#    print('APROVADO')
#else:
#    print('reprovado')

        #Exercício 3
        
salário = int(input('Escreva seu salário: '))
if(salário <= 1500):
    reaj1 = (salário * 20)/100 + salário
    reaj1str = str(reaj1)
    print ('O reajuste de 20 porcento será '+ reaj1str)
elif(salário <= 3000):
    reaj2 = (salário * 15)/100 + salário
    reaj2str = str(reaj2)
    print ('O reajuste de 15 porcento será '+ reaj2str)
else:
    reaj3 = (salário * 10)/100 + salário
    reaj3str = str(reaj3)
    print ('O reajuste de 10 porcento será '+ reaj3str)