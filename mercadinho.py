#Resolve o problema utilizando listas. Um mercadinho de bairro expandiu seus
#caixas e funcionários, agora eles precisam de um programa que implemente uma caixa
#registradora simples. O programa deverá receber um número desconhecido de valores
#referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para
#indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor
#em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta
#operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída
#deve ser conforme o exemplo abaixo:
#Mercadinho BigBom
#Produto 1: R$ 2.20
#Produto 2: R$ 5.80
#Produto 3: R$ 0
#Total: R$ 9.00
#Dinheiro: R$ 20.00
#Troco: R$ 11.00 

print("Mercadinho Big Bom")
print("")


produtos = 1
soma = 0
lista = []

while(produtos >= 0.001):
  count = 0
  produtos = float(input(f"Preço desse produto: "))
  print(f"Produto: R$ {produtos}")
  lista.append(produtos)
  soma += produtos
  if (produtos == 0):
    print(lista)
    print(f"Soma dos produtos: {soma}") 
    #saída
    total = soma
    dinheiro = float(input("Valor em dinheiro: "))
    troco = dinheiro - total
    print(f"Dinheiro: R$ {dinheiro}")
    print(f"Troco: R$ {troco}")
    produtos = 1
    lista = []
    soma = 0