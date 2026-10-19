import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	arr = np.array(matrix)

    if mode == "row":
        return np.mean(arr, axis=1).tolist()
    elif mode == "column":
        return np.mean(arr, axis=0).tolist()
    else:
        raise ValueError("Mode must be 'row' or 'column'")