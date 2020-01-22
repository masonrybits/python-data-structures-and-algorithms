def left_join(map1,map2):
    output = []
    '''for every key in map1, looks for it in map2'''
    for key in map1:
        '''if key in map2, append the value of that key to output in a list format.if the key in map1 is not present in map2, append the value of None to output'''
        if key in map2:
            output.append([key,map1[key],map2[key]])
        else:
            output.append([key,map1[key],None])
    return output
