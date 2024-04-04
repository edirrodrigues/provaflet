

lista_compra = ["arroz","feijão","quiabo"]
print("lista de comprasoriginal:",lista_compra) 

lista_compra.pop(1)
print("após remover o feijão:",lista_compra)

indice_quiabo = lista_compra.index("quiabo")
print("O índice do 'quiabo' na lista:", indice_quiabo)

# Contando quantas vezes 'arroz' aparece na lista
quantidade_arroz = lista_compra.count("arroz")
print("Quantidade de 'arroz' na lista:", quantidade_arroz)

# Ordenando a lista em ordem alfabética
lista_compra.sort()
print("Lista de compras ordenada:", lista_compra)

# Revertendo a ordem dos elementos na lista
lista_compra.reverse()
print("Lista de compras reversa:", lista_compra)