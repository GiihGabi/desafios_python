print("Eleições 2022")
print(" ")
print("Canditados: [1] Vicent Vega, [2] Jules Winnfield, [3] Marcellus Wallace")
print(" ")


vicentVega = 0
julesWinnfield = 0
marcellusWallace = 0
tentativa = 1
votoinvalido = ("Voto invalido, Por favor insira um voto válido")
qtdeleitores = int(input("Quantidade de eleitores: "))
count = 1
somav = 0
somaj = 0
somam = 0

while(count <= qtdeleitores):
  print(f"Eleitor {count}")
  voto = int(input("Insira seu voto: "))
  count = count + 1
  print("")
  if voto == 1:
    somav += voto
    vicentVega += 1
    print("Voto feito com sucesso!")
    print(f"Total de votos Vicente: {somav}")
  elif voto == 2:
    somaj += voto - 1
    julesWinnfield += 1
    print("Voto feito com sucesso!")
    print(f"Total de votos Jules: {somaj}")
  elif voto == 3:
    somam += voto - 2
    marcellusWallace += 1
    print("Voto feito com sucesso!")
    print(f"Total de votos Macellus: {somam}")
  else:
    print(votoinvalido)
    while(count < qtdeleitores and tentativa < 5):
      if voto == 1:
        somav += voto
        vicentVega += 1
        tentativa += 1
        print("Voto feito com sucesso!")
        print(f"Total de votos Vicente: {somav}")
      elif voto == 2:
        somaj += voto - 1
        julesWinnfield += 1
        tentativa += 1
        print("Voto feito com sucesso!")
        print(f"Total de votos Jules: {somaj}")
      elif voto == 3:
        somam += voto - 2
        marcellusWallace += 1
        tentativa += 1
        print("Voto feito com sucesso!")
        print(f"Total de votos Macellus: {somam}")
      elif voto != 1 and voto != 2 and voto != 3:
        voto = int(input("Insira seu voto: "))
        print(votoinvalido)
        tentativa += 1



porcentagemVicente = (somav / qtdeleitores) * 100
porcentagemJules = (somaj / qtdeleitores) * 100
porcentagemMarcellus = (somam / qtdeleitores) * 100

if porcentagemVicente > porcentagemJules and porcentagemVicente > porcentagemMarcellus:
  print(f"O Vicente Vega ganhou a eleição com {porcentagemVicente:.2f}% dos votos")
elif porcentagemJules > porcentagemVicente and porcentagemJules > porcentagemMarcellus:
  print(f"O Jules Winnfield ganhou a eleição com {porcentagemJules:.2f}% dos votos")
elif porcentagemMarcellus > porcentagemVicente and porcentagemJules > porcentagemMarcellus:
  print(f"O Marcellus Wallace ganhou a eleição com {porcentagemMarcellus:.2f}% dos votos")
elif porcentagemVicente == porcentagemJules and porcentagemVicente == porcentagemMarcellus:
  print(f"Ouve um empate")
elif porcentagemJules == porcentagemVicente and porcentagemJules == porcentagemMarcellus:
  print(f"Ouve um empate")
elif porcentagemMarcellus == porcentagemVicente and porcentagemJules == porcentagemMarcellus:
  print(f"Ouve um empate")
elif porcentagemVicente < porcentagemJules or porcentagemVicente < porcentagemMarcellus and porcentagemJules == porcentagemMarcellus:
  print(f"Ouve um empate")
elif porcentagemJules < porcentagemVicente or porcentagemJules < porcentagemMarcellus and porcentagemVicente == porcentagemMarcellus:
  print(f"Ouve um empate")
elif porcentagemMarcellus < porcentagemVicente or porcentagemMarcellus < porcentagemJules and porcentagemVicente == porcentagemMarcellus:
  print(f"Ouve um empate")
elif porcentagemMarcellus and porcentagemVicente and porcentagemMarcellus < porcentagemJules and porcentagemVicente == porcentagemJules:
  print(f"Ouve um empate")