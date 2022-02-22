from collections import Counter

like_ing = []
dislike_ing = []
elements = []
with open("file.txt", "rt") as f:
    for line in f:
        elements.append(line.rstrip('\n'))
elements.pop(0)
list_like = elements[0::2]
list_dislike = elements[1::2]
for i in list_like:
    for word in i.split():
        if word.isalnum():
            like_ing.append(word)
for i in list_like:
    for word in i.split():
        if word.isnumeric():
            like_ing.remove(word)
for i in list_dislike:
    for word in i.split():
        if word.isalnum():
            dislike_ing.append(word)
for i in list_dislike:
    for word in i.split():
        if word.isnumeric():
            dislike_ing.remove(word)

dict_1 = Counter(like_ing)
dict_2 = Counter(dislike_ing)
like_ing = list(set(like_ing))
dislike_ing = list(set(dislike_ing))
for i in dict_1:
    for j in dict_2:
        if i == j:
            if dict_1[i] > dict_2[j]:
                dislike_ing.remove(i)
            elif dict_1[i] < dict_2[j]:
                like_ing.remove(i)
            elif dict_1[i] == dict_2[j]:
                continue
for i in like_ing:
    for j in dislike_ing:
        if i == j:
            like_ing.remove(i)
n = len(like_ing)
like_ing.insert(0, n)
for i in like_ing:
    print(i, end=' ')
f.close()