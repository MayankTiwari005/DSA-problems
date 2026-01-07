def selection_sort(num):
    n = len(num)
    for i in range(0 , n):
        min_index = i
        for j in range(i + 1, n):
            if num[j] < num[min_index]:
                min_index = j
        num[i], num[min_index] = num[min_index], num[i]
    return num

n = [5,7,8,4,1,6,9,2]
print(selection_sort(n))