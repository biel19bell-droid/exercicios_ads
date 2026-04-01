def obter_inteiro(mensagem: str) -> int:
   
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print(" Informe um número inteiro válido.")


def main() -> None:
    print(" Encontrar Maior e Menor Valor \n")

    
    a = obter_inteiro("Digite o valor de A: ")
    maior = a
    menor = a

    print(f"Primeiro valor: A = {a}")

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

    print(f"\nValores lidos: A={a}, B={b}, C={c}, D={d}, E={e}")

    print("RESULTADO:")
    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")
  


if __name__ == "__main__":
    main()
