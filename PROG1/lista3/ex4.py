ALFABET = "abcdefghijklmnopqrstuvwxyz"
def prev_letter(c):
    index = ALFABET.find(c)
    if index == 0:
        return(ALFABET[-1])
    else:
        return(ALFABET[index - 1])

def esconder(s):
    encoded_s = ""
    for z in s:
        if z in ALFABET:
            encoded_s += prev_letter(z)
        else:
            encoded_s += z
    return(encoded_s)

print(esconder("1111111111''''''''''abc~`qá"))
print(esconder("Ola! Que tal ir ao IMPA Tech?"))