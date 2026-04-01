def obter_inteiro(mensagem: str) -> int:

    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Erro: informe um número inteiro válido.")


def main() -> None:
    print("=== Verificação de Divisibilidade por 2 e 3 ===\n")

    a = obter_inteiro("Digite o valor de A: ")
    b = obter_inteiro("Digite o valor de B: ")
    c = obter_inteiro("Digite o valor de C: ")
    d = obter_inteiro("Digite o valor de D: ")

    print(f"\nValores lidos: A={a}, B={b}, C={c}, D={d}")

  
    divisiveis = []

    print("\nVerificando divisibilidade por 2 e 3" \
    ":")

    if a % 2 == 0 and a % 3 == 0:
        divisiveis.append(("A", a))
        print(f" A = {a} é divisível por 2 e por 3")
    else:
        print(f"✗ A = {a} não é divisível por 2 e por 3")

    if b % 2 == 0 and b % 3 == 0:
        divisiveis.append(("B", b))
        print(f" B = {b} é divisível por 2 e por 3")
    else:
        print(f" B = {b} não é divisível por 2 e por 3")

    if c % 2 == 0 and c % 3 == 0:
        divisiveis.append(("C", c))
        print(f" C = {c} é divisível por 2 e por 3")
    else:
        print(f" C = {c} não é divisível por 2 e por 3")

    if d % 2 == 0 and d % 3 == 0:
        divisiveis.append(("D", d))
        print(f" D = {d} é divisível por 2 e por 3")
    else:
        print(f" D = {d} não é divisível por 2 e por 3")

    print("\n" + "=" * 50)
    if divisiveis:
        print("Valores divisíveis por 2 e 3:")
        for nome, valor in divisiveis:
            print(f"  {nome} = {valor}")
    else:
        print("Nenhum valor é divisível por 2 e por 3.")

