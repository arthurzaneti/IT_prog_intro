import math

#_______________________________________________1___________________________________________________
# Algoritmo O(log(n)) que implementa busca binária, algo que podemos fazer porque a lista está ordenada
def search_insert(l, n):
    pos = math.floor(len(l)/2)
    while(True):
        if(l[pos] == n):
            return(pos)
        elif(l[pos] >= n):
            if pos == 0:
                return 0
            if l[pos - 1] < n:
                return(pos) 
            pos -= math.ceil(pos/2)
        else:
            if pos == len(l)-1:
                return(len(l))
            if l[pos + 1] > n:
                return(pos + 1)
            pos += math.ceil(pos/2)
        
#_______________________________________________2___________________________________________________

"""
    Esta é a função mais simples que realiza o que foi pedido. Eu recebo um n inteiro, mas não faz sentido falar sobre as primeiras -5 linhas
do triângulo de Pascal, então se o número for negativo ou zero retorno []. Caso n seja positivo, construo iterativamente as linhas usando que
somando termo a termo linha_i + [0] com [0] + linha_i obtenho a linha_(i+1). Este algoritmo é, a meu ver, O(n^2) em média e também no pior caso.
"""
def triangulo_pascal(n):
    if n <= 0:
        return []
    
    l_atual = [1]
    triangle = [l_atual]
    for i in range(1,n):
        l_aux = l_atual + [0]
        l_atual = [0] + l_atual  
        for j in range(len(l_atual)):
            l_atual[j] += l_aux[j]
        triangle.append(l_atual)
    return(triangle)
            

#________________________________________________________________3_________________________________________________________

# Em geral, algoritmos em listas não ordenadas, em que eu não sei a tail, vão precisar ser O(n) ao mínimo. Dito isso os algoritmos para
#determinar o tamanho da lista e o de remover elementos com um certo valor são O(n), mas eu fiz um método pra guardar a tail e tornar 
#a soma O(1)
class Linked_list:
    def __init__(self, head):
        self.head = head
        self.det_len()
        self.det_tail()
    
    # Complexidade O(n)
    def det_len(self):
        i = 1
        node = self.head
        while(node.next != None):
            i += 1
            node = node.next
        self.len = i
    
    def det_tail(self):
        node = self.head
        while(node.next != None):
            node = node.next
        self.tail = node
    
    def print_list(self):
        node = self.head
        while(node != None):
            print(node.val)
            node = node.next

    # Complexidade O(n)
    def delete_node_with_val(self, val):
        prev = self.head
        node = prev.next
        while(node != None):
            if node.val == val:
                prev.next = node.next
                if node == self.tail:
                    self.tail = prev
            else:
                prev = node
            node = node.next
        return(self)

    # Complexidade O(1) porque estou guardando um ponteiro pra tail
    def __add__(self, Linked_list2):
        self.tail.next = Linked_list2.head
        self.tail = Linked_list2.tail
        return self
        
class List_node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
def create_chained_list(l):
    head = List_node(l[0])
    node = head
    i = 1
    while i < len(l):
        node.next = List_node(l[i])
        node = node.next 
        i += 1
    return(Linked_list(head))

#________________________________________________________________4 e 5________________________________________________________________________

import re

class Polynomial:
    def __init__(self, str_poly):
        dict = {}
        str_poly = str_poly.replace(" ", "")
        str_poly = re.split(r'([+-])', str_poly)
        str_poly = [i for i in str_poly if i !="+"]
        i = 0
        while(i < len(str_poly)):
            sign = 1
            if str_poly[i] == "-":
                i += 1
                sign = -1
            term = str_poly[i].split("x")
            if(len(term) == 1):
                dict[0] = int(term[0]) * sign
            elif(term[0] == ""):
                dict[int(term[1][1:len(term[1])])] = 1 * sign
            else:
                dict[int(term[1][1:len(term[1])])] = int(term[0]) * sign
            i += 1
        self.poly = dict

    
    # A função acabou ficando mais longa do que eu gostaria, provavelmente existem meio melhores de lidar com os edge cases.
    # Ja percebeu que escrevemos o coeficiente do polinômio somente se ele não é 1?!?!?!?!?
    # Ja percebeu que escrevemos o sinal do primeiro coeficiente somente se ele é "-" ?!?!?!?!?

    # Enfim, o exercício pedia para a função que printa o polinômio receber como parâmetro um dicionário, eu fiz assim usando a classe Polynomial,
    #essêncialmente a função que printa o polinômio recebe ainda um dicionário, mas ele agora é um atributo da classe.
    def __str__(self):
        poly_str = ""
        degrees_left = set(self.poly.keys())
        while(degrees_left):
            degree = max(degrees_left)
            degrees_left.remove(degree)
            coef = self.poly[degree]
            if coef > 0 and poly_str != "":
                    if coef == 1 and degree != 0:
                        str_coef = "+"
                    else:
                        str_coef = "+" + str(coef)
            else:
                if coef == 1:
                    str_coef = ""
                else:
                    str_coef = str(coef)

            if degree == 0:
                whole_term = str_coef
            else:
                whole_term = str_coef + "x^" + str(degree)
            
            poly_str += whole_term
        return(poly_str)
    
