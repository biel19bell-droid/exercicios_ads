def main() -> None:
    print("=== Saudação Personalizada ===\n")

    # Ler o nome
    nome = input("Digite seu nome: ").strip()

    # Ler o sexo
    sexo = input("Digite seu sexo (M para masculino, F para feminino): ").strip().upper()

    print(f"\nNome informado: {nome}")
    print(f"Sexo informado: {sexo}")

    # Verificar se o sexo é válido
    if sexo == 'M':
        print(f"\nIlmo. Sr. {nome}")
    elif sexo == 'F':
        print(f"\nIlma. Sra. {nome}")
    else:
        print("\n❌ Sexo informado inválido. Use 'M' para masculino ou 'F' para feminino.")

    print("\n" + "=" * 40)


if __name__ == "__main__":
    main()
