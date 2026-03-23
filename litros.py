tempo = float(input("Digite o tempo (em horas): "))
velocidade = float(input("Digite a velocidade média (em km/h): "))

distancia = velocidade * tempo

litros_gastos = distancia / 12
print(f"\n--- Cálculo do consumo de combustível ---")
print(f"Tempo: {tempo} horas")  
print(f"Velocidade: {velocidade} km/h")
print(f"Distância: {distancia} km")
print(f"Litros gastos: {litros_gastos:.2f} L")  