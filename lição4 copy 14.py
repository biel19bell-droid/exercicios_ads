def obter_inteiro(mensagem: str) -> int:
    """Pede um número inteiro ao usuário de forma segura"""
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Erro: informe um número inteiro válido.")


def main() -> None:
    print("=== Multiplicar por 2 (Apenas se Resultado > 30) ===\n")

    # Ler o número inteiro
    numero = obter_inteiro("Digite um número inteiro: ")

    # Multiplicar por dois
    resultado = numero * 2

    print(f"\nNúmero informado: {numero}")
    print(f"Multiplicação: {numero} × 2 = {resultado}")

    # Apresentar resultado somente se for maior que 30
    if resultado > 30:
        print(f"\n✅ O resultado ({resultado}) é maior que 30.")
        print(f"Resultado da multiplicação: {resultado}")
    else:
        print(f"\n❌ O resultado ({resultado}) não é maior que 30.")
        print("Portanto, o resultado não será apresentado.")

    print("\n" + "=" * 40)


if __name__ == "__main__":
    main()
