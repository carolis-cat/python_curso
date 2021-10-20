# camelCase
n1 = int(input('um número:'))
n2 = int(input('outro número:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
divisaoInteira = n1 // n2
exponenciacao = n1 ** n2
print('A soma é {}, \n o produto é {} e a divisão é {:.3f}' .format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}' .format(divisaoInteira, exponenciacao))
