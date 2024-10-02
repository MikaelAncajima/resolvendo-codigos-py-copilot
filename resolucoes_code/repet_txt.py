# Vamos solicitar como entrada um número e uma string.

'''
Este módulo contém funções para solicitar entrada do usuário e repetir uma string um número específico de vezes.

Funções:
    solicitar_entrada(): Solicita ao usuário um número inteiro e uma string, retornando-os como uma tupla.
    repetir_texto(numero, texto): Repete a string fornecida pelo número de vezes especificado, com um espaço entre cada repetição.
    main(): Função principal que coordena a solicitação de entrada e a repetição da string.
'''

def solicitar_entrada():
    """
    Solicita ao usuário um número inteiro e uma string.

    Retorna:
        tuple: Contém o número inteiro e a string fornecidos pelo usuário.
    """
    numero = int(input("Digite um número: "))
    texto = input("Digite uma string: ")
    return numero, texto

def repetir_texto(numero, texto):
    """
    Repete a string fornecida pelo número de vezes especificado.

    Args:
        numero (int): Número de vezes que a string será repetida.
        texto (str): A string que será repetida.

    Retorna:
        str: A string repetida o número de vezes especificado, com um espaço entre cada repetição.
    """
    return (texto + ' ') * numero

def main():
    numero, texto = solicitar_entrada()
    resultado = repetir_texto(numero, texto)
    print(resultado)

if __name__ == "__main__":
    main()
