# # 1
numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))

print(f"adição = {numero1 + numero2}\nSubtração = {numero1 - numero2}\nMultiplicação = {numero1 * numero2}\nDivisão = {numero1 / numero2}")

# 2
numero = int(input("digite um numero: "))

if(numero % 2 == 0):
    print(f"{numero} é par")
else:
    print(f"{numero} é impar")

# 3
idade = int(input("Qual sua idade? "))
temCarteira = input("Você tem carteira de motorista: (sim/não) ").lower()

if(idade >= 18 and idade <= 30):
    print("Idade entre 18 e 30 anos")
else:
    print("Idade menor que 18 anos ou maior que 30 anos")

if (temCarteira == "sim"):
    print("Tem carteira!")
else:
    print("Não tem carteira!")