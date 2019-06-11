def encoder(l, alph, k):
    res = ''
    if alph.index(l)+k >= len(alph):
        res += alph[k - (len(alph)-alph.index(l))]
    else:
        res += alph[alph.index(l)+k]
    return res

def decoder(l, alph, k):
    res = ''
    if alph.index(l)-k < 0:
        res += alph[len(alph)-(k - alph.index(l))]
    else:
        res += alph[alph.index(l)-k]
    return res
