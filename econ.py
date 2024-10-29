#DESAFIO 1: Crie um sistema de e-commerce, onde o usuário possa: cadastrar-se, comprar um produto, descobrir o valor total, pagar.

print("Log in")
login = "Guilherme"
senha = 123
dado1 = str(input('Digite o seu log in: '))
dado2 = int(input("Agora digite a sua senha: "))
if dado1 == login and dado2 == senha:
     print("Seja bem-vindo")
     print(f'''
         Selecione o item que deseja comprar:
    
     1 - Tênis azul 
     2 - Tênis vermelho 
     3 - Tênis preto
               
     ''')
     selecao = int(input("número do item que deseja comprar"))
     if selecao == 1:
         print("R$ 100.00")
         print("Satisfeito com a sua escolha? por favor, digite SIM se deseja continuar, ou NÃO, se deseja reiniciar a operação")
         answer = (input(">"))
         if answer == "SIM":
                 print("Infome os Seguintes dados para prosseguir com o pagamento") 
                 name = str(input("Nome como aparece no seu cartão de crédito"))
                 cc_number = int(input('Por favor, informe o número do cartão de crédito'))
                 security_code = int(input('Código de segurança do cartão de crédito'))
                 print("Parabéns pela compra, nossa loja agradece")
         else:
                print(f'''É uma pena que você não deseja prosseguir com a compra. 
                      Mesmo assim, a nossa equipe agradece pelo seu interesse de chegar até aqui.''')

     elif selecao == 2:
         print("R$ 150.00")
         print("Satisfeito com a sua escolha? por favor, digite SIM se deseja continuar, ou NÃO, se deseja reiniciar a operação")
         answer = (input(">"))
         if answer == "SIM":
                 print("Infome os Seguintes dados para prosseguir com o pagamento") 
                 name = str(input("Nome como aparece no seu cartão de crédito"))
                 cc_number = int(input('Por favor, informe o número do cartão de crédito'))
                 security_code = int(input('Código de segurança do cartão de crédito'))
                 print("Parabéns pela compra, nossa loja agradece")
         else:
                 print(f'''É uma pena que você não deseja prosseguir com a compra. 
                      Mesmo assim, a nossa equipe agradece pelo seu interesse de chegar até aqui.''')

     else: 
         print("R$ 200.00")
         print("Satisfeito com a sua escolha? por favor, digite SIM se deseja continuar, ou NÃO, se deseja reiniciar a operação")
         answer = (input(">"))
         if answer == "SIM":
                 print("Infome os Seguintes dados para prosseguir com o pagamento") 
                 name = str(input("Nome como aparece no seu cartão de crédito"))
                 cc_number = int(input('Por favor, informe o número do cartão de crédito'))
                 security_code = int(input('Código de segurança do cartão de crédito'))
                 print("Parabéns pela compra, nossa loja agradece")
         else:
                 print(f'''É uma pena que você não deseja prosseguir com a compra. 
                      Mesmo assim, a nossa equipe agradece pelo seu interesse de chegar até aqui.''')
else:
    print(f'''
     Algo não está correto. Por favor,
     verifique novamente seu login 
     ou senha
    ''')