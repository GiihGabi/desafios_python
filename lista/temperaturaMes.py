#– Faça um algoritmo que receba a temperatura média de cada mês do ano e
#armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as
#temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso:
#1 – Janeiro, 2 – Fevereiro, . . . ).

ano = input("Digite o ano: ")
meses = ["Janeiro","Fevereiro", "Março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro",]
listaTemperatura = []
soma = 0

for i in range(12):
  a = float(input(f"Digite a temperatura do mês {meses[i]} em ºC: "))
  listaTemperatura.append(a)
  soma += a
  media = soma / 12
print(f"Soma: {soma}")
print(f"Média das temperaturas: {media:.2f} °C")
print(f"Lista das temperaturas: {listaTemperatura}")
print("")
print("*****Temperaturas acima da média anual****")
print("")
for i in range(12):
  if listaTemperatura[i] > media:
    print(f"{i+1} - {meses[i].capitalize()}")