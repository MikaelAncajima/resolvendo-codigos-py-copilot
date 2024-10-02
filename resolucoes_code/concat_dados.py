# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!
def obter_informacao(mensagem):
    """
    Solicita uma informação do usuário com base na mensagem fornecida.

    Args:
        mensagem (str): A mensagem a ser exibida ao solicitar a informação.

    Returns:
        str: A informação fornecida pelo usuário.
    """
    return input(mensagem)

def concatenar_informacoes(info1, info2):
    """
    Concatena duas informações fornecidas.

    Args:
        info1 (str): A primeira informação.
        info2 (str): A segunda informação.

    Returns:
        str: As informações concatenadas.
    """
    return info1 + info2

def main():
    """
    Função principal que coordena a obtenção e concatenação das informações.
    """
    info1 = obter_informacao("Digite a primeira informação: ")
    info2 = obter_informacao("Digite a segunda informação: ")
    info_concatenada = concatenar_informacoes(info1, info2)
    print("As informações concatenadas são: ", info_concatenada)

if __name__ == "__main__":
    main()
