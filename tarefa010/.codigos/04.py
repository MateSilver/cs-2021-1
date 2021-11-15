# ENTRADA DE VALOR DE IPI:
IPI = float(input('valor do IPI(%): '))

# PASSO 1:
# ENTRADA DE DADOS REFERENTES AO PRIMEIRO PRODUTO:
cod1 = int(input('Código da peça 01: '))
preco1 = float(input(f'Preço da peça {cod1}: '))
quantidade1 = int(input(f'quantidade de peças {cod1}: '))

# PASSO 2:
# ENTRADA DE DADOS REFERENTES AO SEGUNDO PRODUTO:
cod2 = int(input('Código da peça 02: '))
preco2 = float(input(f'Preço da peça {cod2}: '))
quantidade2 = int(input(f'quantidade de peças {cod2}: '))

# EXIBE PRECO TOTAL:
print(f'Total: {((preco1*quantidade1)+(preco2*quantidade2))*((IPI/100)+1)}')