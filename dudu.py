nttl = 0
dados = dict()
tab = list()
ninv = 0
nval = 0
while True:
    n2 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = 0
    soma2 = 0
    n1 = list()
    cpf = input("digite o cpf:")
    print(50*'=')
    nttl = nttl + 1
    while True:
        if (len(cpf) != 11) or not(cpf.isnumeric()):
            cpf = input("cpf invalido para teste, digite novamente:")
            print(50 * '=')
        else:
            print("cpf armazenado com sucesso!")
            print(50 * '=')
            break
    for i in range(9):
        n1.append(int(cpf[i]))
    for x in range(9):
        aux = n1[x] * n2[x]
        soma = soma + aux
    resto = soma % 11
    if resto < 2:
        dgv1 = 0
    else:
        dgv1 = 11 - resto
    n1.append(dgv1)
    n2.insert(0,11)
    for y in range(10):
        aux2 = n1[y] * n2[y]
        soma2 = soma2 + aux2
    resto2 = soma2 % 11
    if resto2 < 2:
        dgv2 = 0
    else:
        dgv2 = 11 - resto2
    n1.append(dgv2)
    n2 = []
    for i in range(11):
        n2.append(int(cpf[i]))
    if n2 == n1:
        n2 = []
        n2.append(int(cpf))
        dados = {'CPF':n2,'VALIDACAO':'VÁLIDO'}
        tab.append(dados)
        nval = nval + 1
    else:
        n2 = []
        n2.append(int(cpf))
        dados = {'CPF':n2, 'VALIDACAO': 'INVÁLIDO'}
        tab.append(dados)
        ninv = ninv + 1
    resp = input("deseja continuar o teste? s/n?:")
    while resp != 'n' and resp != 's':
        resp = input("resposta invalida!!, digite s ou n:")
    if resp == 'n':
        break
print(tab)
print(f'foram testados {nttl} cpfs!')
print(20*'=')
print(f'{nval} cpfs foram validos!')
print(20*'=')
print(f'{ninv} cpfs foram invalidos!')
print(20*'=')
mdval = (nval / nttl)*100
mdinval = (ninv / nttl)*100
print(f"a porcentagem de cpfs valido e: {mdval:.1f}%")
print(f"a porcentagem de cpfs invalido e: {mdinval:.1f}%")