from typing import List

Vector = List[float]
Matrix = List[List[float]]

def add(v: Vector, w: Vector) -> Vector:
    """Adds corresponding elements"""
    assert len(v) == len(w)
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v) == len(w)
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums all corresponding elements"""
    # Check that vectors is not empty
    assert vectors, "no vectors provided"

    # Check that vectors are the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "vectors have different sizes"

    # The i-th element of the result is the sum of every vector[i]
    return[sum(vector[i] for vector in vectors) for i in range(num_elements)]

def scalar_multiply(c: float, v: Vector) -> Vector:
    """multiplies every element by c"""
    return [c * v_i for v_i in v]

def vector_mean(vectors: List[Vector]) -> Vector:
    """computes the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v: Vector, w: Vector) -> float:
    """computes v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), "vectors must be th esame length"
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v: Vector) -> float:
    """returns v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

def magnitude(v: Vector) -> float:
    """returns the magnitude of v"""
    return math.sqrt(sum_of_squares(v))

def distance(v: Vector, w: Vector) -> float:
    """computes the distance beteween v and w"""
    return magnitude(subtract(v,w))
