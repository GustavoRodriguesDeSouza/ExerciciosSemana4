nome = input('Digite o seu nome completo: ')
materia1 = float(input('Digite a sua primeira nota: '))
materia2 = float(input('Digite a sua segunda nota: '))
media = (materia1 + materia2)/2

print('Olá', nome)
if media < 50:
    print('Você foi reprovado!!!')
elif media > 50 and media < 69:
    print('Você está de recuperação!!!')
elif media >= 70:
    print('Parabéns você foi aprovado!!!!!')