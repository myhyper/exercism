def is_factor_of(f, n):
    if n % f == 0: return True
    return False
def convert(number):
    rtv = ""
    if is_factor_of(3, number): rtv += "Pling"
    if is_factor_of(5, number): rtv += "Plang"
    if is_factor_of(7, number): rtv += "Plong"
    return str(number) if "" == rtv else rtv