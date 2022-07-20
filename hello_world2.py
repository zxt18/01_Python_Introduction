#all the even number

begin = 4
end = 15

data = [item for item in range(begin,end) if item % 2 == 0]
#print(f"begin = {begin}, end = {end}, even numbers : ", data)


#removeelementsfromlist\

lista = [3,5,7,9,11,13]
listb = [7,11]

data = [item for item in lista if item not in listb]
#print(f"from {lista} remove {listb}, result : " , data)