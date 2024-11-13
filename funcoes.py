# def soma():
#     n1 = float(input("...."))
#     n2 = float(input("...."))
#     sm = n1 + n2
#     print(sm)

# def sub():
#     n1 = float(input("...."))
#     n2 = float(input("...."))
#     s = n1 - n2
#     print(s)

# def multi():
#     n1 = float(input("...."))
#     n2 = float(input("...."))
#     m = n1*n2
#     print(m)

# def div():
#     n1 = float(input("...."))
#     n2 = float(input("...."))
#     d = n1*n2
#     print(d)

produtos = (bolacha, abacaxi, pimenta)
precos = (10, 7, 3)
def itens():
    print(f'1 - {produtos[0]} {precos[0]}')
    print(f'2 - {produtos[1]} {precos[1]}')
    print(f'3 - {produtos[2]} {precos[2]}')

def finalizar():
    print = ('Selecione os produtos que deseja adquirir' )
    x = imput("Digite o número do item o qual deseja adquirir:  ")
    if x == 1:
        print(f'R$ {precos[0]},00')
    elif x == 2:
        print(f'R$ {precos[1]},00')
    else:
        print(f'R$ {precos[2]},00')


def pagamento():
    print(f'''
    Qual é a forma de pagamento?
    1 - Cartão de Crédito
    2 -  Cartão de Débito
    3 - Pix
    ''')
    y = input("Digite o número refernte a opoção: ")
    if y == 1 or y == 2:
        nome = input("Digite o seu nome conforme aparece no cartão:  ")
        cc = input("Digite o número do cartão de crédito:  ")
        codigo = input("Agora é a vez do código de segurança:  ")
        print("Aguarde um instante..........")
        print("Transação aprovada, volte sempre!")
    else:
        print("O nosso pix é: 126.5545.00001/05")
        z = imput("Realizou a transferência? S/N")
        print("Aguarde um instante..........")
        print("Transação aprovada, volte sempre!")




