var1 = int(input("Digite o primeiro numero: "))
var2 = int(input("Digite o segundo numero: "))
oper = input("Digite a operação + - / *:")

match oper:
    case '+':
        print("Soma: ", var1+var2)
    case '-':
        print("Subtração: ", var1-var2)
    case '/':
        print("Divisão: ", var1/var2)
    case '*':
        print("Multiplicação: ", var1*var2)