print('ola seja bem vindo ao jogo de pergunta e resposta ')
print(  """ /\_/\ 
( o.o )
 > ^ <   """)
print('Qual é o menor país do mundo? ')

resposta= 'vaticano'
for tentativas in range(1,4):
    usuario= input('\ndigite qual a sua resposta! ')
    if usuario==resposta:
        print('parabéns você acertou! ')
    else:
        print(f'\n(︶︹︶) voce errou! tente novamente, voce errou; {tentativas}') 
        if tentativas==4:
            print('aaa que pena sua tentativas acabaram')
