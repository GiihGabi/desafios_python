#Faça um algoritmo que leia dois vetores com 10 elementos cada. Gere um terceiro
#vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos
#dois outros vetores.

vetor1 = []
vetor2 = []
vetor3 = []

for i in range(10):
  a = int(input(f"Números do primeiro vetor - {i+1}: "))
  vetor1.append(a)
for c in range(10):
  b = int(input(f"Números do segundo vetor - {c+1}: "))
  vetor2.append(b)
  for d in range(1):
    vetor3.append(vetor1)
    vetor3.append(vetor2)
print(vetor3)
print(len(vetor3))