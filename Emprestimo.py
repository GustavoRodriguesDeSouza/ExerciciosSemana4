valorCasa = float(input('Digite o valor da casa: '))
seuSalário = float(input('Digite o seu salário: '))
ano = float(input('Em quantos anos vai pagar a casa? '))
meses = ano * 12
prestação = valorCasa/meses
if prestação > seuSalário*0.3:
    print('Infelizmente o seu emprestimo foi reprovado!')
else:
    print('Parabéns! O seu empréstimo foi aprovado!')