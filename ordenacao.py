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

def bubble_sort(valores):
    """Ordena uma lista em ordem crescente usando o método da bolha."""
    lista = valores.copy()
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

def merge_sort(valores):
    """Ordena uma lista em ordem crescente usando o método de ordenação por fusão."""
    if len(valores) <= 1:
        return valores

    meio = len(valores) // 2
    esquerda = merge_sort(valores[:meio])
    direita = merge_sort(valores[meio:])

    return merge(esquerda, direita)

def merge(esquerda, direita):
    """Funde duas listas ordenadas em uma única lista ordenada."""
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado

def quick_sort(valores):
    """Ordena uma lista em ordem crescente usando o método quick sort."""
    if len(valores) <= 1:
        return valores.copy()

    pivo = valores[len(valores) // 2]
    menores = [valor for valor in valores if valor < pivo]
    iguais = [valor for valor in valores if valor == pivo]
    maiores = [valor for valor in valores if valor > pivo]

    return quick_sort(menores) + iguais + quick_sort(maiores)

if __name__ == "__main__":
    exemplo = [5, 4, 3, 2, 1, 3]
    print("selection:", selection_sort(exemplo))
    print("insertion:", insertion_sort(exemplo))
    print("bubble:", bubble_sort(exemplo))
    print("merge:", merge_sort(exemplo))
    print("quick:", quick_sort(exemplo))
