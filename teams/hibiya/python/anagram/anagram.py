def find_anagrams(word, candidates):
    arr_ori = list(word.lower())
    arr_ori.sort()
    rtv = []
    for cand in candidates:
        cand_low = cand.lower()
        arr_cand = list(cand_low)
        arr_cand.sort()
        if word.lower() != cand_low and arr_ori == arr_cand:
            rtv.append(cand)
    return rtv