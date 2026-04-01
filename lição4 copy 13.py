def obter_inteiro(mensagem: str) -> int:
    """Pede um número inteiro ao usuário de forma segura"""
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Erro: informe um número inteiro válido.")


def main() -> None:
    print("=== Soma de Três Valores (Apenas se >= 100) ===\n")

    # Ler os três valores inteiros
    a = obter_inteiro("Digite o valor de A: ")
    b = obter_inteiro("Digite o valor de B: ")
    c = obter_inteiro("Digite o valor de C: ")

    # Calcular a soma
    soma = a + b + c

    print(f"\nValores: A={a}, B={b}, C={c}")
    print(f"Soma: {a} + {b} + {c} = {soma}")

    # Apresentar resultado somente se for maior ou igual a 100
    if soma >= 100:
        print(f"\n✅ A soma ({soma}) é maior ou igual a 100.")
        print(f"Resultado da soma: {soma}")
    else:
        print(f"\n❌ A soma ({soma}) é menor que 100.")
        print("Portanto, o resultado não será apresentado.")

    print("\n" + "=" * 40)


if __name__ == "__main__":
    main()
