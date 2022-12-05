#Binario para Decimal
numeroBinario = int(input("Digite um número em binário: "))
binarioDecimal = int(str(numeroBinario), 2)
print(f"O número binário {numeroBinario} em decimal é: {binarioDecimal}")
print(" ")
#Decimal para Binário
decimal = int(input("Digite um número em decimal: "))
binario = bin(decimal)
print(f"O número decimal {decimal} em binário é: {binario[2:]}")
print(" ")
#Decimal para Octal
decimal2 = int(input("Digite um número em decimal: "))
octal = oct(decimal2)
print(f"O número decimal {decimal2} em Octal é: {octal[2:]}")
print(" ")
#Decimal para Hexadecimal
decimal3 = int(input("Digite um número em decimal: "))
hexadecimal = hex(decimal3)
print(f"O número decimal {decimal3} em Hexadecimal é: {hexadecimal[2:]}")
print(" ")