# # for
# for n in range(10):
#     print(n)

# for variavel in range (1,11,2):
#     print(variavel)

# print("-----------------------------------------------------------------------------------")

# lista = [1,2,3]
# for c in lista:
#     print(c)

# texto = "fhshfjskfhskjfhskjfhskj"
# for x in texto:
#     print(x)
    
# print("-----------------------------------------------------------------------------------")

# for d in lsit(range(1,16)):
#     print(d)

# for n in range(1,4):
#     print("Cadastre-se")
#     nome = input("Digite o seu noem: ")
#     idade = input("Digite a sua idade: ")
#     email = input("Digite o seu email: ")
#     print("Obrigado, próximo cliente")  #repete todas as ionserçôes até a última


# lista = []
# for n in eange(1,4):
#     print("Cadastre-se")
#     nome = input("Digite o seu noem: ")
#     idade = input("Digite a sua idade: ")
#     email = input("Digite o seu email: ")
#     print("Obrigado, próximo cliente")
#     lista += (nome, idade, email) #adiciona na lista
# print(lista) #print fora do for o resulta já sai com todos os dados

# n = [1,2,3,4]
# x = 2

# print(f'''
# {n[0] x {x} = {n[0]*x}}
# {n[1] x {x} = {n[1]*x}}
# {n[2] x {x} = {n[2]*x}}
# {n[3] x {x} = {n[3]*x}}
# ''')


# lista = []

# numero = int(input())
# for n in range(0,11):
#     result = n*numero
#     print(f'{n} X {numero} = {result}')




# chances = range(1,4)
# for n in chances:
#     chute = int(input("Digite um número: "))
#     aleatorio = randon.randint(1,6)
#     if chute == aleatorio
#         print('Vc acertou em cheio, o número é {chute}')
#         break
#     else: 
#         print('Vc tem apenas', chances, 'chances, o número é', aleatorio)
#         chances.pop() #poderia ser del chances e remover o primeiro valor del chances[0]

# d = {
# 'a': 1,
# 'b': 2,
# 'c': 3,
# }

# lista = []
# for n, x in d.items(): #item são as variaveis, keys são ois valores entre chaves
#     print(x, n)



# SISTEMA DE BANCO
conta = 1
senha = 1
print(f'''
Bem-Vindo ao Banco GRS

por favor, faça o login para prosseguir com os próximos passos.
''')
dado = input("Número da sua conta bancária:  ")
dado1 = input("Digite a senha: ")
for n in range(1,4):
    if conta == dado and senha == dado1:
        break
        print(f'''
        Seja Bem-Vindo

        Suas opções são:
        1 - Verificar Extrato
        2 - Fazer um Depósito
        3 - Saque
        4 - Sair
        ''')
    
    
    else:
        print("Tente novamente, algum dado está equivocado")
        dado = input("Número da sua conta bancária:  ")
        dado1 = input("Digite a senha: ")
            # if conta == dado and senha == dado1:
            # break
            # print(f'''
            # Seja Bem-Vindo

            # Suas opções são:
            # 1 - Verificar Extrato
            # 2 - Fazer um Depósito
            # 3 - Saque
            # 4 - Sair
            # ''')

    





