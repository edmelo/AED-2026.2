def selection_sort(valores):
	"""Ordena uma lista em ordem crescente usando seleção direta."""
	lista = valores.copy()

	for i in range(len(lista) - 1):
		menor = i
		for j in range(i + 1, len(lista)):
			if lista[j] < lista[menor]:
				menor = j

		if menor != i:
			lista[i], lista[menor] = lista[menor], lista[i]

	return lista

"""testa o metodo com alguns valores."""
a = [5, 4, 3, 2, 1, 3]
print(selection_sort(a))

def insertion_sort(valores):
    """Ordena uma lista em ordem crescente usando inserção direta."""
    lista = valores.copy()

    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

    return lista

"""testa o metodo com alguns valores."""
b = [5, 4, 3, 2, 1, 3]
print(insertion_sort(b))