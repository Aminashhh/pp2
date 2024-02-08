def find_common_elements(list1, list2):
    newlist = []
    for i in list1:
        if i in list2:
            newlist.append(i)
    print(newlist)

list1_input = input(" ")
list2_input = input(" ")
list1 = [int(x) for x in list1_input.split()]
list2 = [int(x) for x in list2_input.split()]
find_common_elements(list1,list2)
    