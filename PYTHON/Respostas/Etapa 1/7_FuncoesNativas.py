# 1
palavra = input("Digite uma palavra: ")
print(len(palavra))

print()

# 2
numeros = input("Digite 5 numeros separados por espaço: ")
listaNumeros = [int(x) for x in numeros.split()]

print(f"A soma dos números é: {sum(listaNumeros)}")
print(f"O maior número é: {max(listaNumeros)}")

print()

# 3
nome = "Maricio"
idade = 19
Fome = True
print(f"{type(nome)}\n{type(idade)}\n{type(Fome)}")