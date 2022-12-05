atleta = int(input("Insira a quantidade de atletas: "))
qtdSaltos = int(input("Quantidade de saltos: "))
maiorMedia = 0 
maiorAtleta = ""


for i in range(1, atleta + 1):
  print("")
  print(f"Atleta n°: {i}")
  nome = input(f"Digite o nome do atleta: ")
  soma = 0
  media = 0
  maior = 0 
  menor = 0
  for s in range(1, qtdSaltos + 1):
    print(f"Salto n°: {s}")
    salto = float(input(f"Valor do salto: "))
    soma += salto

    if s == 1:
      maior = salto
      menor = salto
    if salto > maior:
      maior = salto
    if salto < menor:
      menor = salto 
      
  media = soma / qtdSaltos
  print(f"Melhor salto: {maior}")
  print(f"Pior salto: {menor}")
  print(f"Valor da média de salto do atleta: {media}m")

  if media > maiorMedia:
    maiorMedia = media
    maiorAtleta = nome
print("") 
print(f"O {maiorAtleta}, Ganhou o atletismo com a média: {maiorMedia}")