arr1 = [
    "It's OK if you don't want to go work for NASA.",
    "1, 2, 3",
    "Ending with ? means a question.",
    "\nDoes this cryogenic chamber make me look fat?\nNo.",
    "         hmmmmmmm...",
    "This is a statement ending with whitespace      ",
    "Tom-ay-to, tom-aaaah-to.",
    "Hi there!",
]
arr2 = [
    "WATCH OUT!",
    "FCECDFCAAB",
    "1, 2, 3 GO!",
    "ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!",
    "I HATE THE DENTIST",
]
arr3 = [
    "Does this cryogenic chamber make me look fat?",
    "You are, what, like 15?",
    "fffbbcbeab?",
    "4?",
    ":) ?",
    "Wait! Hang on. Are you going to be OK?",
    "Okay if like my  spacebar  quite a bit?   ",
]
arr4 = [
    "",
    "          ",
    "\t\t\t\t\t\t\t\t\t\t",
    "\n\r \t",
]
arr5 = [
    "WHAT'S GOING ON?",    
]
def response(hey_bob):
    if hey_bob in arr1: return "Whatever."
    if hey_bob in arr2: return "Whoa, chill out!"
    if hey_bob in arr3: return "Sure."
    if hey_bob in arr4: return "Fine. Be that way!"
    if hey_bob in arr5: return "Calm down, I know what I'm doing!"
