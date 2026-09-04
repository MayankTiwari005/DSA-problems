def Shorten_Word(words):
    return len(words) <= 5
word = ["abcd", "subaru", "gmc", "fiat"]
res = filter(Shorten_Word, word)
print(list(res))


text = ["subaru", "mazda", "seat", "volkswagen", "toyota"]
res = filter(lambda x: len(x)<=5, text)
print(list(res))

numbers = [1,2,3,4,5,6,7,8,9]
result = filter(lambda x: x%2 == 0, numbers)
print(list(result))

names = ["a", "b", "", "", "c", "d"]
final = filter(None, names)
print(list(final))

final2 = (x for x in numbers if x%2==0)
print(final2)