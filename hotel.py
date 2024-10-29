#DESAFIO 2: Você foi contratado para desenvolver uma parte do sistema de um hotel. O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias.

print(f'''
Bem-Vindo ao Hotel México

Por favor, informe a quantidade de diárias que o sr(a) ficará hospedado.
      
Lembrando que a diária começa contar a partir das 12:00 do dia anterior e 
se encerra às 10:00 do dia seguinte. Portanto, cada diária equivale a grosso
modo, o número de noites dormidas.
''')
day = float(input("Número de Diárias: "))
print(f'''
Na sequência, informe os dados das pessoas que ficarão hospedas no quarto.
!LEMBRANDO QUE SÓ SÃO PERMITIDAS NO MÁXIMO 3 PESSOAS POR ACOMODAÇÃO!
''')
number = int(input("Qual é o número de ocupantes da sua acomodação: "))
if number == 1:
    name1 = str(input("Nome do Primeiro Ocupante: "))
    age1 = int(input("Idade: "))
    print(f'''
    Escolha a sua suíte:
    1 - Simples R$ 100.00
    2 - Dupla   R$ 150.00
    3 - Luxo    R$ 250.00
    ''')
    accomodation = int(input("Qual será a sua acomodação? Digite o número referente a ela a seguir: "))
    if accomodation == 1:
        price1 = float(100 * day)
        print(name1, "sua experiência no Hotel México ficará em um total de R$", price1)
    elif accomodation == 2:
        price2 = float(150 * day)
        print(name1, "sua experiência no Hotel México ficará em um total de R$", price2)
    else:
        price3 = float(250 * day)
        print(name1, "sua experiência no Hotel México ficará em um total de R$", price3)
elif number == 2:
    name1 = str(input("Nome do Primeiro Ocupante: "))
    age1 = int(input("Idade: "))
    name2 = str(input("Nome do Segundo Ocupante: "))
    age2 = int(input("Idade: "))
    print(f'''
    Escolha a sua suíte:
    1 - Simples R$ 100.00
    2 - Dupla   R$ 150.00
    3 - Luxo    R$ 250.00
    ''')
    accomodation = int(input("Qual será a sua acomodação? Digite o número referente a ela a seguir: "))
    if accomodation == 1:
        price1 = float(100 * day)
        print(name1, "sua experiência no Hotel México ficará em um total de R$", price1)
    elif accomodation == 2:
        price2 = float(150 * day)
        print(name1, "sua experiência no Hotel México ficará em um total de R$", price2)
    else:
        price3 = float(250 * day)
        print(name1, "sua experiência no Hotel México ficará em um total de R$", price3)
elif number == 3:
    name1 = str(input("Nome do Primeiro Ocupante: "))
    age1 = int(input("Idade: "))
    name2 = str(input("Nome do Segundo Ocupante: "))
    age2 = int(input("Idade: "))
    name3 = str(input("Nome do Terceiro Ocupante: "))
    age3 = int(input("Idade: "))
    print(f'''
    Escolha a sua suíte:
    1 - Simples R$ 100.00
    2 - Dupla   R$ 150.00
    3 - Luxo    R$ 250.00
    ''')
    accomodation = int(input("Qual será a sua acomodação? Digite o número referente a ela a seguir: "))
    if accomodation == 1:
        price1 = float(100 * day)
        print(name1, "sua experiência no Hotel México ficará em um total de R$", price1)
    elif accomodation == 2:
        price2 = float(150 * day)
        print(name1, "sua experiência no Hotel México ficará em um total de R$", price2)
    else:
        price3 = float(250 * day)
        print(name1, "sua experiência no Hotel México ficará em um total de R$", price3)
else:
    print(f'''
    Essa quantidade de ocupantes excede o número máximo de ocupantes por acomodação,
    portanto não será possível seguir com o reserva.
    
    Inicie o processo novamente, revisando o número de ocupantes, 
    ou contate o nosso suporte via chat ou telefone (11) 99999-9999.''')