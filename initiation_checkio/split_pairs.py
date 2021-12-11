def split_pairs(a):
    lst = []
    if len(a) % 2 == 0:
        for i in range(0, len(a) - 1, 2):
            lst.append(a[i] + a[i + 1])
    else:
        a += '_'
        if len(a) % 2 == 0:
            for i in range(0, len(a) - 1, 2):
                lst.append(a[i] + a[i + 1])
    return lst