print('ola seja bem vindo ao jogo de pergunta e resposta ')
print(  """ /\_/\ 
( o.o )
 > ^ <   """)
print('Qual é o menor país do mundo? ')

resposta= 'vaticano'
tentativas= 1
while tentativas<=4:
    usuario= input('\ndigite qual a sua resposta! ')
    if usuario==resposta:
        print('\n(◑‿◐) parabéns você acertou!ヽ(^。^)丿(/•ิ_•ิ)/ ')
        break
    else:
        print(f'\n(︶︹︶) voce errou! tente novamente, essa foi a tentativa: {tentativas}') 
        tentativas+=1       
        if tentativas==4:
            print('(╥﹏╥) aaa que pena sua tentativas acabaram')
            break
