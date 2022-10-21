import Jogo_da_Forca
import Jogo_de_Adivinhação

def escolhe_jogo():

    print('**********************************')
    print ('Escolha seu Jogo!')
    print('**********************************')

    print('(1) Forca (2) Adivinhação')

    jogo = int(input('Qual jogo você quer ?'))

    if (jogo ==1):
        print("Jogando forca")
        Jogo_da_Forca.forca()
    elif(jogo==2):
        print('Jogando Adivinhação')
        Jogo_de_Adivinhação.adivinhação()

    print('Fim do jogo')

if(__name__=='__main__'):
    escolhe_jogo()


