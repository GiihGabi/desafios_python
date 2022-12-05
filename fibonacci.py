import math

count = 0
n = 0
v = int(input("Insira um número: "))

while(n <= v):
  n = int(input("Insira um número: "))
  formula = int(((1 + math.sqrt(5)) ** n - (1 - math.sqrt(5)) ** n) / (2 ** n * math.sqrt(5)))
  print(f"A sequência conforme Fibonacci é: {formula}")
  count = count + 1