#crie um algoritmo que leia 20 números inteiros e os guarde em um lista
#alem de guardar todos em uma unica lista, separe os numeros pares em uma lista "par"
#e os impares em uma lista "impar". No final mostre as listas e seus valores

a = []
par = []
impar= []

for i in range(0, 20):
  b = int(input("Insira os números de 0 a 20: "))
  a.append(b)
  if (b % 2 == 0) :
    par.append(b)
  else:
    impar.append(b)
    
print(a)
print(f"Par: {par} - Ímpar: {impar}")
print(f"Lista: {a} - Par: {par} - Ímpar: {impar}")