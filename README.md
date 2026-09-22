# AED-2026.2

Material de apoio para estudar **Algoritmos e Estruturas de Dados (AED)**.

## Como pensar em um algoritmo

Um algoritmo é uma receita: recebe uma entrada, executa passos bem definidos e
produz uma saída. Para estudar, faça sempre estas três perguntas:

1. **O que muda a cada repetição?**
2. **Qual é a condição de parada?**
3. **Quanto trabalho é feito quando a entrada cresce?**

Nos exemplos abaixo, a lista `[5, 4, 3, 2, 1, 3]` será chamada de `L`.

## Ordenação: colocar valores em ordem

### 1. Selection sort (seleção)

**Ideia simples:** procure o menor valor da parte ainda desorganizada e
coloque-o na próxima posição.

Exemplo:

```text
[5, 4, 3, 2, 1, 3]
 ^----- procure o menor: 1
[1, 4, 3, 2, 5, 3]
    ^-- procure o menor restante: 2
[1, 2, 3, 4, 5, 3]
```

Depois de cada volta, a parte à esquerda já está certa. O código está em
`selection_sort` em `ordenacao.py`.

- Melhor, médio e pior caso: **O(n²)**
- Memória extra: **O(1)** (fora a cópia da lista)
- Lembrete para a prova: **seleciona o menor e troca**.

### 2. Insertion sort (inserção)

**Ideia simples:** mantenha a parte esquerda ordenada e insira nela o próximo
elemento, como fazemos ao organizar cartas na mão.

```text
[5] 4 3 2 1 3       4 entra antes de 5
[4, 5] 3 2 1 3      3 entra antes de 4
[3, 4, 5] 2 1 3
```

- Melhor caso (lista já ordenada): **O(n)**
- Médio e pior caso: **O(n²)**
- Lembrete para a prova: **retira uma chave e desloca os maiores**.

### 3. Bubble sort (bolha)

**Ideia simples:** compare vizinhos. Se estiverem invertidos, troque-os. O
maior valor “borbulha” até o final a cada passagem.

```text
5 4 3 2 1 3
5 4 3 1 2 3   (2 e 1 foram trocados)
4 3 1 2 3 5   (5 chegou ao fim)
```

- Melhor caso: **O(n²)** nesta implementação
- Médio e pior caso: **O(n²)**
- Memória extra: **O(1)** (fora a cópia da lista)
- Lembrete para a prova: **compara vizinhos e empurra o maior**.

### 4. Merge sort (fusão)

**Ideia simples:** divida a lista até sobrarem listas de um elemento; depois
una duas listas já ordenadas.

```text
[5, 4, 3, 2] -> [5, 4] [3, 2] -> [5] [4] [3] [2]
              -> [4, 5] [2, 3] -> [2, 3, 4, 5]
```

- Melhor, médio e pior caso: **O(n log n)**
- Memória extra: **O(n)**
- Lembrete para a prova: **divide, ordena as partes, funde**.

### 5. Quick sort

**Ideia simples:** escolha um pivô e separe os valores em menores, iguais e
maiores. Ordene recursivamente apenas menores e maiores.

Para o pivô `3`:

```text
[5, 4, 3, 2, 1, 3]
menores = [2, 1] | iguais = [3, 3] | maiores = [5, 4]
```

- Caso médio: **O(n log n)**
- Pior caso: **O(n²)** (quando as divisões ficam muito desequilibradas)
- Lembrete para a prova: **pivô, partição e recursão**.

### Comparação rápida

| Algoritmo | Melhor | Médio | Pior | Ideia-chave |
| --- | ---: | ---: | ---: | --- |
| Selection | O(n²) | O(n²) | O(n²) | Escolher o menor |
| Insertion | O(n) | O(n²) | O(n²) | Inserir uma chave |
| Bubble | O(n²) | O(n²) | O(n²) | Trocar vizinhos |
| Merge | O(n log n) | O(n log n) | O(n log n) | Dividir e fundir |
| Quick | O(n log n) | O(n log n) | O(n²) | Usar um pivô |

`n` é a quantidade de elementos. Não confunda `O(n²)` com “sempre demora”:
para listas pequenas, a diferença pode ser imperceptível. A notação serve para
comparar o crescimento do trabalho.

## Fila (FIFO)

Uma fila funciona como uma fila de pessoas: **quem chega primeiro sai
primeiro** (First In, First Out).

```text
enfileirar("Ana")  -> [Ana]
enfileirar("Bia")  -> [Ana, Bia]
desenfileirar()    -> sai Ana; fica [Bia]
frente()           -> olha Bia sem remover
```

Operações da interface `Fila` em `fila.py`:

| Operação | Ação |
| --- | --- |
| `enfileirar(x)` | coloca `x` no final |
| `desenfileirar()` | remove e retorna o primeiro |
| `frente()` | consulta o primeiro sem remover |
| `vazia()` | informa se não há elementos |
| `tamanho()` | informa quantos elementos existem |

Uma fila é útil em atendimento, impressão de documentos e busca em largura
(BFS). A condição importante é: **não se pode remover nem consultar a frente
de uma fila vazia**.

## Roteiro para estudar antes da prova

1. Explique cada algoritmo em uma frase, sem olhar o código.
2. Simule `[5, 4, 3, 2, 1, 3]` no papel e marque o que fica garantido após
   cada repetição.
3. Decore a ideia, não só o nome: `selection = menor`, `insertion = carta`,
   `bubble = vizinho`, `merge = divide/funde`, `quick = pivô`.
4. Compare os casos melhor, médio e pior usando a tabela.
5. Para cada método, responda: “ele modifica a lista original ou devolve uma
   cópia?”. Neste projeto, as ordenações simples copiam a lista; `merge_sort`
   e `quick_sort` também devolvem novas listas.

Para executar os exemplos:

```bash
python ordenacao.py
```
