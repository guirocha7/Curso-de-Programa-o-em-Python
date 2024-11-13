from funcoes import * # o * chama todas as funções do módulo. Posso usar a "," e chamar uma por uma também.

def calculadora():
    operacao = input("Qual é a sua operação? (+ / - / * / %) >>>")
    if operacao == "+":
        soma()
    elif operacao == "-":
        sub()
    elif operacao == "*":
        multi()
    elif operacao == "%":
        div()


while True:
    calculadora()

