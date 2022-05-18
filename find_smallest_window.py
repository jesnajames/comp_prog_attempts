"""
#URL : https://practice.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1/?page=1&difficulty[]=1&company[]=Google&category[]=Hash&category[]=Map&sortBy=submissions
Given two strings S and P. Find the smallest window in the string S consisting of all the characters(including duplicates) of the string P.  
Return "-1" in case there is no such window present. In case there are multiple such windows of same length, 
return the one with the least starting index. 

Example: 
"""
from copy import deepcopy


def get_windows(s: str, p: str):
    substrings = []
    for lptr in range(len(s)):
        p_copy = deepcopy(p)
        if s[lptr] in p_copy:
            p_copy = p_copy.replace(s[lptr], "")
            for rptr in range(lptr+1, len(s)):
                if s[rptr] in p_copy:
                    p_copy = p_copy.replace(s[rptr], "")
                    if not p_copy:
                        substrings.append(s[lptr:rptr+1])
                        break
    return substrings


def get_smallest_window(s: str, p: str):
    substrings = []
    for lptr in range(len(s)):
        p_copy = deepcopy(p)
        if s[lptr] in p_copy:
            p_copy = p_copy.replace(s[lptr], "")
            for rptr in range(lptr + 1, len(s)):
                if s[rptr] in p_copy:
                    p_copy = p_copy.replace(s[rptr], "")
                    if not p_copy:
                        substrings.append(s[lptr:rptr + 1])
                        break
    if not substrings:
        return -1
    min_len = len(substrings[0])
    smallest_window = substrings[0]
    for i in range(1, len(substrings)):
        if len(substrings[i]) < min_len:
            min_len = len(substrings[i])
            smallest_window = substrings[i]
    return smallest_window

 
print(get_smallest_window("timetopractise", "toc"))  # toprac

print(get_smallest_window("zoomlazapzo", "oza"))  # apzo
