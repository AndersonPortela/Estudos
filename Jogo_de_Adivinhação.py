import random

def adivinhação ():

    print('**********************************')
    print ('Bem vindo ao jogo de Adivinhação!')
    print('**********************************')

    numero_secreto = random.randrange(1,100)
    pontos = 1000

    print ('Qual o nível da partida ?')
    print ('(1) fácil (2) médio (3) Dificil)')

    nivel = int(input('Define nível: '))

    if (nivel ==1):
        total_de_tentativas=20
    elif(nivel==2):
        total_de_tentativas=10
    else:
        total_de_tentativas=5

    for rodada in range(1,total_de_tentativas +1):
        print('tentativas {} de {}'.format(rodada,total_de_tentativas))
        chute = int(input('Digite o seu número entre 1 e 100: '))
        print('você digitou ', chute)

        if (chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100')
            continue

        acertou =  chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print('Parabéns, você acertou e fez {} pontos'.format(pontos))
            break
        else:
            if (maior):
                print ('Você errou! Seu chute foi maior que o numero secreto.')
            elif(menor):
                print ('Você errou! Seu chute foi menor que o numero secreto.')
            pontos_perdidos = abs(numero_secreto-chute)
            pontos = pontos - pontos_perdidos

    print('Fim do jogo')
if(__name__=='__main__'):
    jogar()


