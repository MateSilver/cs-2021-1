import registros
import registros_medio
import registros_superior

empresa = []

novo = registros.registro('roberto',1234)
empresa.append(novo)
novo = registros.registro('richard',1334)
empresa.append(novo)
novo = registros.registro('daniel',1244)
empresa.append(novo)
novo = registros.registro('lucão',1236)
empresa.append(novo)
novo = registros_medio.registro_medio('Vitor',1254,'Santa clara','Duque de Caxias')
empresa.append(novo)
novo = registros_medio.registro_medio('Wilson',1534,'padre pelagio','Coração de Jesus')
empresa.append(novo)
novo = registros_medio.registro_medio('Danilo',1249,'Luiz afonso padilha','Salomão')
empresa.append(novo)
novo = registros_medio.registro_medio('Casemiro',1836,'Juliano bittencourt','Dona Rosa')
empresa.append(novo)
novo = registros_superior.registro_superior('Ana',1204,'Santa clara','UFG')
empresa.append(novo)
novo = registros_superior.registro_superior('Susan',1314,'Julio Bravo','IFG')
empresa.append(novo)

custo_basico = 0
custo_medio = 0
custo_superior = 0
for i in range(0,10):
    if empresa[i]._escola:
        custo_basico += empresa[i]._saldo
    elif empresa[i]._escola_medio:
        custo_medio += empresa[i]._saldo
    else:
        custo_superior = empresa[i]._saldo
custo = custo_basico+custo_medio+custo_superior
print(f'custo de funcionarios do ensino basico: {custo_basico}')
print(f'Custo dos funcionarios do ensino medio: {custo_medio}')
print(f'Custo dos de ensino superior: {custo_superior}')