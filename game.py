"""
2048 game file
Author: Joe Ryan
"""

def merge(line):
    """ 
    merge cells in line and return a new list of same size
    """
    if len(line) <=1:
        return list(line)
    else:
        merge_list = []
        for tile in line:
            if tile != 0:
                merge_list.append(tile)
        for i in range(0,len(merge_list)-1):
            if merge_list[i] == merge_list[i+1]:
                merge_list[i] = merge_list[i]*2
                merge_list[i+1] = 0
        for item in merge_list:
            if item == 0:
                merge_list.remove(item)
        for i in range(len(merge_list), len(line)):
            merge_list.append(0)
 
        return merge_list