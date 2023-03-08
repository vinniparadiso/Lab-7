#Bethany Berlage and Vinni Paradiso and Olivia Busk

def letter_o(word):
    total=0
    for letter in word:
        if letter=="o":
            total=total+1

    return total
    

print(letter_o("bonobos"))
