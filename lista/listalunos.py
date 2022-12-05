#crie um algoritmo que leia 4 notas de 10 alunos, calcule e guarde em uma lista
#a média de cada aluno. No final mostre quantos alunos tiveram a média maior ou igual a 7

lista = []
qtdNotasMaior7 = 0

for i in range(1,3 +1):
  soma = 0
  media = 0 
  print(f"Aluno:{i}")
  for i in range(4):
    nota = float(input("Insira a nota desse aluno: "))
    soma += nota
  media = soma / 4
  lista.append(media)
  print(media > 7)
for a in range(lista):
  if lista >= 7:
    print(lista)
  else:
    print("")
print(lista)