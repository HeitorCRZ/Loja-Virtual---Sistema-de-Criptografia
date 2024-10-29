from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://DB_First:DB_Heitor060807@cluster0.xzfx3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
Banco = client['Gerenciamento_Inventario']
Produto = Banco['Produtos']
Fornecedor = Banco['Fornecedores']
Transacao = Banco['Trasações']

try:

    while True:  # Início do programa
        Escolher_Coleção = int(input(
            "Escolha a Coleção a ser manipulada:\n1-Produtos\n2-Fornecedores\n3-Trasações\n4-Sair\nR:"))  # Escolha da coleção a ser manipulada
        while Escolher_Coleção > 4 or Escolher_Coleção < 1:  # Teste se o valor recebido é válido
            print("=-" * 56)
            Escolher_Coleção = int(input("Escolha inválida!!!\n1-Produtos\n2-Fornecedores\n3-Trasações\n4-Sair\nR:"))
        print("=-" * 56)
        if Escolher_Coleção == 4:
            break

        Escolher_CRUD = int(
            input("Escolha a operação do CRUD:\n1-Create\n2-Read\n3-Update\n4-Delete\nR:"))  # Escolha operação CRUD
        while Escolher_CRUD > 4 or Escolher_CRUD < 1:  # Teste se o valor recebido é válido
            print("=-" * 56)
            Escolher_CRUD = int(input("Escolha inválida!!!\n1-Create\n2-Read\n3-Update\n4-Delete\nR:"))
        print("=-" * 56)

        while Escolher_Coleção == 1:  # Coleção Produtos
            print("\n\n")
            print(
                "---------------------------------------------> Coleção : Produtos <----------------------------------------------\n\n")

            while Escolher_CRUD == 1:  # Realizar a operação Create na Coleção: Produtos
                print("\n\n")
                print(
                    "---------------------------------------------> Operação : Create <----------------------------------------------")
                Nome_Produto = input("Digite o nome do produto:")
                Nome_Codigo = input("Digite o código do produto:")
                Nome_Quantidade = int(input("Digite a quantidade de produtos disponíveis:"))

                Produto.insert_one(  # Inserindo dados na coleção: Produtos
                    {
                        "Nome": Nome_Produto,
                        "Código": Nome_Codigo,
                        "Quantidade": Nome_Quantidade
                    }
                )
                print("=-" * 56)

                while True:  # Verificar se o usuário gostaria de adicionar mais campos ao registro
                    x = input(
                        "Gostaria de adicionar mais um campo ao registro do produto?\nSim --> S/s\nNão --> N/n\nR:")
                    if x.lower() == 'n':
                        break
                    elif x.lower() == 's':
                        Nome_Campo = input("Digite o nome do campo:")
                        Conteudo_Campo = input(f"Digite o conteúdo do campo {Nome_Campo}:")

                        Produto.update_one(  # Inserir no registro um novo campo
                            {"Código": Nome_Codigo},
                            {"$set": {Nome_Campo: Conteudo_Campo}}
                        )
                        print("=-" * 56)

                    else:
                        print("Resposta invalida!!!!!")
                        print("=-" * 56)

                print("=-" * 56)
                Escolher_CRUD = int(input(
                    "Escolha a operação do CRUD:\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))  # Escolha operação CRUD
                while Escolher_CRUD > 5 or Escolher_CRUD < 1:  # Teste se o valor recebido é válido
                    print("=-" * 56)
                    Escolher_CRUD = int(input("Escolha inválida!!!\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))
                print("=-" * 56)

            while Escolher_CRUD == 2:  # Realizar a operação Read na Coleção: Produtos
                print("\n\n")
                print(
                    "---------------------------------------------> Operação : Read <----------------------------------------------")

                Metodo_Read = int(input(
                    "Escolha como deve ser a pesquisa:\n1----->Por Codigo\n2----->Todos\nR:"))  # Usuario escolhero metodo de pesquisa
                while Metodo_Read > 2 or Metodo_Read < 1:  # Teste se o valor recebido é válido
                    print("=-" * 56)
                    Metodo_Read = int(input("Escolha inválida!!!\n1----->Por Codigo\n2----->Todos\nR:"))
                print("=-" * 56)

                if Metodo_Read == 1:  # Realizar o Read por Codígo
                    Selecionar_Codígo = input("Digite o codígo do produto :")
                    print("=-" * 56)
                    Resultado = Produto.find_one(  # Seleciona um produto pelo codígo
                        {
                            "Código": Selecionar_Codígo
                        }
                    )
                    if Resultado:  # Verifica se existe valor dentro da variavel
                        print(f"-----------------> Produto Selecionado : {Resultado['Nome']} <-----------------\n")
                        for chave, valor in Resultado.items():  # Imprimir todos dados dentro do registro
                            print(f"{chave}: {valor}")
                    else:
                        print("Produto não encontrado")

                if Metodo_Read == 2:  # Realizar o Read de todos
                    Resultado = Produto.find()  # Seleciona todos os produtos
                    Resultado = list(Resultado)  # Converte o cursor para uma lista para verificar se há resultados
                    if Resultado:  # Verifica se existe valor dentro da variável
                        cont = 1
                        for tupla in Resultado:
                            print("__" * 56)
                            print(f"-----------------> Produto {cont}º : {tupla['Nome']} <-----------------\n")
                            cont += 1
                            for chave, valor in tupla.items():  # Imprimir todos os dados dentro do registro
                                print(f"{chave}: {valor}")
                    else:
                        print("Não existem produtos cadastrados")

                print("=-" * 56)
                Escolher_CRUD = int(input(
                    "Escolha a operação do CRUD:\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))  # Escolha operação CRUD
                while Escolher_CRUD > 5 or Escolher_CRUD < 1:  # Teste se o valor recebido é válido
                    print("=-" * 56)
                    Escolher_CRUD = int(input("Escolha inválida!!!\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))
                print("=-" * 56)

            while Escolher_CRUD == 3:  # Realizar a operação Update na Coleção: Produtos
                print("\n\n")
                print(
                    "---------------------------------------------> Operação : Update <----------------------------------------------")

                Exibir_Lista = int(input("Exibir lista com os produtos ?\n1----->Não, é desnecessario\n2----->Sim, é necessario\nR:"))  # Verificar se o usuario precisa consultar os produtos
                while Exibir_Lista > 2 or Exibir_Lista < 1:  # Teste se o valor recebido é válido
                    print("=-" * 56)
                    Exibir_Lista = int(
                        input("Escolha inválida!!!\n1----->Não é necessario\n2----->Sim é necessario\nR:"))
                print("=-" * 56)

                if Exibir_Lista == 1:  # Realizar o Update sem exibir lista
                    Selecionar_Codígo = input("Digite o código do produto: ")  # Recebe o codígo
                    print("=-" * 56)

                    Resultado = Produto.find_one({
                        "Código": Selecionar_Codígo
                    })

                    if Resultado:  # Verifica se existe valor dentro da variável
                        print(f"-----------------> Produto a ser atualizado: {Resultado['Nome']} <-----------------\n")
                        for chave, valor in Resultado.items():  # Imprimir todos dados dentro do registro
                            print(f"{chave}: {valor}")
                        print("=-" * 56)

                        while True:
                            Campo_Update = input("\nEscolha o campo a ser atualizado: ")

                            if Campo_Update not in Resultado:
                                print("Campo não encontrado no documento.")
                                continue

                            Update_Conteudo = input(f"Novo Dado do campo {Campo_Update}: ")
                            print("=-" * 56)

                            Produto.update_one(  # Atuliza o rpoduto pelo codígo
                                {"Código": Selecionar_Codígo},
                                {"$set": {Campo_Update: Update_Conteudo}}
                            )

                            print("----------------> ATUALIZADO COM SUCESSO <----------------\n")
                            print("=-" * 56)

                            Update_Continuar = int(input("Atualizar mais 1 campo?\n1---->Sim\n2---->Não\nR:"))
                            while Update_Continuar > 2 or Update_Continuar < 1:  # Verificação se o valor recebido é válido
                                print("=-" * 56)
                                Update_Continuar = int(input("Escolha inválida!!!\n1---->Sim\n2---->Não\nR:"))
                            if Update_Continuar == 2:
                                break
                    else:
                        print("Produto não encontrado")
                        print("=-" * 56)

                if Exibir_Lista == 2:  # Realizar o Update exibindo lista
                    Resultado = Produto.find()  # Seleciona todos os produtos
                    Resultado = list(Resultado)  # Converte o cursor para uma lista para verificar se há resultados
                    if Resultado:  # Verifica se existe valor dentro da variável
                        cont = 1
                        for tupla in Resultado:
                            print("__" * 56)
                            print(f"-----------------> Produto {cont}º : {tupla['Nome']} <-----------------\n")
                            cont += 1
                            for chave, valor in tupla.items():  # Imprimir todos os dados dentro do registro
                                print(f"{chave}: {valor}")
                    else:
                        print("Não existem produtos cadastrados")
                    print("=-" * 56)

                    Selecionar_Codígo = input("Digite o código do produto: ")  # Converte para inteiro
                    print("=-" * 56)

                    Resultado = Produto.find_one({  # Resultado recebe o registro com o codigo determinado pelo usuario
                        "Código": Selecionar_Codígo
                    })

                    if Resultado:  # Verifica se existe valor dentro da variável
                        print(f"-----------------> Produto a ser atualizado: {Resultado['Nome']} <-----------------\n")
                        for chave, valor in Resultado.items():  # Imprimir todos dados dentro do registro
                            print(f"{chave}: {valor}")
                        print("=-" * 56)

                        while True:
                            Campo_Update = input("\nEscolha o campo a ser atualizado: ")

                            if Campo_Update not in Resultado:  # verifica se o campo existe
                                print("Campo não encontrado no documento.")
                                continue

                            Update_Conteudo = input(
                                f"Novo Dado do campo {Campo_Update}: ")  # Usuario escolhe o novo dado
                            print("=-" * 56)

                            Produto.update_one(  # Atualiza o produto escolhido
                                {"Código": Selecionar_Codígo},
                                {"$set": {Campo_Update: Update_Conteudo}}
                            )

                            print("----------------> ATUALIZADO COM SUCESSO <----------------\n")
                            print("=-" * 56)

                            Update_Continuar = int(input("Adicionar mais 1 campo?\n1---->Sim\n2---->Não\nR:"))
                            while Update_Continuar > 2 or Update_Continuar < 1:  # Verificação se o valor recebido é válido
                                print("=-" * 56)
                                Update_Continuar = int(input("Escolha inválida!!!\n1---->Sim\n2---->Não\nR:"))
                            if Update_Continuar == 2:
                                break
                    else:
                        print("Produto não encontrado")
                        print("=-" * 56)

                print("=-" * 56)
                Escolher_CRUD = int(input(
                    "Escolha a operação do CRUD:\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))  # Escolha operação CRUD
                while Escolher_CRUD > 5 or Escolher_CRUD < 1:  # Teste se o valor recebido é válido
                    print("=-" * 56)
                    Escolher_CRUD = int(input("Escolha inválida!!!\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))
                print("=-" * 56)

            while Escolher_CRUD == 4:  # Realizar a operação Delete na Coleção: Produtos
                print("\n\n")
                print(
                    "---------------------------------------------> Operação : Delete <----------------------------------------------")

                Metodo_Exclusão = int(input(
                    "Escolha uma das opções abaixo :\n1----->Deletar por codígo\n2----->Deletar por um campo alternativo\nR:"))  # Verificar o metodo de exclusão
                while Metodo_Exclusão > 2 or Metodo_Exclusão < 1:  # Teste se o valor recebido é válido
                    print("=-" * 56)
                    Metodo_Exclusão = int(input(
                        "Escolha inválida!!!\n1----->Deletar por codígo\n2----->Deletar por um campo alternativo\nR:"))
                print("=-" * 56)

                if Metodo_Exclusão == 1:  # Realizar o Delete por codígo
                    Selecionar_Codígo = input("Digite o código do produto: ")  # Recebe o codígo
                    print("=-" * 56)

                    Resultado = Produto.find_one({  # Selecionar produto pelo codígo
                        "Código": Selecionar_Codígo
                    })

                    if Resultado:  # Verifica se existe valor dentro da variável
                        print(f"-----------------> Produto a ser Deletado {Resultado['Nome']} <-----------------\n")
                        for chave, valor in Resultado.items():  # Imprimir todos dados dentro do registro
                            print(f"{chave}: {valor}")
                        print("=-" * 56)

                        Confirmação = input("Digite 'CONFIRMAR' para concluir a ação :")
                        if Confirmação == "CONFIRMAR":  # Valida a exclusão
                            Produto.delete_one(
                                {
                                    "Código": Selecionar_Codígo
                                }
                            )
                            print("----------------> DELETADO COM SUCESSO <----------------\n")
                        else:
                            print("----------------> ERRO AO DELETAR!!!! <----------------\n")
                        print("=-" * 56)
                    else:
                        print("Produto não encontrado")
                        print("=-" * 56)

                if Metodo_Exclusão == 2:  # Realizar o Delete por campo alternativo
                    Deletar_Campo = input(
                        "Digite o campo pelo qual você quer deletar: ")  # Campo pelo qual vai ser executado o delete
                    Deletar_Dado = input(
                        "Digite o dado pelo qual você quer deletar: ")  # Dado pelo qual vai ser executado o delete
                    print("=-" * 56)
                    Resultado = Produto.find(  # Seleciona todos os produtos com os daods escolhidos pelo usuario
                        {
                            Deletar_Campo: Deletar_Dado
                        }
                    )
                    Resultado = list(Resultado)  # Converte o cursor para uma lista para verificar se há resultados

                    if Resultado:  # Verifica se existe valor dentro da variável
                        cont = 1
                        for tupla in Resultado:
                            print("__" * 56)
                            print(f"-----------------> Produto {cont}º : {tupla['Nome']} <-----------------\n")
                            cont += 1
                            for chave, valor in tupla.items():  # Imprimir todos os dados dentro do registro
                                print(f"{chave}: {valor}")
                        print("=-" * 56)
                        Confirmação = input("Digite 'CONFIRMAR' para excluir os registros selecionados acima :")
                        print("=-" * 56)
                        if Confirmação == "CONFIRMAR":  # Valida a exclusão
                            Produto.delete_many(
                                {
                                    Deletar_Campo: Deletar_Dado
                                }
                            )
                            print("----------------> DELETADO COM SUCESSO <----------------\n")
                        else:
                            print("----------------> ERRO AO DELETAR!!!! <----------------\n")
                    else:
                        print("Não existem produtos cadastrados com essas credenciais")

                print("=-" * 56)
                Escolher_CRUD = int(input(
                    "Escolha a operação do CRUD:\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))  # Escolha operação CRUD
                while Escolher_CRUD > 5 or Escolher_CRUD < 1:  # Teste se o valor recebido é válido
                    print("=-" * 56)
                    Escolher_CRUD = int(input("Escolha inválida!!!\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))
                print("=-" * 56)

            if Escolher_CRUD == 5:  # Teste de saída da coleção
                break

        while Escolher_Coleção == 2:  # Coleção Fornecedor
            print("\n\n")
            print(
                "---------------------------------------------> Coleção : Fornecedor <----------------------------------------------\n\n")

            while Escolher_CRUD == 1:  # Realizar a operação Create na Coleção: Fornecedor
                print("\n\n")
                print(
                    "---------------------------------------------> Operação : Create <----------------------------------------------")
                Nome_Fornecedor = input("Digite o nome do fornecedor:")
                Nome_Codigo = input("Digite o código do fornecedor:")
                Nome_Contato = input("Digite o contato do fornecedor:")

                Fornecedor.insert_one(  # Inserindo dados na coleção: Fornecedor
                    {
                        "Nome": Nome_Fornecedor,
                        "Código": Nome_Codigo,
                        "Contato": Nome_Contato
                    }
                )
                print("=-" * 56)

                while True:  # Verificar se o usuário gostaria de adicionar mais campos ao registro
                    x = input(
                        "Gostaria de adicionar mais um campo ao registro do fornecedor?\nSim --> S/s\nNão --> N/n\nR:")
                    if x.lower() == 'n':
                        break
                    elif x.lower() == 's':
                        Nome_Campo = input("Digite o nome do campo:")
                        Conteudo_Campo = input(f"Digite o conteúdo do campo {Nome_Campo}:")

                        Fornecedor.update_one(  # Inserir no registro um novo campo
                            {"Código": Nome_Codigo},
                            {"$set": {Nome_Campo: Conteudo_Campo}}
                        )
                        print("=-" * 56)

                    else:
                        print("Resposta invalida!!!!!")
                        print("=-" * 56)

                print("=-" * 56)
                Escolher_CRUD = int(input(
                    "Escolha a operação do CRUD:\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))  # Escolha operação CRUD
                while Escolher_CRUD > 5 or Escolher_CRUD < 1:  # Teste se o valor recebido é válido
                    print("=-" * 56)
                    Escolher_CRUD = int(input("Escolha inválida!!!\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))
                print("=-" * 56)

            while Escolher_CRUD == 2:  # Realizar a operação Read na Coleção: Fornecedor
                print("\n\n")
                print(
                    "---------------------------------------------> Operação : Read <----------------------------------------------")

                Metodo_Read = int(input(
                    "Escolha como deve ser a pesquisa:\n1----->Por Codigo\n2----->Todos\nR:"))  # Usuario escolhero metodo de pesquisa
                while Metodo_Read > 2 or Metodo_Read < 1:  # Teste se o valor recebido é válido
                    print("=-" * 56)
                    Metodo_Read = int(input("Escolha inválida!!!\n1----->Por Codigo\n2----->Todos\nR:"))
                print("=-" * 56)

                if Metodo_Read == 1:  # Realizar o Read por Codígo
                    Selecionar_Codígo = input("Digite o codígo do fornecedor :")
                    print("=-" * 56)
                    Resultado = Fornecedor.find_one(  # Seleciona um fornecedor pelo codígo
                        {
                            "Código": Selecionar_Codígo
                        }
                    )
                    if Resultado:  # Verifica se existe valor dentro da variavel
                        print(f"-----------------> Fornecedor Selecionado : {Resultado['Nome']} <-----------------\n")
                        for chave, valor in Resultado.items():  # Imprimir todos dados dentro do registro
                            print(f"{chave}: {valor}")
                    else:
                        print("Fornecedor não encontrado")

                if Metodo_Read == 2:  # Realizar o Read de todos
                    Resultado = Fornecedor.find()  # Seleciona todos os fornecedores
                    Resultado = list(Resultado)  # Converte o cursor para uma lista para verificar se há resultados
                    if Resultado:  # Verifica se existe valor dentro da variável
                        cont = 1
                        for tupla in Resultado:
                            print("__" * 56)
                            print(f"-----------------> Fornecedor {cont}º : {tupla['Nome']} <-----------------\n")
                            cont += 1
                            for chave, valor in tupla.items():  # Imprimir todos os dados dentro do registro
                                print(f"{chave}: {valor}")
                    else:
                        print("Não existem fornecedores cadastrados")

                print("=-" * 56)
                Escolher_CRUD = int(input(
                    "Escolha a operação do CRUD:\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))  # Escolha operação CRUD
                while Escolher_CRUD > 5 or Escolher_CRUD < 1:  # Teste se o valor recebido é válido
                    print("=-" * 56)
                    Escolher_CRUD = int(input("Escolha inválida!!!\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))
                print("=-" * 56)

            while Escolher_CRUD == 3:  # Realizar a operação Update na Coleção: Fornecedor
                print("\n\n")
                print(
                    "---------------------------------------------> Operação : Update <----------------------------------------------")

                Exibir_Lista = int(input(
                    "Exibir lista com os fornecedores ?\n1----->Não, é desnecessario\n2----->Sim, é necessario\nR:"))  # Verificar se o usuario precisa consultar os fornecedores
                while Exibir_Lista > 2 or Exibir_Lista < 1:  # Teste se o valor recebido é válido
                    print("=-" * 56)
                    Exibir_Lista = int(
                        input("Escolha inválida!!!\n1----->Não é necessario\n2----->Sim é necessario\nR:"))
                print("=-" * 56)

                if Exibir_Lista == 1:  # Realizar o Update sem exibir lista
                    Selecionar_Codígo = input("Digite o código do fornecedor: ")  # Recebe o codígo
                    print("=-" * 56)

                    Resultado = Fornecedor.find_one({
                        "Código": Selecionar_Codígo
                    })

                    if Resultado:  # Verifica se existe valor dentro da variável
                        print(
                            f"-----------------> Fornecedor a ser atualizado: {Resultado['Nome']} <-----------------\n")
                        for chave, valor in Resultado.items():  # Imprimir todos dados dentro do registro
                            print(f"{chave}: {valor}")
                        print("=-" * 56)

                        while True:
                            Campo_Update = input("\nEscolha o campo a ser atualizado: ")

                            if Campo_Update not in Resultado:
                                print("Campo não encontrado no documento.")
                                continue

                            Update_Conteudo = input(f"Novo Dado do campo {Campo_Update}: ")
                            print("=-" * 56)

                            Fornecedor.update_one(  # Atualiza o fornecedor pelo codígo
                                {"Código": Selecionar_Codígo},
                                {"$set": {Campo_Update: Update_Conteudo}}
                            )

                            print("----------------> ATUALIZADO COM SUCESSO <----------------\n")
                            print("=-" * 56)

                            Update_Continuar = int(input("Atualizar mais 1 campo?\n1---->Sim\n2---->Não\nR:"))
                            while Update_Continuar > 2 or Update_Continuar < 1:  # Verificação se o valor recebido é válido
                                print("=-" * 56)
                                Update_Continuar = int(input("Escolha inválida!!!\n1---->Sim\n2---->Não\nR:"))
                            if Update_Continuar == 2:
                                break
                    else:
                        print("Fornecedor não encontrado")
                        print("=-" * 56)

                if Exibir_Lista == 2:  # Realizar o Update exibindo lista
                    Resultado = Fornecedor.find()  # Seleciona todos os fornecedores
                    Resultado = list(Resultado)  # Converte o cursor para uma lista para verificar se há resultados
                    if Resultado:  # Verifica se existe valor dentro da variável
                        cont = 1
                        for tupla in Resultado:
                            print("__" * 56)
                            print(f"-----------------> Fornecedor {cont}º : {tupla['Nome']} <-----------------\n")
                            cont += 1
                            for chave, valor in tupla.items():  # Imprimir todos os dados dentro do registro
                                print(f"{chave}: {valor}")
                    else:
                        print("Não existem fornecedores cadastrados")
                    print("=-" * 56)

                    Selecionar_Codígo = input("Digite o código do fornecedor: ")  # Converte para inteiro
                    print("=-" * 56)

                    Resultado = Fornecedor.find_one(
                        {  # Resultado recebe o registro com o codigo determinado pelo usuario
                            "Código": Selecionar_Codígo
                        })

                    if Resultado:  # Verifica se existe valor dentro da variável
                        print(
                            f"-----------------> Fornecedor a ser atualizado: {Resultado['Nome']} <-----------------\n")
                        for chave, valor in Resultado.items():  # Imprimir todos dados dentro do registro
                            print(f"{chave}: {valor}")
                        print("=-" * 56)

                        while True:
                            Campo_Update = input("\nEscolha o campo a ser atualizado: ")

                            if Campo_Update not in Resultado:
                                print("Campo não encontrado no documento.")
                                continue

                            Update_Conteudo = input(f"Novo Dado do campo {Campo_Update}: ")
                            print("=-" * 56)

                            Fornecedor.update_one(  # Atualiza o fornecedor pelo codígo
                                {"Código": Selecionar_Codígo},
                                {"$set": {Campo_Update: Update_Conteudo}}
                            )

                            print("----------------> ATUALIZADO COM SUCESSO <----------------\n")
                            print("=-" * 56)

                            Update_Continuar = int(input("Atualizar mais 1 campo?\n1---->Sim\n2---->Não\nR:"))
                            while Update_Continuar > 2 or Update_Continuar < 1:  # Verificação se o valor recebido é válido
                                print("=-" * 56)
                                Update_Continuar = int(input("Escolha inválida!!!\n1---->Sim\n2---->Não\nR:"))
                            if Update_Continuar == 2:
                                break
                    else:
                        print("Fornecedor não encontrado")
                        print("=-" * 56)

                print("=-" * 56)
                Escolher_CRUD = int(input(
                    "Escolha a operação do CRUD:\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))  # Escolha operação CRUD
                while Escolher_CRUD > 5 or Escolher_CRUD < 1:  # Teste se o valor recebido é válido
                    print("=-" * 56)
                    Escolher_CRUD = int(input("Escolha inválida!!!\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))
            print("=-" * 56)

            while Escolher_CRUD == 4:  # Realizar a operação Delete na Coleção: Fornecedor
                print("\n\n")
                print(
                    "---------------------------------------------> Operação : Delete <----------------------------------------------")

                Metodo_Exclusão = int(input(
                    "Escolha uma das opções abaixo :\n1----->Deletar por código\n2----->Deletar por um campo alternativo\nR:"))  # Verificar o método de exclusão
                while Metodo_Exclusão > 2 or Metodo_Exclusão < 1:  # Teste se o valor recebido é válido
                    print("=-" * 56)
                    Metodo_Exclusão = int(input(
                        "Escolha inválida!!!\n1----->Deletar por código\n2----->Deletar por um campo alternativo\nR:"))
                print("=-" * 56)

                if Metodo_Exclusão == 1:  # Realizar o Delete por código
                    Selecionar_Codigo = input("Digite o código do fornecedor: ")  # Recebe o código
                    print("=-" * 56)

                    Resultado = Fornecedor.find_one({"Código": Selecionar_Codigo})  # Selecionar fornecedor pelo código

                    if Resultado:  # Verifica se existe valor dentro da variável
                        print(f"-----------------> Fornecedor a ser Deletado: {Resultado['Nome']} <-----------------\n")
                        for chave, valor in Resultado.items():  # Imprimir todos os dados dentro do registro
                            print(f"{chave}: {valor}")
                        print("=-" * 56)

                        Confirmacao = input("Digite 'CONFIRMAR' para concluir a ação :")
                        if Confirmacao == "CONFIRMAR":  # Valida a exclusão
                            Fornecedor.delete_one({"Código": Selecionar_Codigo})
                            print("----------------> DELETADO COM SUCESSO <----------------\n")
                        else:
                            print("----------------> ERRO AO DELETAR!!!! <----------------\n")
                        print("=-" * 56)
                    else:
                        print("Fornecedor não encontrado")
                        print("=-" * 56)

                if Metodo_Exclusão == 2:  # Realizar o Delete por campo alternativo
                    Deletar_Campo = input(
                        "Digite o campo pelo qual você quer deletar: ")  # Campo pelo qual vai ser executado o delete
                    Deletar_Dado = input(
                        "Digite o dado pelo qual você quer deletar: ")  # Dado pelo qual vai ser executado o delete
                    print("=-" * 56)
                    Resultado = Fornecedor.find({
                        Deletar_Campo: Deletar_Dado})  # Seleciona todos os fornecedores com os dados escolhidos pelo usuário
                    Resultado = list(Resultado)  # Converte o cursor para uma lista para verificar se há resultados

                    if Resultado:  # Verifica se existe valor dentro da variável
                        cont = 1
                        for tupla in Resultado:
                            print("__" * 56)
                            print(f"-----------------> Fornecedor {cont}º : {tupla['Nome']} <-----------------\n")
                            cont += 1
                            for chave, valor in tupla.items():  # Imprimir todos os dados dentro do registro
                                print(f"{chave}: {valor}")
                        print("=-" * 56)
                        Confirmacao = input("Digite 'CONFIRMAR' para excluir os registros selecionados acima :")
                        print("=-" * 56)
                        if Confirmacao == "CONFIRMAR":  # Valida a exclusão
                            Fornecedor.delete_many({Deletar_Campo: Deletar_Dado})
                            print("----------------> DELETADO COM SUCESSO <----------------\n")
                        else:
                            print("----------------> ERRO AO DELETAR!!!! <----------------\n")
                    else:
                        print("Não existem fornecedores cadastrados com essas credenciais")

                print("=-" * 56)
                Escolher_CRUD = int(input(
                    "Escolha a operação do CRUD:\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))  # Escolha operação CRUD
                while Escolher_CRUD > 5 or Escolher_CRUD < 1:  # Teste se o valor recebido é válido
                    print("=-" * 56)
                    Escolher_CRUD = int(input("Escolha inválida!!!\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))
                print("=-" * 56)

            if Escolher_CRUD == 5:  # Teste de saída da coleção
                break








        while Escolher_Coleção == 3:  # Coleção Transação
            print("\n\n")
            print(
                "---------------------------------------------> Coleção : Transação <----------------------------------------------\n\n")

            while Escolher_CRUD == 1:  # Realizar a operação Create na Coleção: Transação
                print("\n\n")
                print(
                    "---------------------------------------------> Operação : Create <----------------------------------------------")
                Nome_Produto = input("Digite o nome do produto: ")
                Nome_Codigo = input("Digite o código da transação: ")
                Nome_Quantidade = int(input("Digite a quantidade da transação: "))  # Converta para inteiro
                Nome_ES = input("Digite se foi entrada ou saída: EX--->(ENTRADA/SAÍDA): ").strip().upper()
                Nome_Data = input("Digite a data da transação: ")

                Transacao.insert_one({ # Inserindo dados na coleção: Transação
                    "Produto": Nome_Produto,
                    "Código": Nome_Codigo,
                    "Quantidade": Nome_Quantidade,
                    "ES": Nome_ES,
                    "Data": Nome_Data
                })

                print("=-" * 56)

                if Nome_ES == "ENTRADA":  # Atualiza a tabela produtos com a quantidade certa de produtos
                    Resultado = Produto.find_one({ # Seleciona o registro com o nome do produto
                        "Nome": Nome_Produto
                    })
                    if Resultado: #  Verifica se tem valor na variavel
                        Novo_QTD = Resultado.get('Quantidade', 0) + Nome_Quantidade # Recupera o campo "Quantidade" e atribui a uma nova variavel
                        Produto.update_one( #Atualiza a coleção Produtos
                            {"Nome": Nome_Produto},
                            {"$set": {"Quantidade": Novo_QTD}}
                        )
                else: # Caso for saida
                    Resultado = Produto.find_one({ # Seleciona o registro com o nome do produto
                        "Nome": Nome_Produto
                    })
                    if Resultado: #  Verifica se tem valor na variavel
                        Novo_QTD = Resultado.get('Quantidade', 0) - Nome_Quantidade  # Recupera o campo "Quantidade" e atribui a uma nova variavel
                        Produto.update_one( #Atualiza a coleção Produtos
                            {"Nome": Nome_Produto},
                            {"$set": {"Quantidade": Novo_QTD}}
                        )

                while True:  # Verificar se o usuário gostaria de adicionar mais campos ao registro
                    x = input(
                        "Gostaria de adicionar mais um campo ao registro da transação?\nSim --> S/s\nNão --> N/n\nR:")
                    if x.lower() == 'n':
                        break
                    elif x.lower() == 's':
                        Nome_Campo = input("Digite o nome do campo:")
                        Conteudo_Campo = input(f"Digite o conteúdo do campo {Nome_Campo}:")

                        Transacao.update_one(  # Inserir no registro um novo campo
                            {"Código": Nome_Codigo},
                            {"$set": {Nome_Campo: Conteudo_Campo}}
                        )
                        print("=-" * 56)

                    else:
                        print("Resposta inválida!!!!!")
                        print("=-" * 56)

                print("=-" * 56)
                Escolher_CRUD = int(input(
                    "Escolha a operação do CRUD:\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))  # Escolha operação CRUD
                while Escolher_CRUD > 5 or Escolher_CRUD < 1:  # Teste se o valor recebido é válido
                    print("=-" * 56)
                    Escolher_CRUD = int(input("Escolha inválida!!!\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))
                print("=-" * 56)

            while Escolher_CRUD == 2:  # Realizar a operação Read na Coleção: Transação
                print("\n\n")
                print(
                    "---------------------------------------------> Operação : Read <----------------------------------------------")

                Metodo_Read = int(input("Escolha como deve ser a pesquisa:\n1----->Por Código\n2----->Todos\nR:"))  # Usuário escolhe método de pesquisa
                while Metodo_Read > 2 or Metodo_Read < 1:  # Teste se o valor recebido é válido
                    print("=-" * 56)
                    Metodo_Read = int(input("Escolha inválida!!!\n1----->Por Código\n2----->Todos\nR:"))
                print("=-" * 56)

                if Metodo_Read == 1:  # Realizar o Read por Código
                    Selecionar_Codigo = input("Digite o código da transação:")
                    print("=-" * 56)
                    Resultado = Transacao.find_one(  # Seleciona uma transação pelo código
                        {
                            "Código": Selecionar_Codigo
                        }
                    )
                    if Resultado:  # Verifica se existe valor dentro da variável
                        print(f"-----------------> Transação Selecionada : {Resultado['Produto']} <-----------------\n")
                        for chave, valor in Resultado.items():  # Imprimir todos dados dentro do registro
                            print(f"{chave}: {valor}")
                    else:
                        print("Transação não encontrada")

                if Metodo_Read == 2:  # Realizar o Read de todos
                    Resultado = Transacao.find()  # Seleciona todas as transações
                    Resultado = list(Resultado)  # Converte o cursor para uma lista para verificar se há resultados
                    if Resultado:  # Verifica se existe valor dentro da variável
                        cont = 1
                        for tupla in Resultado:
                            print("__" * 56)
                            print(f"-----------------> Transação {cont}º : {tupla['Produto']} <-----------------\n")
                            cont += 1
                            for chave, valor in tupla.items():  # Imprimir todos os dados dentro do registro
                                print(f"{chave}: {valor}")
                    else:
                        print("Não existem transações cadastradas")

                print("=-" * 56)
                Escolher_CRUD = int(input(
                    "Escolha a operação do CRUD:\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))  # Escolha operação CRUD
                while Escolher_CRUD > 5 or Escolher_CRUD < 1:  # Teste se o valor recebido é válido
                    print("=-" * 56)
                    Escolher_CRUD = int(input("Escolha inválida!!!\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))
                print("=-" * 56)

            while Escolher_CRUD == 3:  # Realizar a operação Update na Coleção: Transação
                print("\n\n")
                print(
                    "---------------------------------------------> Operação : Update <----------------------------------------------")

                Exibir_Lista = int(input(
                    "Exibir lista com as transações?\n1----->Não, é desnecessário\n2----->Sim, é necessário\nR:"))  # Verificar se o usuário precisa consultar as transações
                while Exibir_Lista > 2 or Exibir_Lista < 1:  # Teste se o valor recebido é válido
                    print("=-" * 56)
                    Exibir_Lista = int(
                        input("Escolha inválida!!!\n1----->Não é necessário\n2----->Sim é necessário\nR:"))
                print("=-" * 56)

                if Exibir_Lista == 1:  # Realizar o Update sem exibir lista
                    Selecionar_Codigo = input("Digite o código da transação: ")  # Recebe o código
                    print("=-" * 56)

                    Resultado = Transacao.find_one({
                        "Código": Selecionar_Codigo
                    })

                    if Resultado:  # Verifica se existe valor dentro da variável
                        print(
                            f"-----------------> Transação a ser atualizada: {Resultado['Produto']} <-----------------\n")
                        for chave, valor in Resultado.items():  # Imprimir todos os dados dentro do registro
                            print(f"{chave}: {valor}")
                        print("=-" * 56)

                        while True:
                            Campo_Update = input("\nEscolha o campo a ser atualizado: ")

                            if Campo_Update not in Resultado:
                                print("Campo não encontrado no documento.")
                                continue

                            Update_Conteudo = input(f"Novo Dado do campo {Campo_Update}: ")
                            print("=-" * 56)

                            Transacao.update_one(  # Atualiza a transação pelo código
                                {"Código": Selecionar_Codigo},
                                {"$set": {Campo_Update: Update_Conteudo}}
                            )

                            print("----------------> ATUALIZADO COM SUCESSO <----------------\n")
                            print("=-" * 56)

                            Update_Continuar = int(input("Atualizar mais 1 campo?\n1---->Sim\n2---->Não\nR:"))
                            while Update_Continuar > 2 or Update_Continuar < 1:  # Verificação se o valor recebido é válido
                                print("=-" * 56)
                                Update_Continuar = int(input("Escolha inválida!!!\n1---->Sim\n2---->Não\nR:"))
                            if Update_Continuar == 2:
                                break
                    else:
                        print("Transação não encontrada")
                        print("=-" * 56)

                if Exibir_Lista == 2:  # Realizar o Update exibindo lista
                    Resultado = Transacao.find()  # Seleciona todas as transações
                    Resultado = list(Resultado)  # Converte o cursor para uma lista para verificar se há resultados
                    if Resultado:  # Verifica se existe valor dentro da variável
                        cont = 1
                        for tupla in Resultado:
                            print("__" * 56)
                            print(f"-----------------> Transação {cont}º : {tupla['Produto']} <-----------------\n")
                            cont += 1
                            for chave, valor in tupla.items():  # Imprimir todos os dados dentro do registro
                                print(f"{chave}: {valor}")
                    else:
                        print("Não existem transações cadastradas")
                    print("=-" * 56)

                    Selecionar_Codigo = input("Digite o código da transação: ")  # Converte para inteiro
                    print("=-" * 56)

                    Resultado = Transacao.find_one(
                        {  # Resultado recebe o registro com o código determinado pelo usuário
                            "Código": Selecionar_Codigo
                        })

                    if Resultado:  # Verifica se existe valor dentro da variável
                        print(
                            f"-----------------> Transação a ser atualizada: {Resultado['Produto']} <-----------------\n")
                        for chave, valor in Resultado.items():  # Imprimir todos os dados dentro do registro
                            print(f"{chave}: {valor}")
                        print("=-" * 56)

                        while True:
                            Campo_Update = input("\nEscolha o campo a ser atualizado: ")

                            if Campo_Update not in Resultado:
                                print("Campo não encontrado no documento.")
                                continue

                            Update_Conteudo = input(f"Novo Dado do campo {Campo_Update}: ")
                            print("=-" * 56)

                            Transacao.update_one(  # Atualiza a transação pelo código
                                {"Código": Selecionar_Codigo},
                                {"$set": {Campo_Update: Update_Conteudo}}
                            )

                            print("----------------> ATUALIZADO COM SUCESSO <----------------\n")
                            print("=-" * 56)

                            Update_Continuar = int(input("Atualizar mais 1 campo?\n1---->Sim\n2---->Não\nR:"))
                            while Update_Continuar > 2 or Update_Continuar < 1:  # Verificação se o valor recebido é válido
                                print("=-" * 56)
                                Update_Continuar = int(input("Escolha inválida!!!\n1---->Sim\n2---->Não\nR:"))
                            if Update_Continuar == 2:
                                break
                    else:
                        print("Transação não encontrada")
                        print("=-" * 56)

                print("=-" * 56)
                Escolher_CRUD = int(input(
                    "Escolha a operação do CRUD:\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))  # Escolha operação CRUD
                while Escolher_CRUD > 5 or Escolher_CRUD < 1:  # Teste se o valor recebido é válido
                    print("=-" * 56)
                    Escolher_CRUD = int(input("Escolha inválida!!!\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))
                print("=-" * 56)

            while Escolher_CRUD == 4:  # Realizar a operação Delete na Coleção: Transação
                print("\n\n")
                print(
                    "---------------------------------------------> Operação : Delete <----------------------------------------------")

                Metodo_Exclusão = int(input(
                    "Escolha uma das opções abaixo :\n1----->Deletar por código\n2----->Deletar por um campo alternativo\nR:"))  # Verificar o método de exclusão
                while Metodo_Exclusão > 2 or Metodo_Exclusão < 1:  # Teste se o valor recebido é válido
                    print("=-" * 56)
                    Metodo_Exclusão = int(input(
                        "Escolha inválida!!!\n1----->Deletar por código\n2----->Deletar por um campo alternativo\nR:"))
                print("=-" * 56)

                if Metodo_Exclusão == 1:  # Realizar o Delete por código
                    Selecionar_Codigo = input("Digite o código da transação: ")  # Recebe o código
                    print("=-" * 56)

                    Resultado = Transacao.find_one({"Código": Selecionar_Codigo})  # Seleciona transação pelo código

                    if Resultado:  # Verifica se existe valor dentro da variável
                        print(f"-----------------> Transação a ser Deletada: {Resultado['Produto']} <-----------------\n")
                        for chave, valor in Resultado.items():  # Imprimir todos os dados dentro do registro
                            print(f"{chave}: {valor}")
                        print("=-" * 56)

                        Confirmacao = input("Digite 'CONFIRMAR' para concluir a ação :")
                        if Confirmacao == "CONFIRMAR":  # Valida a exclusão
                            Transacao.delete_one({"Código": Selecionar_Codigo})
                            print("----------------> DELETADO COM SUCESSO <----------------\n")
                        else:
                            print("----------------> ERRO AO DELETAR!!!! <----------------\n")
                        print("=-" * 56)
                    else:
                        print("Transação não encontrada")
                        print("=-" * 56)

                if Metodo_Exclusão == 2:  # Realizar o Delete por campo alternativo
                    Deletar_Campo = input(
                        "Digite o campo pelo qual você quer deletar: ")  # Campo pelo qual vai ser executado o delete
                    Deletar_Dado = input(
                        "Digite o dado pelo qual você quer deletar: ")  # Dado pelo qual vai ser executado o delete
                    print("=-" * 56)
                    Resultado = Transacao.find({
                        Deletar_Campo: Deletar_Dado})  # Seleciona todas as transações com os dados escolhidos pelo usuário
                    Resultado = list(Resultado)  # Converte o cursor para uma lista para verificar se há resultados

                    if Resultado:  # Verifica se existe valor dentro da variável
                        cont = 1
                        for tupla in Resultado:
                            print("__" * 56)
                            print(f"-----------------> Transação {cont}º : {tupla['Produto']} <-----------------\n")
                            cont += 1
                            for chave, valor in tupla.items():  # Imprimir todos os dados dentro do registro
                                print(f"{chave}: {valor}")
                        print("=-" * 56)
                        Confirmacao = input("Digite 'CONFIRMAR' para excluir os registros selecionados acima :")
                        print("=-" * 56)
                        if Confirmacao == "CONFIRMAR":  # Valida a exclusão
                            Transacao.delete_many({Deletar_Campo: Deletar_Dado})
                            print("----------------> DELETADO COM SUCESSO <----------------\n")
                        else:
                            print("----------------> ERRO AO DELETAR!!!! <----------------\n")
                    else:
                        print("Não existem transações cadastradas com essas credenciais")

                print("=-" * 56)
                Escolher_CRUD = int(input(
                    "Escolha a operação do CRUD:\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))  # Escolha operação CRUD
                while Escolher_CRUD > 5 or Escolher_CRUD < 1:  # Teste se o valor recebido é válido
                    print("=-" * 56)
                    Escolher_CRUD = int(input("Escolha inválida!!!\n1-Create\n2-Read\n3-Update\n4-Delete\n5-Sair\nR:"))
                print("=-" * 56)

            if Escolher_CRUD == 5:  # Teste de saída da coleção
                break




except Exception as e:
    print(f"Ocorreu um erro: {e}")
