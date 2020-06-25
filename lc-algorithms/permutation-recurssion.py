import copy
def permute(l):
    perm = []
    if len(l) == 0:
        perm.append([])
    else:
        first_element = l[0]
        after_first = slice(1,None)
        print(l[after_first])
        sub_permutes = permute(l[after_first])
        print(len(sub_permutes))
        for p in sub_permutes:
            for j in range(0, len(p) + 1):
                r = copy.deepcopy(p)
                r.insert(j, first_element)
                print(r)
                perm.append(r)
        
    return perm

if __name__ == '__main__':
    l = ['a','b','c']
    print(permute(l))
