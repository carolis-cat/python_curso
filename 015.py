km = float(input('quantos km vc rodou?'))
dias = int(input('por quantos dia vc alugou?'))
pago = (dias * 60) + (km * 0.15)
print('o total a pagar será: R${:.2f}.'.format(pago))
