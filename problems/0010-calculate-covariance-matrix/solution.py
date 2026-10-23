
import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    vectors = np.array(vectors, dtype=float)

    # Calculate the mean of each vector
    averages = np.mean(vectors, axis=1, keepdims=True)

    # Subtract each vector's mean
    centered = vectors - averages

    # Calculate the covariance matrix
    n = vectors.shape[0]
    result = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            result[i, j] = np.dot(centered[i], centered[j]) / (vectors.shape[1] - 1)

    return result.tolist()