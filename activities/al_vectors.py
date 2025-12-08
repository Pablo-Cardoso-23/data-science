from typing import List, Tuple, Callable
import math

# VETORES

Vector = List[float]

height_weight_age = [70,
                     170,
                     40]

grades = [95, 80, 75, 62]

def add(v: Vector, w: Vector) -> Vector:
    """Soma os elementos correspondentes."""
    assert len(v) == len(w), "Vectors must be the same length"

    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

def subtract(v: Vector, w: Vector) -> Vector:
    """Subtrai os elementos correspondentes."""
    assert len(v) == len(w), "Vectors must be the same length"

    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]

def vector_sum(vectors: List[Vector]) -> Vector:
    """Soma todos os elementos correspondentes."""
    assert vectors, "No vectors provided!"
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "All vectors must be the same length"

    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]

assert vector_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [12, 15, 18]

def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiplica cada elemento por um escalar."""
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]

def vector_mean(vectors: List[Vector]) -> Vector:
    """Calcula o vetor médio."""
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]

def dot(v: Vector, w: Vector) -> float:
    """Calcula o produto escalar de v e w."""
    assert len(v) == len(w), "Vectors must be the same length"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32

def sum_of_squares(v: Vector) -> float:
    """Retorna a soma dos quadrados dos elementos do vetor."""
    return dot(v, v)

assert sum_of_squares([1, 2, 3]) == 14

def magnitude(v: Vector) -> float:
    """Retorna a magnitude (ou comprimento) do vetor v."""
    return math.sqrt(sum_of_squares(v))

assert magnitude([3, 4]) == 5.0

def squared_distance(v: Vector, w: Vector) -> float:
    """Computa (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(subtract(v, w))

def distance(v: Vector, w: Vector) -> float:
    """Computa a distância Euclidiana entre v e w."""
    return math.sqrt(squared_distance(v, w))

# MATRIZES

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[1, 2],
     [3, 4],    
     [5, 6]]

def shape(A: List[List[float]]) -> Tuple[int, int]:
    """Retorna o número de linhas e colunas da matriz A."""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)

def get_row(A: List[List[float]], i: int) -> Vector:
    """Retorna a i-ésima linha da matriz A."""
    return A[i]

def get_column(A: List[List[float]], j: int) -> Vector:
    """Retorna a j-ésima coluna da matriz A."""
    return [A_i[j] for A_i in A]


def make_matrix(num_rows: int, num_cols: int,
                entry_fn: Callable[[int, int], float]) -> List[List[float]]:
    """Cria uma matriz onde o elemento (i, j) é dado por entry_fn(i, j)."""
    return [[entry_fn(i, j) for j in range(num_cols)]
            for i in range(num_rows)]

def identity_matrix(n: int) -> List[List[float]]:
    """Cria uma matriz identidade de tamanho n x n."""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)
