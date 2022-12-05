uma_lista = [1, 2, 3, 4,5,6]
outra_lista = [2,3, 4, 5, 6]
comp = []
a = set(uma_lista) and set(outra_lista)
comp.append(a)
print(a)
print(comp)
print(len(a))