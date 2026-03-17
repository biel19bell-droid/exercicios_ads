# Conversor de Moeda: Crie um programa que leia quanto dinheiro uma pessoa tem em R$, e mostre quantos dólares ela pode comprar (considere US$ 1,00 = R$ 5,00)

reais = float(input("Digite a sua quantia de dinheiro em R$: R$ "))
taxa = 5.00
dolares = reais / taxa

print(f"Com R$ {reais} é possível comprar US$ {dolares}") 