# STORING REPITITIONS IN A DICTIONARY

nums = [1,2,5,9,111,845,5,5,2,845]
freq = dict()
for i in range(0,len(nums)):
    if nums[i] in freq:
        freq[nums[i]] += 1

    else:
        freq[nums[i]] = 1

print(freq)
print(freq[5])



