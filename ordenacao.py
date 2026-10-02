import random


class AlgOrdem:
    def selection(self, valores):
        lista = valores.copy()

        for i in range(len(lista) - 1):
            menor = i
            for j in range(i + 1, len(lista)):
                if lista[j] < lista[menor]:
                    menor = j

            if menor != i:
                lista[i], lista[menor] = lista[menor], lista[i]

        return lista

    def insertion(self, valores):
        lista = valores.copy()

        for i in range(1, len(lista)):
            chave = lista[i]
            j = i - 1

            while j >= 0 and lista[j] > chave:
                lista[j + 1] = lista[j]
                j -= 1

            lista[j + 1] = chave

        return lista

    def bubble(self, valores):
        lista = valores.copy()
        n = len(lista)

        for i in range(n):
            for j in range(0, n - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

        return lista

    def merge(self, valores):
        if len(valores) <= 1:
            return valores.copy()

        meio = len(valores) // 2
        esquerda = self.merge(valores[:meio])
        direita = self.merge(valores[meio:])

        return self._merge(esquerda, direita)

    def _merge(self, esquerda, direita):
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

    def quick(self, valores):
        if len(valores) <= 1:
            return valores.copy()

        pivo = valores[len(valores) // 2]
        menores = [valor for valor in valores if valor < pivo]
        iguais = [valor for valor in valores if valor == pivo]
        maiores = [valor for valor in valores if valor > pivo]

        return self.quick(menores) + iguais + self.quick(maiores)

    def  heap(self, valores):
        def heapify(lista, n, i):
            maior = i
            esquerda = 2 * i + 1
            direita = 2 * i + 2

            if esquerda < n and lista[esquerda] > lista[maior]:
                maior = esquerda

            if direita < n and lista[direita] > lista[maior]:
                maior = direita

            if maior != i:
                lista[i], lista[maior] = lista[maior], lista[i]
                heapify(lista, n, maior)

        lista = valores.copy()
        n = len(lista)

        for i in range(n // 2 - 1, -1, -1):
            heapify(lista, n, i)

        for i in range(n - 1, 0, -1):
            lista[i], lista[0] = lista[0], lista[i]
            heapify(lista, i, 0)

        return lista


if __name__ == "__main__":
    algoritmos = AlgOrdem()
    valores = [random.randint(1, 100) for _ in range(20)]
    print(algoritmos.selection(valores))
    print(algoritmos.insertion(valores))
    print(algoritmos.bubble(valores))
    print(algoritmos.merge(valores))
    print(algoritmos.quick(valores))
    print(algoritmos.heap(valores))
