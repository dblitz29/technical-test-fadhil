import numpy as np

def cosine_similarity(a, b):
    z = np.dot(a,b)
    n_a = np.linalg.norm(a)
    n_b = np.linalg.norm(b)
    if n_a == 0 or n_b ==0:
        return 0
    return z / (n_a * n_b)