# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def solicitar_numeros():
    """Solicita dois números do usuário e os retorna como floats."""
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1, num2

def solicitar_operacao():
    """Solicita a operação desejada pelo usuário e a retorna como string."""
    return input("Digite a operação (+, -, *, /): ")

def realizar_operacao(num1, num2, operacao):
    """Realiza a operação matemática entre dois números e retorna o resultado."""
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return abs(num1 - num2)
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operação inválida"

def main():
    """Função principal que coordena a solicitação de dados e a realização da operação."""
    num1, num2 = solicitar_numeros()
    operacao = solicitar_operacao()
    resultado = realizar_operacao(num1, num2, operacao)
    print(f"O resultado da operação é: {resultado}")

if __name__ == "__main__":
    main()
