# OPTIMAL SOLUTION FOR CODE NUMBER 7
# CREATING HASH MAPS, 
# HASH MAPS INITIALLY STORE 0 IN IT AND CHANGES ACCORDINGLY TO MAKE SOLUTION OPTIMAL AND EFFICIENT.
# h_map = [0]*11, creates 11 indexes having o in them, index value is 0 to 10,


n = [1, 2 , 7 , 8 , 10 , 5 , 2 , 5 , 7 , 3 , 5 , 10]
m = [5 , 111 , 204 , 4 , 6 , 1 , 2]
hash_list = [0]*11

for num in n:
    hash_list[num] += 1
for num in m:
    if num<1 or num>10:
        print(num," : ",0)
    else:
        print(num, " : ", hash_list[num])
