#crie um algoritmo que leia 4 notas de 10 alunos, calcule e guarde em uma lista
#a média de cada aluno. No final mostre quantos alunos tiveram a média maior ou igual a 7

lista = []
qtdNotasMaior7 = 0
soma = 0
media = 0 

for i in range(10):
  print(f"Aluno:{i+1}")
  for i in range(4):
    nota = float(input("Insira a nota desse aluno: "))
    soma += nota  
  media = soma / 4
  lista.append(media)
  soma = 0  
for c in lista:
  if c >= 7: 
    qtdNotasMaior7 += 1
print(f"Lista das notas dos alunos: {lista}")
print(f"Quantidade de notas maior que 7: {qtdNotasMaior7}")