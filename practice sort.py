
def bubble(num):
    n = len(num)
    for i in range(n-2, -1, -1):
        is_swap = False
        for j in range(0, i+1):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
                is_swap= True
            j +=1
        if is_swap == False:
            break
    return num


def selection(arr):
    n = len(arr)
    for i in range(0,n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return n

def insertion(lst):
    n = len(lst)
    for i in range(1,n):
        key = lst[i]
        j = i-1
        while j >= 0 and j > lst[key]:
            lst[j+1] = lst[j] 
            j -=1
        lst[key] = lst[j+1]
    
    return lst

