# Repeatedly find minimum and palce it in
# TC is o(n^2) cus both loop iterates over same array. SC is o(1)
# def task(array):
#     n=len(array)
#     for i in range(0,n):
#         min_index = i 
#         for j in range(i+1,n):
#             if array[j]<array[min_index]:
#                 min_index = j
#         array[i], array[min_index] = array[min_index], array[i]


# array = [2,9,6,5,4,8,7,1]
# task(array)
# print(array)





array = [12,100,90,34,1,67,89]
def task(array):
    n = len(array)
    for i in range(0,n):
            min_ind = i
            for j in range(i+1,n):          
                 if array[j]<array[min_ind]:
                      min_ind = j
            array[i],array[min_ind] = array[min_ind],array[i]


task(array)
print(array)



    
