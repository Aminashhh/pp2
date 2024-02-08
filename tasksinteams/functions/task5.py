def find_common_elements(list1, list2):
    newlist = []
    for i in list1:
        if i in list2:
            newlist.append(i)
    print(newlist)

list1 = [12,13,14,15]
list2 = [12,13,16,17]
find_common_elements(list1,list2)
    