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
        break
    
    
    else:
        print("Tente novamente, algum dado está equivocado")

#n = input('Clique enter para sair') - Esssencial para torna o código executável


#interface gráfica: permite a interação do usuário com a linguagem.
#tornamos o código em executável (.EXE), clicamos duas vezes e ele funciona. O passo a passo está no notion.

#----------------------------------------------- WHILE ---------------------------------------------------------------#

contador = 3
while contador > 0:
    print(contador)
    contador = contador - 1

cont = 0
while cont <= 10:
    print(cont)
    cont = cont + 1

contador = 0
n = int(input('Digite um némero:  '))
while contador <= 10:
        calculo = n * contador
        print(f'{n} "X" {contador} "=" {calculo}')
        contador = contador + 1

#----------------------------------------------- ATIVIDADE 2 | CRIE UM MERCADO ---------------------------------------------------------------#
d = {

"Tomate" : "RS 6,00/kilo",
"Cerveja" : "RS 4,00/unidade",
"Chocolate" : "RS 10,00/unidade"
}


lista1_keys = []
lista2_values = []
for n,x in d.items():
    lista1_keys.append(n)
    lista2_values.append(x)
    print(lista1_keys,lista2_values)

carrinho = []
meus_valores = []
for n in range(0):
    escolha = int(input("Escolha"))
    if escolha in lista1_keys:
        carrinho.append(lista1_keys[escolha])
        print(carrinho)
        pergunta = input("Deseja adicionar mais coisas? s/n?")
    else:
        print("Obrigado, volte sempre")








