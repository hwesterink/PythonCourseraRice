"""
sort a list calling the sort_merge function
"""
count_sort = 0
count_merge = 0
lists_dict = { 1: [5], 2: [6,3], 4: [8,2,5,3], 8: [3,1,8,3,5,2,6,9],
               16: [9,8,7,6,5,4,3,2,1,0,9,8,7,6,5,4] }

def merge(list1, list2):
    global count_merge
    count_merge += 1
    result = []
    #print list1, list2
    while len(list1)>0 and len(list2)>0:
        if list1[0] > list2[0]:
            result.append(list2[0])
            list2 = list2[1:]
        else:
            result.append(list1[0])
            list1 = list1[1:]
    #print result
    if len(list1) == 0:
        result += list2
    else:
        result += list1
    #print result
    return result

def sort_merge(to_sort):
    global count_sort
    count_sort += 1
    length = len(to_sort)
    if length == 0 or length == 1:
        return to_sort
    else:
        return merge(sort_merge(to_sort[0:length/2]), sort_merge(to_sort[length/2:]))


count1 = count_sort + count_merge
print lists_dict[1]
print sort_merge(lists_dict[1])
print count_sort, count_merge
count1 = count_sort + count_merge
print count1
print
count_sort = 0
count_merge = 0
print lists_dict[2]
print sort_merge(lists_dict[2])
print count_sort, count_merge
count2 = count_sort + count_merge
print count2, 2*count1+2
print
count_sort = 0
count_merge = 0
print lists_dict[4]
print sort_merge(lists_dict[4])
print count_sort, count_merge
count4 = count_sort + count_merge
print count4, 2*count2+2
print
count_sort = 0
count_merge = 0
print lists_dict[8]
print sort_merge(lists_dict[8])
print count_sort, count_merge
count8 = count_sort + count_merge
print count8, 2*count4+2
print
count_sort = 0
count_merge = 0
print lists_dict[16]
print sort_merge(lists_dict[16])
print count_sort, count_merge
count16 = count_sort + count_merge
print count16, 2*count8+2

