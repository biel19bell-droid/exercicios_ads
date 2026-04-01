def obter_inteiro(mensagem: str) -> int:
   
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Erro: informe um número inteiro válido.")


def main() -> None:
    print("=" * 50)
    print("  Ordenação de Três Valores em Ordem Crescente")
    print("=" * 50 + "\n")

    print(" Digite três números inteiros:\n")
    a = obter_inteiro("Valor de A: ")
    b = obter_inteiro("Valor de B: ")
    c = obter_inteiro("Valor de C: ")

    print(f"\nValores lidos: A = {a}, B = {b}, C = {c}")
    print("\nAgora vamos ordenar esses valores em ordem crescente\n")

   
    print(" Comparação Entre A e B:")
    if a > b:
        print(f"   {a} > {b}? Sim. Então trocamos.")
        a, b = b, a  
        print(f"   Depois da troca: A = {a}, B = {b}")
    else:
        print(f"   {a} > {b}? Não. A e B já estão corretos.")

    print("\n Comparação 2 - Verificando A e C:")
    if a > c:
        print(f"   {a} > {c}? Sim. Então trocamos.")
        a, c = c, a
        print(f"   Depois da troca: A = {a}, C = {c}")
    else:
        print(f"   {a} > {c}? Não. A e C já estão corretos.")

    
    print("\n Comparação 3 - Verificando B e C:")
    if b > c:
        print(f"   {b} > {c}? Sim. Então trocamos.")
        b, c = c, b 

        print(f"   Depois da troca: B = {b}, C = {c}")
    else:
        print(f"   {b} > {c}? Não. B e C já estão corretos.")

  
    print("\n" + "=" * 50)
    print(" Resultado - Ordem Crescente:")
    print("=" * 50)
    print(f"\n  {a}  →  {b}  →  {c}\n")


if __name__ == "__main__":
    main()
