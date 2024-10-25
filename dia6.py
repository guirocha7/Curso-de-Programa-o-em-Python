# #DESAFIO 1: Crie um sistema de e-commerce, onde o usuário possa: cadastrar-se, comprar um produto, descobrir o valor total, pagar.

# print("Log in")
# login = "Guilherme"
# senha = 123456
# dado1 = str(input('Digite o seu log in '))
# dado2 = int(input("Agora digite a sua senha "))
# if dado1 == login and dado2 == senha:
#     print("Seja bem-vindo")
#     print(f'''
    
#     Selecione o item que deseja comprar:
    
#     1 - Tênis azul 
#     2 - Tênis vermelho 
#     3 - Tênis preto

    
#     ''')
#     selecao = int(input("número do item que deseja comprar"))
#     if selecao == 1:
#         print("R$ 100.00")
#         print("Satisfeito com a sua escolha? por favor, digite SIM se deseja continuar, ou NÃO, se deseja reiniciar a operação")
#         answer = (input(">"))
#         if answer == "SIM":
#                 print("Infome os Seguintes dados para prosseguir com o pagamento") 
#                 name = str(input("Nome como aparece no seu cartão de crédito"))
#                 cc_number = int(input('-'))
#                 security_code = int(input('-'))
#                 print("Parabéns pela compra, nossa loja agradece")

#     elif selecao == 2:
#         print("R$ 150.00")
#         print("Satisfeito com a sua escolha? por favor, digite SIM se deseja continuar, ou NÃO, se deseja reiniciar a operação")
#         answer = (input(">"))
#         if answer == "SIM":
#                 print("Infome os Seguintes dados para prosseguir com o pagamento") 
#                 name = str(input("Nome como aparece no seu cartão de crédito"))
#                 cc_number = int(input('-'))
#                 security_code = int(input('-'))
#                 print("Parabéns pela compra, nossa loja agradece")

#     else: 
#         print("R$ 200.00")
#         print("Satisfeito com a sua escolha? por favor, digite SIM se deseja continuar, ou NÃO, se deseja reiniciar a operação")
#         answer = (input(">"))
#         if answer == "SIM":
#                 print("Infome os Seguintes dados para prosseguir com o pagamento") 
#                 name = str(input("Nome como aparece no seu cartão de crédito"))
#                 cc_number = int(input('-'))
#                 security_code = int(input('-'))
#                 print("Parabéns pela compra, nossa loja agradece")


# else:
#     print(f'''
#     "Seu login não está correto, 
#     verifique novamente seu login 
#     ou senha''')




#DESAFIO 2: 

print(f'''
Bem-Vindo ao Hotel México

Por favor, informe a quantidade de diárias que o sr(a) ficará hospedado.
''')
day = str(input("Número de Diárias: "))
print(f'''
Na sequência, informe os dados das pessoas que ficarão hospedas no quarto.
!LEMBRANDO QUE SÓ SÃO PERMITIDAS NO MÁXIMO 3 PESSOAS POR ACOMODAÇÃO!
''')
number = int(input("Qual é o número de ocupantes da sua acomodação: "))
if number == 1:
    name1 = str(input("Nome: "))
    age1 = int(input("Idade: "))
    print(f'''
    Escolha a sua suíte:
    1 - Simples R$ 100.00
    2 - Dupla   R$ 150.00
    3 - Luxo    R$ 250.00
    ''')
    accomodation = int(input("Qual será a sua acomodação? Digite o número referente a ela a seguir: "))
    if accomodation == 1:
        price1 = 100 * day
        print(name1, "sua experiência no Hotel México ficará em um total de", price1)
    elif accomodation == 2:
        price2 = 150 * day
        print(name1, "sua experiência no Hotel México ficará em um total de", price2)
    else:
        price3 = 200 * day
        print(name1, "sua experiência no Hotel México ficará em um total de", price3)


elif number == 2:
    name2 = str(input("Nome: "))
    age2 = int(input("Idade: "))
    print(f'''
    Escolha a sua suíte:
    1 - Simples R$ 100.00
    2 - Dupla   R$ 150.00
    3 - Luxo    R$ 250.00
    ''')
    accomodation = int(input("Qual será a sua acomodação? Digite o número referente a ela a seguir: "))
    if accomodation == 1:
        price1 = 100*day
        print(name1, "sua experiência no Hotel México ficará em um total de", price1)
    elif accomodation == 2:
        price2 = 150*day
        print(name1, "sua experiência no Hotel México ficará em um total de", price2)
    else:
        price3 = 200*day
        print(name1, "sua experiência no Hotel México ficará em um total de", price3)
elif number == 3:
    name3 = str(input("Nome: "))
    age3 = int(input("Idade: "))
    print(f'''
    Escolha a sua suíte:
    1 - Simples R$ 100.00
    2 - Dupla   R$ 150.00
    3 - Luxo    R$ 250.00
    ''')
accomodation = int(input("Qual será a sua acomodação? Digite o número referente a ela a seguir: "))
    if accomodation == 1:
        price1 = 100*day
        print(name1, "sua experiência no Hotel México ficará em um total de", price1)
    elif accomodation == 2:
        price2 = 150*day
        print(name1, "sua experiência no Hotel México ficará em um total de", price2)
    else:
        price3 = 200*day
        print(name1, "sua experiência no Hotel México ficará em um total de", price3)
else:
    print(f'''
    Essa quantidade de ocupantes excede o número máximo de ocupantes por acomodação,
    portanto não será possível seguir com o cadastro.
    
    Inicie o processo novamente revisando o número de ocupante, 
    ou contate o nosso suporte via chat ou telefone (11) 99999-9999''')






























