def trie(liste):

    if len(liste) <= 1:
        return liste
    
    pivot = liste[-1]
    p = []
    q = []
    for i in range(len(liste) - 1):
        if liste[i] < pivot:  
            p.append(liste[i])
        else:  
            q.append(liste[i])
    return trie(p) + [pivot] + trie(q)

print("Le tableau trié est :", trie([5, 4, 3, 2, 1]))





