lista_mesclada = [1, 2, 3, "Olá, Python", True, 12.6]
print("Conteúdo inicial da lista:", lista_mesclada)
lista_mesclada.append(["Lista aninhada"])
print("Lista após adicionar uma lista aninhada com 'append':", lista_mesclada)
lista_mesclada.insert(4, 5)
print("Lista após inserir o valor 5 na posição 4 com 'insert':", lista_mesclada)
print("Tamanho atual da lista:", len(lista_mesclada))
del lista_mesclada[1]
print("Lista após remover o item na posição 1:", lista_mesclada)
nova_lista_mesclada = lista_mesclada[:4]
print("Conteúdo da nova lista 'nova_lista_mesclada':", nova_lista_mesclada)
