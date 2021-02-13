def remove_duplicate(array):
    """:cvar
        Feature without lossing memory"""
    index =0;
    for i in range(len(array)-1):
        if  array[i] != array[i+1]:
            array[index] = array[i]
            index = index + 1
    return index
import numpy as np
count = index = 0

while(index != 9):
    array = np.random.randint(low = 1, high = 10,size= 20)
    array.sort() #this returns None Hotas
    index = remove_duplicate(array)
    count = count +1
print(array[:index],count)