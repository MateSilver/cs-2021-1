import registros

funcionario = registros.registro('alex',1234)
cargo = input('cargo: ')
if cargo.lower() == 'gerente':
    funcionario._saldo += 1500.0
elif cargo.lower() == 'superior':
    funcionario._saldo += 600.0
elif cargo.lower() == 'vendedor':
    funcionario._saldo += 250.0