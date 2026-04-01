def obter_inteiro(mensagem: str) -> int:
    """Pede um número inteiro ao usuário de forma segura"""
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Erro: informe um número inteiro válido.")


def main() -> None:
    print("=== Verificar Faixa de Valores (1 a 9) ===\n")

    # Ler o valor numérico inteiro
    numero = obter_inteiro("Digite um número inteiro: ")

    print(f"\nNúmero informado: {numero}")

    # Verificar se está na faixa de 1 a 9
    if 1 <= numero <= 9:
        print("✅ O valor está na faixa permitida (1 a 9).")
    else:
        print("❌ O valor está fora da faixa permitida (1 a 9).")

    print("\n" + "=" * 40)


if __name__ == "__main__":
    main()
