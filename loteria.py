from random import randint

#Não terminei foi só um início, mas deêm uma olhada e me ajudem!

print("***************Faça a sua aposta!!!!****************")
print("")
print("Você tem direito para escolher seis números")
print("Se você acertar os seis numeros fará uma sena, se acertar 5 uma quina e 4 uma quadra")
print("premioQuadra  6.000")
print("premioQuina 45.000")
print("premioTotal 100.000")
print("")
count = 0
numSorteados = []
jogador = 0
numeroDaSorte = [10, 55, 60, 56, 18, 1]


#totalJogadores = int(input("Insira o total de jogadores dessa aposta: "))
while (count < 6):
  pergunta = input("Você deseja fazer uma aposta? (s/n)")
  if pergunta == "s":
    print(jogador)
    numSorteados = []
  elif pergunta == "n":
    break
  jogador = print(f"Jogador n° {count+1}")
  totalJogadores = int(input("Insira o total de jogadores dessa aposta: "))
  count += 1
  for i in range(6):   
    aposta = int(input(f"Aposta n° {i+1}: "))    
    if aposta < 1 or aposta > 60:
      print("Faça uma aposta válida")
      break
    numSorteados.append(aposta)   
  print(numSorteados)
    
a = set(numeroDaSorte) and set(numSorteados)  
if len(a) == 6:
  print(f"Voce ganhou o total, Divisão do prêmio: {100.000 / totalJogadores:.3f} para cada jogador da aposta ganha")
elif len(a) == 5:
  print(f"Voce ganhou a quina, Divisão do prêmio: {45.000 / totalJogadores:.3f} para cada jogador da aposta ganha")
elif len(a) == 4:
  print(f"Voce ganhou a quadra, Divisão do prêmio: {6.000 / totalJogadores:.3f} para cada jogador da aposta ganha")
else:
  print("f")
  