Word = input("enter your word: ")
def est_palindrome(chaine):

    chaine = chaine.lower()

    chaine = chaine.replace(" ", "")

    return chaine == chaine[::-1]


print(est_palindrome(Word))  
