#yuandemianji


import math
import numbers
from unittest import result

def compute_area_of_circle(r):
    return round(math.pi * r**2, 2)

# print(compute_area_of_circle(2))
# print(compute_area_of_circle(3.14))
# print(compute_area_of_circle(1))

#ngeshuzidepingfanghe (e.g. 1^2+2^2+3^2+...)


def sum_of_square(n) :
    result = 0
    for number in range(1,n+1) : 
        result += number * number
    return result



#print(f"Sum of squares of 3 is : {sum_of_square(3)}")
#print(sum_of_square(5))
#print(sum_of_square(10))


#all the even number

def get_even_number(begin,end):
    result = []
    for item in range(begin,end) : 
        if item % 2 == 0 : 
            result.append(item)
    return result

begin = 4
end = 15
#print(f"begin={begin},end={end},even numbers:",get_even_number(begin,end))


#removeelementsfromlist\

def remove_element_from_list(lista,listb) : 
    for item in listb : 
        lista.remove(item)
    return lista
    
lista = [3,5,7,9,11,13]
listb = [7,11]
#print(f"from {lista} remove {listb}, result : {remove_element_from_list(lista,listb)}")


#norepeating

def get_the_uniq_list(lista) :
    result = []
    for item in lista : 
        if item not in result :
            result.append(item)
    return result

lista = [10,20,30,10,20]
# print(f"souce list{lista}, uniq list : " , get_the_uniq_list(lista))


#so wuliao 
# Find the largest element of a list.

list_a = [2,5,1,2,6,8,33,123,72134,123,3163,242341,12312,1212,4634,1212,63463,99,99999, 999999999999]

def get_largest_elem(list_a) : 
    result = list_a[0]
    for item in list_a : 
        if item > result : 
            result = item
    return result

#print(f"the largest element of list is", get_largest_elem(list_a))


#sum of cubes

#Create a function def sum_of_cubes(lista) : 
#Return : sum_of_cubes

#Print : Sum of cubes of lista {} is {}


lista = [1,2,3,4,5,11,13]

def sum_of_cubes(lista) : 
    result = 0 
    for number in lista :
        result += number * number * number
    return result

#print(f"sum of cubes of lista {lista} is : {sum_of_cubes(lista)}")


"""
Return the sum of cubes of even numbers only

list_a = [1,2,3,4,5,6,7,8]

ans = 2^3 + 4^3 + 6^3 + 8^3
"""

list_a = [1,2,3,5,6,7,8] 

begin = 1 
end = 8

def even_n_only(list_a) : 
    result = []
    for item in range(list_a) :
        if item % 2 == 0 : 
            result.append(item)
    return result
print(even_n_only(begin,end))

def the_sum_of_cubes_of_even_numbers_only(list_a) : 
    outcome = 0 
    for number in list_a : 
        outcome += number **3 
    return outcome

print(f"the sum of cubes in {list_a} of even numbers is : {the_sum_of_cubes_of_even_numbers_only(even_n_only(begin,end))} ")








