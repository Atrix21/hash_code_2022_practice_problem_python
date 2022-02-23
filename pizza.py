from collections import Counter

like_ing = []
dislike_ing = []
elements = []
with open("input_data/e_elaborate.in.txt", "rt") as f:
    for line in f:
        elements.append(line.rstrip('\n'))
elements.pop(0)
list_like = elements[0::2]
list_dislike = elements[1::2]


def f1(l1, l2):
    for item in l1:
        for word in item.split():
            if word.isalnum():
                l2.append(word)


def f2(l1, l2):
    for item in l1:
        for word in item.split():
            if word.isnumeric():
                l2.remove(word)


f1(list_like, like_ing)
f2(list_like, like_ing)
f1(list_dislike, dislike_ing)
f2(list_dislike, dislike_ing)

dict_1 = Counter(like_ing)
dict_2 = Counter(dislike_ing)
like_ing = list(set(like_ing))
dislike_ing = list(set(dislike_ing))
for i in dict_1:
    for j in dict_2:
        if i == j:
            if dict_1[i] >= dict_2[j]:
                dislike_ing.remove(i)
            elif dict_1[i] < dict_2[j]:
                like_ing.remove(i)
n = len(like_ing)
like_ing.insert(0, n)
for i in like_ing:
    print(i, end=' ')
f.close()
