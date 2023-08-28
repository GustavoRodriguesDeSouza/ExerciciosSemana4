pro = input('Digite o nome do produto: ')
pre = float(input('Digite o preço do produto: '))
pag = int(input('Digite 1 se for um dinheiro ou cheque, 2 se for no débito, 3 se queser parcelar em vezes ou 4 se quiser parcelar 3 vezes'))
if pag == 1:
    desc = (pre * 10)/100
    print(f'A vista o produto escolhido que foi {pro} ficará: {pre - desc}:')
elif pag == 2:
    desc2 = (pre * 5)/100
    print(f'A vista no cartão o produto escolhido que foi {pro} ficará: {pre - desc2}')
elif pag == 3:
    print(f'Parcelado o produto escolhido que foi {pro} no cartão em duas vezes ficará {pre/2} ')
elif pag == 4:
    jur = (pre * 20)/100
    print(f'o produto escolhido que foi {pro} parcelado no cartão  em três vezes ou mais vai vai sofrer juros de 20% assim ficando: {pre + jur} ')

