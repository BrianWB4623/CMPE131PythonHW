def merge_list(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both inputs must be lists.")
    mergeList=[]
    for item in list1:
        if not isinstance(item, int):
            raise TypeError("Both lists must contain only integers.")
        mergeList.append(item)
    for item in list2:
        if not isinstance(item, int):
            raise TypeError("Both lists must contain only integers.")
        mergeList.append(item)
    for i in range(len(mergeList)-1):
        for j in range(i+1,len(mergeList)):
            if(mergeList[j]<mergeList[i]):
                temp=mergeList[i]
                mergeList[i]=mergeList[j]
                mergeList[j]=temp
    return mergeList