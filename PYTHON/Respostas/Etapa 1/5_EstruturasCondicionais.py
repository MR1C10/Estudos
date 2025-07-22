# 1
numero = int(input("Digite um número: "))

if (numero > 0):
    print(f"{numero} é positivo")
elif (numero < 0):
    print(f"{numero} é negativo")
else:
    print(f"{numero} é zero")

print()

# 2
nota = float(input("Digite a nota do aluno (0 a 10): "))

if (nota >= 7):
    print("Aluno aprovado!")
elif (nota >= 5 and nota < 7):
    print("Aluno em recuperação")
else:
    print("Aluno reprovado")

print()

# 3
idade = int(input("Digite sua idade: "))

if (idade <= 12):
    print("Criança")
elif (idade >= 13 and idade <= 17):
    print("Adolescente")
elif (idade >= 18 and idade <= 59):
    print("Adulto")
else:
    print("Idoso")