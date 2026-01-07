# HASHING IN PYTHON
# n and m can have 10^8 elements
#  1<= n[i] <=10


# BRUTE FORCE METHOD
n = [1,5,8,9,10,1,7,2,5,5,7]
m = [10,111,1,9,5,67,2]
dct = dict()
'''   SAME FOR FUNCTION
for i in range(0, len(m)):
    count = 0
    for x in range(0, len(n)):
        if n[x] == m[i]:
            count += 1
    print(count)
'''

for num in m:
    count = 0
    for x in n:
        if x == num:
            count += 1

    print(num," : ",count)
