import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    gradient = np.array(gradient, dtype=float)
    magnitude = float(np.linalg.norm(gradient))

    if magnitude == 0:
        direction, descent_direction = gradient - gradient, gradient -gradient
	else:
		direction = gradient / magnitude
		descent_direction = -direction

    return {
        'magnitude': magnitude,
        'direction': direction.tolist(),
        'descent_direction': descent_direction.tolist()
    }