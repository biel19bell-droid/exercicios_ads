def obter_inteiro(mensagem: str) -> int:
    """Pede um número inteiro ao usuário de forma segura"""
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Erro: informe um número inteiro válido.")


def main() -> None:
    print("=== Verificar se o Número é Par ou Ímpar ===\n")

    # Ler o valor numérico inteiro
    numero = obter_inteiro("Digite um número inteiro: ")

    print(f"\nNúmero informado: {numero}")

    # Verificar se é par ou ímpar
    if numero % 2 == 0:
        print("✅ Este número é PAR.")
    else:
        print("✅ Este número é ÍMPAR.")

    print("\n" + "=" * 40)


if __name__ == "__main__":
    main()
