#Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua
#posição na lista.

lista = []

for i in range(1, 5 + 1):
  num = int(input(f"Insira um número inteiro {i}: "))
  lista.append(num)
  print(f"O {num} está na posição: {len(lista)}")
print(lista)