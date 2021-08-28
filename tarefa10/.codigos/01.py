# ENTRADA DE DADOS DE ANOS MES E DIAS TOTAIS
# DA VIDA DE UMA PESSOA:
ano = int(input('anos: '))
mes = int(input('meses: '))
dia = int(input('dias: '))

"""
 calculo de quantidade total de tempo de vida
 de uma pessoa em dias:

 1 mes = 30  dias
 1 ano = 365 dias
"""

# SOMANDO DADOS
total = (ano*365)+(mes*30)+dia

# SAIDA:
print(f'Total de dias: {total}')