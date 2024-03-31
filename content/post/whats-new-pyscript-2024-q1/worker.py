from pyscript import sync

def pseudorandom(seed: int, iters: int):
    """Linear congruential generator. Parameters borrowed from POSIX and are probably bad"""
    modulus = 2**48
    a = 25214903917 
    increment = 11

    for _ in range(iters):
        seed = (a * seed + increment) % modulus
    return seed % (2 ** 47)

sync.pseudorandom = pseudorandom