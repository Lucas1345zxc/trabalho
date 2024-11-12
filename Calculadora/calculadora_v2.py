# Inicializa a variável saida
saida = ''

def adicao(a, b):
    return a + b

def subracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b

def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao.lower() == 'adição':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subtração':
        resultado = subracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicação':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisão':
        resultado = divisao(num1, num2)
    else:
        return "Operação inválida"
    
    return resultado

while saida.lower() != 'n':
    # Solicita ao usuário os valores e a operação
    primeiro_numero = float(input("Digite o primeiro número: "))
    segundo_numero = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, / ou o nome da operação): ")

    # Chama a função calculadora
    resultado = calculadora(primeiro_numero, segundo_numero, operacao)

    # Exibe o resultado
    print(f'Resultado da operação: {resultado}')

    # Pergunta se o usuário deseja continuar
    saida = input("Deseja continuar? (S/N): ")

# Fim do programa
print("Programa encerrado.")
