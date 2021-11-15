import registros
import registros_medio
import registros_superior

funcionario = []
i = input('numero de funcionarios: ')
for j in range(0,i):
    nome = input('nome: ')
    id = input('id: ')
    res = input('tem escola?')
    if res == 's':
        escola = input('escola: ')
        res = input('tem faculdade?')
        if res == 's':
            facul = input('faculdade: ')
            funcionario.append(registros_superior.registro_superior(nome,id,escola,facul))
        else:
            funcionario.append(registros_medio.registro_medio(nome,id,escola))
    else:
        funcionario.append(registros.registro(nome,id))