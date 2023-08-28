num = int(input('Digite algum número inteiro: '))
esc = int(input('Escolha a base de conversão: Digite 1 para binário, 2 para octal ou 3 para hexadecimal: '))
if esc == 1:
    print('A conversão do número [{}] para binário será: [{}]'.format(num, '{0:b}'.format(num)))
elif esc == 2:
    print('A conversão do número [{}] para octal será: [{}]'.format(num, '{0:o}'.format(num)))
elif esc == 3:
    print('A conversão do número [{}] para hexadecimal será: [{}]'.format(num, '{0:x}'.format(num)))
else:
    print('ERRO! Tente novamente!')