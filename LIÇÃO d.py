def obter_nota(numero: int) -> float:
    while True:
        try:
            valor = float(input(f"Nota {numero}: ").replace(',', '.'))
            if 0 <= valor <= 10:
                return valor
            print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Valor inválido. Informe um número.")


def main() -> None:
    print("=== Cálculo de Média Escolar ===\n")

    # Ler as 4 notas bimestrais
    n1 = obter_nota(1)
    n2 = obter_nota(2)
    n3 = obter_nota(3)
    n4 = obter_nota(4)

    # Calcular primeira média
    md1 = (n1 + n2 + n3 + n4) / 4

    print(f"\nMédia das notas bimestrais: {md1:.1f}")

    # Verificar aprovação
    if md1 >= 7:
        print("Status: Aprovado")
        print(f"Média final: {md1:.1f}")
    else:
        print("Média abaixo de 7. Você será submetido(a) a exame.\n")

        # Ler nota de exame
        ne = obter_nota("Exame")

        # Calcular segunda média
        md2 = (md1 + ne) / 2

        print(f"\nMédia com exame: {md2:.1f}")

        # Verificar aprovação em exame
        if md2 >= 5:
            print("Status: Aprovado em exame")
        else:
            print("Status: Reprovado")

        print(f"Média final: {md2:.1f}")


if __name__ == "__main__":
    main()
