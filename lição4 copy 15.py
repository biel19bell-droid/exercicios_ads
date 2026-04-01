def obter_inteiro(mensagem: str) -> int:
    """Pede um número inteiro ao usuário de forma segura"""
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Erro: informe um número inteiro válido.")


def main() -> None:
    print("=== Verificação de Divisibilidade por 2 e 3 ===\n")

    # Ler quatro valores inteiros
    a = obter_inteiro("Digite o valor de A: ")
    b = obter_inteiro("Digite o valor de B: ")
    c = obter_inteiro("Digite o valor de C: ")
    d = obter_inteiro("Digite o valor de D: ")

    print(f"\nValores lidos: A={a}, B={b}, C={c}, D={d}")

    # Lista para armazenar os valores divisíveis por 2 e 3
    divisiveis = []

    # Verificar cada valor
    print("\nVerificando divisibilidade por 2 e 3 (ou seja, por 6):")

    # Verificar A
    if a % 2 == 0 and a % 3 == 0:
        divisiveis.append(("A", a))
        print(f"✓ A = {a} é divisível por 2 e por 3")
    else:
        print(f"✗ A = {a} não é divisível por 2 e por 3")

    # Verificar B
    if b % 2 == 0 and b % 3 == 0:
        divisiveis.append(("B", b))
        print(f"✓ B = {b} é divisível por 2 e por 3")
    else:
        print(f"✗ B = {b} não é divisível por 2 e por 3")

    # Verificar C
    if c % 2 == 0 and c % 3 == 0:
        divisiveis.append(("C", c))
        print(f"✓ C = {c} é divisível por 2 e por 3")
    else:
        print(f"✗ C = {c} não é divisível por 2 e por 3")

    # Verificar D
    if d % 2 == 0 and d % 3 == 0:
        divisiveis.append(("D", d))
        print(f"✓ D = {d} é divisível por 2 e por 3")
    else:
        print(f"✗ D = {d} não é divisível por 2 e por 3")

    # Apresentar resultado final
    print("\n" + "=" * 50)
    if divisiveis:
        print("Valores divisíveis por 2 e 3:")
        for nome, valor in divisiveis:
            print(f"  {nome} = {valor}")
    else:
        print("Nenhum valor é divisível por 2 e por 3.")

if __name__ == "__main__":
    main()
