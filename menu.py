import operacao
import this
this.opcao = -1

def menu():
    print('\n---------- MENU----------'           +
          'Escolha uma das opções abaixo: \n\n'   +
          '1. Cadastrar\n'                        +
          '2. Consultar\n'                        +
          '3. Atualizar Nome\n'                   +
          '4. Atualizar Telefone\n'               +
          '5. Atualizar Endereço\n'               +
          '6. Atualizar Data de Nascimento\n'     +
          '7. Excluir\n'                          +
          '0. Sair\n')
    this.opcao = int(input('Escolhe uma opção: '))

def operacoes():
    while(this.opcao != 0):
        menu()
        if this.opcao == 0:
            print('Obrigado!')
        elif this.opcao == 1:
            print('Informe seu CPF: ')
            cpf = input()
            print('Informe seu nome:')
            nome = input()
            print('Informe seu telefone: ')
            telefone = input()
            print ('Informe seu endereço: ')
            endereco = input()
            print ('Informe sua data de nascimento: ')
            dataDeNascimento = input()
            #Chamar o metodo inserir
            operacao.inserir(cpf, nome, telefone, endereco, dataDeNascimento)

        elif this.opcao == 2:
            #Chamar o metodo consultar
            operacao.consultar()

        elif this.opcao == 3:
            print("Informe o CPF da pessoa que deseja atualizar")
            this.cpf=int(input())
            print("informe o novo nome: ")
            this.campo = input()
            operacao.atualizar(this.cpf, 'nome', this.campo)

        elif this.opcao == 4:
            print("Informe o CPF da pessoa que deseja atualizar")
            this.cpf = int(input())
            print("Informe o novo telefone: ")
            this.campo = input()
            operacao.atualizar(this.cpf, 'telefone', this.campo)

        elif this.opcao == 5:
            print("Informe o CPF da pessoa que deseja atualizar")
            this.cpf = int(input())
            print("Informe o novo endereço: ")
            this.campo = input()
            operacao.atualizar(this.cpf, 'endereco', this.campo)

        elif this.opcao == 6:
            print("Informe o CPF da pessoa que deseja atualizar")
            this.cpf = int(input())
            print("Informe a nova Data de Nascimento: ")
            this.campo = input()
            operacao.atualizar(this.cpf, 'dataDeNascimento', this.campo)

        elif this.opcao == 7:
            print("Informe o CPF da pessoa que deseja excluir: ")
            this.cpf = int(input())
            operacao.excluir(this.cpf)

        else:
            print('Opção escolhida não é valido, tente novamente FDP por gentileza !')


