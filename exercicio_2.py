# Conversor de Medidas: Crie um programa que receba um valor em metros e o exiba convertido em centímetros e milímetros

metros = float(input("Digite o valor em metros: "))
cm = metros * 100
mm = metros * 1000

print(f"{metros} metros correspondem à:")
print(f"centímetos: {cm}cm")
print(f"milímetros: {mm}mm")
