def get_optionIdList(QueryDictValues):
    QueryDictValues.pop(0) #exclude csrf-token
    valueList = QueryDictValues[0][0].split(':')
    categoryId = valueList[0] #get category id from radio button value
    #get list of option id
    optionIdList = []
    for item in QueryDictValues:
        item = item[0].split(':')
        optionIdList.append(item[1])
    
    return categoryId, optionIdList