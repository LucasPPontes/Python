import itertools

letters = ["a","b","c","ç","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@","!","#","$"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]

passwd = ["a"]

wordlist = []

def create_wordlist():

    
    
    with open("wordlist.txt","w") as wordlistfile:
        for line in itertools.product(numbers,repeat=4):
            x = "".join(line)
            wordlist.append(x)
            wordlistfile.write("\n".join(wordlist))

create_wordlist()