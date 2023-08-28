nome = input('Qual é o seu nome? ')
nascimento = int(input('Qual é o ano de seu nascimento? '))
sub = 2023 - nascimento
if sub < 18:
    res = 18 - sub
    print(f'Quando você completar 18 anos deverá se alistar no serviço militar! Falta aproximadamente {res} ano(s) para que você possa alistar')
elif sub == 18:
    print(f'O cidadão [{nome}] já possui idade para se alistar!')
elif sub > 18:
    res2 = sub - 18
    print(f'O cidadão {nome} passou {res2} ano(s) para a idade certa de seu alistamento!!')
else:
    print('ERRO! TENTE NOVAMENTE!!!!')


