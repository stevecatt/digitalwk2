array = [2,1,45,67,89,4,5,7,9]

def bubblesort():
    for i in range(0, len(array)):
        #print(array)
        for j in range(0, len(array)):
        #print(array)
            if array[i] <
             array[j]:
            #print(array)
                r = array[i]
                array[i]= array[j]
                array[j]= r
            #print(array)
    return array

bubblesort()

print(array)