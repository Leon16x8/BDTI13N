import operacao
import this
this.opcao = -1

def menu():
    print('\nEscolha uma das opções abaixo: \n\n' +
          '1. Cadastrar\n' +
          '2. Consultar\n' +
          '0. Sair\n')
    this.opcao = int(input())

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
        else:
            print('Opção escolhida não é valido, tente novamente FDP por gentileza !')
