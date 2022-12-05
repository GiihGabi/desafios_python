#Crie um algoritmo que leia 10 números, guarde-os em uma lista “ORDEM”. Depois
#gere uma segunda lista “REVERSA” que deve conter os elementos em ordem inversa a original

lista = []


for i in range(10):
  num = int(input("Insira o número: "))
  lista.append(num)
print(lista)
lista.sort()
print(lista)
lista.reverse()
print(lista)