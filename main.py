def longestCommonPrefix(strs):
    #Want to intialize a large number in case the strings in strs are long. 
    min_len_string = 100 

    #initizlize empty string
    sub_str = ""
    
    #If there are not strings in strs then return "Empty List"
    if len(strs) == 0:
        raise IndexError

    #find the shortest length string in strs
    for s in strs:
        min_len_string = min(min_len_string, len(s))

    for char in range(min_len_string):
        for j in range(len(strs)):
            """
            To save computation we only want to search the length of the shortest string
            Doest matter what strs enter we search, so we loop strs[0][i]
            f == f
            fl == fl
            flo != fli 
            return sub_str
            """
            if strs[j][char] != strs[0][char]:
                return sub_str
        #Add to sub_string
        sub_str += strs[0][char]

