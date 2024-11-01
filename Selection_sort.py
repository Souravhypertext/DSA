my_array = list(map(int,input("Enter the list you want to sort : ").split()))

n = len(my_array)
for i in range(n):
    min_index = i
    for j in range(i+1,n):
        if my_array[j] < my_array[min_index]:
            min_index = j

    my_array[i] , my_array[min_index] = my_array[min_index] , my_array[i]

print("Sorted Array : ", my_array)