# #INDENTAÇÃO: ESPAÇAMENTOS UTILIZADOS ENQUANTO PROGRAMAMOS. ESTÁ RELACIONADO COM A ORGANIZAÇÃODO CÓDIGO. POR EXEMPLO, TUDO QUE FOR PERTENCENTE A FUNÇÃO "IF", DEVE ESTAR COM UM ESPAÇAMENTO PRÉ-DEFINIDO. ESTÁ RELACIONBADO COM A ORGANIZAÇÃO DO CÓDIGO, OS BLOCOS DE CÓDIGO. É SOBRE ENCAPSULAR CORRETAMENTE.

# if 10 > 2:
#     print("olá mundo")

# #O que já vimos: variáveis, comentários, tipos primitivos, sinais comparação lógicos, sinais aritméticos, i/o

# #CONCATENAR: JUNTAR DADOS. 5 FORMAS: %, f',",", .FORMAT
# nome = "Carlos"
# print('Olá %s' %(nome))

# nome = 'José'
# print(f'Olá {nome}{2}')

# nome =  "Paula"
# print("Olá {}" .format(nome))

# nome = "Julia"
# print('Olá','nome')

# nome = 'Pedro'
# print('Olá', ' ' + 'nome')

# #PULAR LINHA
# print('Olá \n mundo')

# print('''
# Olá, meu nome é Guilherme.
# Acabei de pular a linha,
# olha só que legal :)
# ''')

# #REFATORAÇÃO
# #bug: impede de funcionar como planejado
# #erro: sistema não funciona.

# #Comentar várias linhas ao mesmo tempo no Visual Studio Code, Ctrl + :

# # lista é identificada através do []

#---------------------------------------------------------------------------------------------------------------------------------------------------------#
#AULA 8

lista = [1,2,3,4,5,6]
print(lista)

n1 = lista[0]
n2 = lista[1]
soma = n1 + n2
print(soma)

lista[0] = 25
lista[1] = 12
print(lista)

lista.append(10)
lista.append('Teste')
lista += (910, 2030, 50 , 'TEST')
lista.extend([1,'teste',n2])
lista.insert(0,100) #no indice 0, atribuir o valor 100
print(lista)

#Três formas de dletar dados

del lista[3] #deleta o indice número 3 da lista, no caso o valor 4.
lista.remove(5) #deleta o número 5 da lista.
lista.pop() #remove o último dado
print(lista)


# inicio | fim | step by step
x = list(range(0,21,2))
print(x)

y = list(range(5,51,5))
print(y)

carros = ["uno",'ferrari','corvette',"lamborghini"]
print(carros + lista)

print('Marcado')

produtos = ['ARROZ', 'FEIJÃO', 'MACARRÃO', 'MOLHO']
valores = [10.0,15.0,8.00,3.50]
carrinho = [ ]
meus_valores = []

produto1 = int(input('''
                 0 - ARROZ
                 1 - FEIJÃO
                 2 - MACARRÃO
                 3 - MOLHO
                 >> '''))

produto2 = int(input('''
                 0 - ARROZ
                 1 - FEIJÃO
                 2 - MACARRÃO
                 3 - MOLHO
                 >> '''))


carrinho = [produtos[produto1], produtos[produto2]]
meus_valores = [valores[produto1],valores[produto2]]
SOMA = sum(meus_valores)

print(f'''
..................................
      CUPOM
      
    
1 - {produtos[produto1]} R$ {valores[produto1]}
2 - {produtos[produto2]} R$ {valores[produto2]}




''')

#DICIONÁRIO

dicionario = {
"nome" : "Paulo",
'idade' : 25,
'endereco' : 'Rua Palestra',
'email' : 'paulo@gmail.com',
'curso' : 'Python 60'

}

dicionario['idade'] = 30
dicionario['novo'] = 25
dicionario['cpf'] = 163789098-00


#CONDICIONAIS: SÃO BLOCOD DE CÓDIGO PARA QUE O COMPUTADOR PARA FAZER ESCOLHAS

if 35 >= 45:
    print('É maior')

elif 35 == numero:
    print('É igual')
else:
    print('É menor')



