def convert(n):
    rtv = ""
    if n % 3 == 0: rtv += "Pling"
    if n % 5 == 0: rtv += "Plang"
    if n % 7 == 0: rtv += "Plong"
    if "" == rtv:
        return str(n)
    else: return rtv