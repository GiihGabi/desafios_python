#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O
#resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer
#um programa em Python utilizando listas, que receba o nome e as cinco distâncias alcançadas
#pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa
#deve ser encerrado quando
#não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
#Atleta: Rodrigo Curvêllo
#Primeiro Salto: 6.5 m
#Segundo Salto: 6.1 m
#Terceiro Salto: 6.2 m
#Quarto Salto: 5.4 m
#Quinto Salto: 5.3 m
#Resultado final:
#Atleta: Rodrigo Curvêllo
#Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
#Média dos saltos: 5.9 m

atleta = int(input("Insira a quantidade de atletas: "))
print("")
lista = []
soma = 0
vazio = 0
for i in range(1, atleta + 1):
  print("")
  print(f"Atleta n°: {i}")
  nome = input(f"Digite o nome do atleta: ")
  media = 0
  if nome == "":
    break
  for s in range(1, 5 + 1):    
    print(f"Salto n° {s}: ")
    salto = float(input(f"Valor do salto: "))
    soma += salto
    lista.append(salto)
  print("Resultado final:")
  print(f"Atleta: {nome}")  
  print(f"Saltos: {lista}")
  lista = []
  media = soma / 5
  print(f"Média dos saltos: {media}")