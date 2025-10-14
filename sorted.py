def reverse_sort_dictionary(dict1):
    sortedItems=sorted(dict1.items(),reverse=True)
    result=[]
    for name, info in sortedItems:
        phoneNumber=info[0]
        result.append((name,phoneNumber))
    return result
    