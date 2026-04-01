nome = input("Nome do aluno: ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2

if media < 3:
    situacao = "Reprovado"
elif media < 5:
    situacao = "Exame"
else:
    situacao = "Aprovado"

print(f"\nAluno: {nome}")
print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")