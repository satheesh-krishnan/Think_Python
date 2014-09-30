import random
def sortbylength(words):
    t = []
    for word in words:
       t.append((len(word), word))

    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res
s='kgjh jdfn jngd jndg kkm kmfd'
l=s.split(" ")


d=sortbylength(l)
print d

