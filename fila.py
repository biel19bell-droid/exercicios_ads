from datetime import date


def classificar_fila(idade: int) -> str:
    if idade < 60:
        return "Fila normal"
    if idade < 80:
        return "Fila especial"
    return "Fila 80+"


def main() -> None:
    print("=== Fila de Atendimento ===")
    nome = input("Nome: ").strip()

    try:
        ano_nasc = int(input("Ano de nascimento: ").strip())
    except ValueError:
        print("Valor inválido. Informe um ano numérico.")
        return

    ano_atual = date.today().year
    idade = ano_atual - ano_nasc

    if idade < 0:
        print("Ano de nascimento inválido.")
        return

    fila = classificar_fila(idade)

    print("\nResultado:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Fila correta: {fila}")


if __name__ == "__main__":
    main()
