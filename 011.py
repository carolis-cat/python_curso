from math import ceil
largura = float(input('qual é a largura?'))
altura = float(input('qual é a altura?'))
print('sua area é {:.2f} e você vai precisar de {} latas de tinta'.format(largura*altura, ceil(largura*altura/2)))
