IPI = float(input('valor do IPI(%): '))

cod1 = int(input('Código da peça 01: '))
preco1 = float(input(f'Preço da peça {cod1}: '))
quantidade1 = int(input(f'quantidade de peças {cod1}: '))

cod2 = int(input('Código da peça 02: '))
preco2 = float(input(f'Preço da peça {cod2}: '))
quantidade2 = int(input(f'quantidade de peças {cod2}: '))

print(f'Total: {((preco1*quantidade1)+(preco2*quantidade2))*((IPI/100)+1)}')