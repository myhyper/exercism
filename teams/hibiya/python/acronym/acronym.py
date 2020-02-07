alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def convert(s): str1 = "";return(str1.join(s)) 
def abbreviate(words):
    arr = []
    for word in words.replace('-',' ').split():
        for ch in word.upper():
            if ch in alphanumeric:
                arr.append(ch)
                break
    return convert(arr)