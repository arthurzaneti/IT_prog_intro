#1) 
def merge(l1, l2):
    i1 = 0
    i2 = 0
    l = []
    while(i1 < len(l1) and i2 < len(l2)):
        # Aqui o pior caso é quando as duas listas acabam ao mesmo tempo, dai o loop while ocorreria praticamente
        # len(l1) + len(l2) vezes. De resto as operações são menos custosas, portanto o algoritmo é O(len(l1) + len(l2))

        # Tomei a opção (arbitrária) de manter dúplicas
        if(l1[i1] > l2[i2]):
            l.append(l1[i1])
            i1 += 1
        else:
            l.append(l2[i2])
            i2 += 1

    return(l + l1[i1:len(l1)] + l2[i2:len(l2)])


#_______________________________________________________________________________

#2) 
# A "memória" do comprador se assemelha a uma fila
# A variável N é completamente inútil em Python, mesmo assim a inseri como parâmetro devido a especificação do exercício
def items_to_buy(N, K, l):
    memory = []
    i = 0
    item_counter = 0
    while(i < N):
        if not(l[i] in memory):
            if K != 0:
                if len(memory) == K:
                    memory.pop(0)    
                memory.append(l[i])
            item_counter += 1
        i += 1
    
    return(item_counter)

print(items_to_buy(5,0,[1,1,1,1,1]))
#3)

def is_parenteses_valid(s):
    count = 0
    for char in s:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        if count < 0:
            return(False)
    return(count == 0)
"""
print(is_parenteses_valid("(((((((()))"))
print(is_parenteses_valid("()()()(()())"))
print(is_parenteses_valid("[[[]]]"))
"""

