def calcular_imc(peso: float, altura: float) -> float:
    return peso / (altura * altura)


def classificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "Abaixo do peso normal"
    if imc < 25.0:
        return "Peso normal"
    if imc < 30.0:
        return "Excesso de peso"
    if imc < 35.0:
        return "Obesidade classe I"
    if imc < 40.0:
        return "Obesidade classe II"
    return "Obesidade classe III"


def ler_valor(nome_campo: str) -> float:
    texto = input(f"{nome_campo}: ").strip().replace(',', '.')
    valor = float(texto)
    if valor <= 0:
        raise ValueError("Valor deve ser maior que zero")
    return valor


def main() -> None:
    print("=== Cálculo de IMC ===")
    nome = input("Nome: ").strip()

    try:
        peso = ler_valor("Peso (kg)")
        altura = ler_valor("Altura (m)")
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
        return

    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    print("\nResultado:")
    print(f"Nome: {nome}")
    print(f"IMC: {imc:.1f}")
    print(f"Classificação: {classificacao}")


if __name__ == "__main__":
    main()
