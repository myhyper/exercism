def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Given strands are not in the same length.")
    cnt = 0
    for x,y in zip(strand_a, strand_b):
        if x != y: cnt += 1
    return cnt
