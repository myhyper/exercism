arr = "abcdefghijklmnopqrstuvwxyz"
def is_pangram(sentence):
    sentence = sentence.replace(' ','').lower()
    if len(sentence) < 26: return False
    for ch in arr:
        if ch not in sentence: return False
    return True