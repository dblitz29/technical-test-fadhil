# Just search up if numpy considered as High level library or not, and it is 
def cosine_similarity(vec1,vec2):
    if len(vec1) != len(vec2):
        return "Error: Vectors must be the same length"
    dot = 0.0 
    n_vec1 = 0.0
    n_vec2 = 0.0
    for x,y in zip (vec1,vec2):
        dot += x*y
        n_vec1 += x*x
        n_vec2 += y*y
    
    if n_vec1 == 0 or n_vec2 ==0:
        return 0

    return dot / ((n_vec1**0.5) * (n_vec2**0.5))
