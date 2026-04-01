import math


def obter_numero(mensagem: str) -> float:
    """Pede um número ao usuário de forma segura"""
    while True:
        try:
            valor = float(input(mensagem).replace(',', '.'))
            return valor
        except ValueError:
            print("Erro: informe um número válido.")


def main() -> None:
    print(" Resolvedor de Equação de 2º Grau (Fórmula de Bhaskara) \n")

    # Pedir os coeficientes da equação: Ax² + Bx + C = 0
    a = obter_numero("Digite o coeficiente A: ")
    b = obter_numero("Digite o coeficiente B: ")
    c = obter_numero("Digite o coeficiente C: ")

    # Verificar se é realmente uma equação de 2º grau
    if a == 0:
        print("\nErro: O coeficiente A não pode ser zero!")
        print("Isso não é uma equação de 2º grau completa.")
        return

    print(f"\nEquação: {a}x² + {b}x + {c} = 0")
    print("=" * 40)

    # Calcular delta (discriminante)
    delta = (b * b) - (4 * a * c)

    print(f"\nDelta = B² - 4AC")
    print(f"Delta = {b}² - 4 × {a} × {c}")
    print(f"Delta = {b * b} - {4 * a * c}")
    print(f"Delta = {delta}")

    # Analisar o delta e encontrar as soluções
    print("\n" + "=" * 40)

    if delta < 0:
        print("\nDelta é Negativo")
        print(" Não existe solução real.")
        print("(As soluções são números complexos)")

    elif delta == 0:
        print("\nDelta é Zero")
        print(" Existe UMA solução real.")

        # Fórmula: x = -B / 2A
        x = -b / (2 * a)

        print(f"\nFórmula: x = -B / 2A")
        print(f"x = -{b} / (2 × {a})")
        print(f"x = -{b} / {2 * a}")
        print(f"\nResultado: x = {x}")

    else:  # delta > 0
        print("\nDelta é Postivo ")
        print(" Existem Duas soluções reais e diferentes.")

        # Calcular raiz de delta
        raiz_delta = math.sqrt(delta)

        # Fórmula: x = (-B ± √delta) / 2A
        x1 = (-b + raiz_delta) / (2 * a)
        x2 = (-b - raiz_delta) / (2 * a)

        print(f"\nFórmula: x = (-B ± √delta) / 2A")
        print(f"√delta = √{delta} = {raiz_delta:.4f}")

        print(f"\nX₁ = (-B + √delta) / 2A")
        print(f"X₁ = (-{b} + {raiz_delta:.4f}) / {2 * a}")
        print(f"X₁ = {x1:.4f}")

        print(f"\nX₂ = (-B - √delta) / 2A")
        print(f"X₂ = (-{b} - {raiz_delta:.4f}) / {2 * a}")
        print(f"X₂ = {x2:.4f}")


if __name__ == "__main__":
    main()
