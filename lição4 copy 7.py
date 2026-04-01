def obter_inteiro(mensagem: str) -> int:
    """Pede um número inteiro ao usuário de forma segura"""
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Erro: informe um número inteiro válido.")


def main() -> None:
    print("=== Encontrar Maior e Menor Valor ===\n")

    # Ler o primeiro valor para inicializar maior e menor
    a = obter_inteiro("Digite o valor de A: ")
    maior = a
    menor = a

    print(f"Primeiro valor: A = {a}")

    # Ler os outros quatro valores e comparar
    b = obter_inteiro("Digite o valor de B: ")
    if b > maior:
        maior = b
    if b < menor:
        menor = b

    c = obter_inteiro("Digite o valor de C: ")
    if c > maior:
        maior = c
    if c < menor:
        menor = c

    d = obter_inteiro("Digite o valor de D: ")
    if d > maior:
        maior = d
    if d < menor:
        menor = d

    e = obter_inteiro("Digite o valor de E: ")
    if e > maior:
        maior = e
    if e < menor:
        menor = e

    # Mostrar todos os valores lidos
    print(f"\nValores lidos: A={a}, B={b}, C={c}, D={d}, E={e}")

    # Apresentar resultado
    print("\n" + "=" * 40)
    print("RESULTADO:")
    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")
    print("=" * 40)


if __name__ == "__main__":
    main()
