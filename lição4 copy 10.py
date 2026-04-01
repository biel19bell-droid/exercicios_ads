def obter_inteiro(mensagem: str) -> int:
    """Pede um número inteiro ao usuário de forma segura"""
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Erro: informe um número inteiro válido.")


def main() -> None:
    print("=== Apresentar Valor se Não For Maior que 3 ===\n")

    # Ler o valor numérico inteiro
    numero = obter_inteiro("Digite um número inteiro: ")

    print(f"\nNúmero informado: {numero}")

    # Usar apenas o operador lógico de negação
    # A condição é: apresentar se NÃO for maior que 3
    if not (numero > 3):
        print(f"✅ O valor {numero} não é maior que 3, então é apresentado.")
    else:
        print(f"❌ O valor {numero} é maior que 3, então não é apresentado.")

    print("\n" + "=" * 40)


if __name__ == "__main__":
    main()
