import random
def weighted_srs(data, n, weights, with_replacement):
    if with_replacement: return random.choices(data, weights=weights, k=n)
    sample, d, w = [], list(data), list(weights)
    for i in range(n):
        picked = random.choices(d, weights=w, k=1)
        sample += picked
        index = d.index(picked[0])
        del d[index], w[index]
    return sample
