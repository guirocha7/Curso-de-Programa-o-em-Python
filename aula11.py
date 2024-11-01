# def soma():
#     n1 = int(input("Digite um número")) #Variáveis locais: dentro da função | variáveis globais são referentes ao código por inteiro.
#     n2 = int(input("Digite um número"))
#     multi = n1 + n2
#     print(soma)
# def subtracao():
#     n1 = int(input("Digite um número"))
#     n2 = int(input("Digite um número"))
#     multi = n1 - n2
#     print(sub)
# def multiplicacao():
#     n1 = int(input("Digite um número"))
#     n2 = int(input("Digite um número"))
#     multi = n1 * n2
#     print(multi)
# def divisao():
#     n1 = int(input("Digite um número"))
#     n2 = int(input("Digite um número"))
#     div = n1 / n2
#     print(div)
# def calculadora():
#     operação = input('+ - * /"')
#     if operação == "+":
#         soma()
#     elif operação == "-":
#         subtracao()
#     elif operação == "*":
#         multiplicacao()
#     elif operacao == "/":
#         divisao()
#     else:
#         print("Digitação não existe")
# while True:
#     calculadora()




def extrato():




def banco():
    print("Seu saldo é de R$ 100.000.000,00")

def deposito():

        







    conta = 1
    senha = 1
    print(f'''
    Bem-Vindo ao Banco GRS

    por favor, faça o login para prosseguir com os próximos passos.
    ''')
saldo = 1000
    for n in range(1,4):
        dado = int(input("Número da sua conta bancária:  "))
        dado1 = int(input("Digite a senha: "))
        if conta == dado and senha == dado1:
            print(f'''
            Seja Bem-Vindo

            Suas opções são:
            1 - Verificar Extrato
            2 - Fazer um Depósito
            3 - Saque
            4 - Sair
            ''')
            print("Qual função deseja utilizar? Digite o número relativo a seguir.")
            opcao = input("Digite o número")
            if opcao == 1:
                print("Seu saldo é de R$", saldo)
            elif opcao == 2:
                print("insira a quantia em dinheiro na máquina")
                depositoo = 
            elif opcao == 3:
                saque = input("Quanto deseja sacar?")
                if saque > 100000000:
                    print("Não é possível realizar a operação")
                else: 
                    resultado = 1000000000 - saque
                    print("Seu novo saque é de RS ",saque)
            else:
                print("Deseja mesmo sair? s/n")
                resposta = input("......")
                if resposta == s:
                    print("até logo, tchau.")
                    break
                else:
                    print("Fim da linha")       
        else:
            print("Tente novamente, algum dado está equivocado")


banco()