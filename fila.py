"""TAD Fila (FIFO): especificacao e interface em Python.

Uma fila segue a politica FIFO (First In, First Out):
o primeiro elemento inserido e o primeiro a ser removido.

Operacoes do TAD e pre-condicoes:

1. criar() -> Fila
	Pre: nenhuma.
	Pos: retorna uma fila vazia.

2. enfileirar(x) -> None
	Pre: a fila deve existir.
	Pos: x e inserido no final da fila.

3. desenfileirar() -> T
	Pre: fila nao vazia.
	Pos: remove e retorna o elemento do inicio da fila.

4. frente() -> T
	Pre: fila nao vazia.
	Pos: retorna (sem remover) o elemento do inicio da fila.

5. vazia() -> bool
	Pre: a fila deve existir.
	Pos: indica se a fila esta vazia.

6. tamanho() -> int
	Pre: a fila deve existir.
	Pos: retorna a quantidade de elementos da fila.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar


T = TypeVar("T")


class Fila(Generic[T], ABC):
    """Interface do TAD Fila."""

    @abstractmethod
    def enfileirar(self, elemento: T) -> None:
        """Insere elemento no final da fila.

        Pre-condicao: a fila deve existir.
        """

    @abstractmethod
    def desenfileirar(self) -> T:
        """Remove e retorna o elemento do inicio da fila.

        Pre-condicao: fila nao vazia.
        """

    @abstractmethod
    def frente(self) -> T:
        """Retorna o elemento do inicio sem removelo.

        Pre-condicao: fila nao vazia.
        """

    @abstractmethod
    def vazia(self) -> bool:
        """Indica se a fila esta vazia.

        Pre-condicao: a fila deve existir.
        """

    @abstractmethod
    def tamanho(self) -> int:
        """Retorna o numero de elementos da fila.

        Pre-condicao: a fila deve existir.
        """
