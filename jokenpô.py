import random
joq = int(input('Digite 1 para pedra, 2 para papel ou 3 para tesoura: '))
comp = random.randint(1, 3)
if joq == 1 and comp == 2:
    print('GANHEI! Escolhi papel!')
elif joq == 1 and comp == 3:
    print('Você ganhou ;-; ! Escolhi tesoura!')
elif joq == comp:
    print('EMPATE >< ! Escolhemos os mesmos!')

elif joq == 2 and comp == 1:
    print('GANHEI! Escolhi papel!')
elif joq == 2 and comp == 3:
    print('GANHEI! Escolhi tesoura!')
elif joq == comp:
    print('EMPATE >< ! Escolhemos os mesmos!')

elif joq == 3 and comp == 1:
    print('GANHEI! Escolhi pedra!')
elif joq == 3 and comp == 2:
    print('Você ganhou ;-; ! Escolhi papel!')
elif joq == comp:
    print('EMPATE! Escolhemos os mesmos!')


