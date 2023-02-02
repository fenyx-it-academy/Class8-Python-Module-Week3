def shared_letters(w1, w2):
    set1 = set(w1)
    set2 = set(w2)
    shared = set1 & set2    # intersection
    unique1 = set1 - set2   # difference
    unique2 = set2 - set1   # difference
    return [''.join(sorted(shared)), ''.join(sorted(unique1)), ''.join(sorted(unique2))]

print(shared_letters("strong", "strength")) 