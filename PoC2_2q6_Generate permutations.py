"""
Generating permutations using recursion
"""
outcomes_dict = { 0:(), 1:(3), 2:(1,2), 3:(1,2,3), 4:(1,2,3,4), 5:(1,2,3,4,5), 6:(1,2,3,4,5,6) }


def permutations(outcomes):

    try:
        length = len(outcomes)
    except:
        outcomes_as_set = set()
        outcomes_as_set.add(outcomes)
        return outcomes_as_set
    
    if length == 0:
        return set([])
    else:
        rest_permutations = permutations(outcomes[1:])
        new_perms = set()
        if len(rest_permutations) == 0:
            new_perms.add(outcomes)
        else:
            for perm in rest_permutations:
                list_perm = list(perm)
                len_list = len(list_perm)
                for index in range(len_list+1):
                    list_perm = list(perm)
                    list_perm.insert(index, outcomes[0])
                    tuple_perm = tuple(list_perm)
                    new_perms.add(tuple_perm)
        return new_perms

for index in range(7):    
    if index == 0:
        print index, len(permutations(outcomes_dict[index]))+1, 1
    else:        
        p_n_min_1 = len(permutations(outcomes_dict[index-1]))
        if p_n_min_1 == 0:
            p_n_min_1 += 1
        print index, len(permutations(outcomes_dict[index])), index * p_n_min_1
