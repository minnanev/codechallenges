def unique_names(names1, names2):

    # insert the list to the set
    list_set = set(names1+names2)
    # convert the set to the list
    unique_list = (list(list_set))
    for x in unique_list:
        print(x)


names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
unique_names(names1, names2)
