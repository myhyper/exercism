def find_anagrams(word, candidates):
    a = list(word.lower())
    a.sort()
    rtv = []
    for w in candidates:
        b = list(w.lower())
        b.sort()
        
        if word.lower() != w.lower() and a == b:
            rtv.append(w)
    return rtv