
s = "abddyyzzzxxyyaabb"
q = ["a","b","d","c"]

hash_list = [0]*27

#for hash list
for ch in s:
    ascii_val = ord(ch)
    index = ascii_val - 97
    hash_list[index] += 1

#for computation
for j in q:
    ascii_val = ord(j)
    index = ascii_val - 97
    print(j, hash_list[index])