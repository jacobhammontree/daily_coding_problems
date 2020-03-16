"""
This problem was asked by Facebook.

Given a list of integers L, find the maximum length of a sequence of consecutive numbers that can be formed using elements from L.

For example, given L = [5, 2, 99, 3, 4, 1, 100], return 5 as we can build a sequence [1, 2, 3, 4, 5] which has length 5.
"""
from collections import  defaultdict
print("hello")

# This function is O(n log n) in average, O(n^2) worst case
def maxSequence(L):
    f = {}
    max_conseq = 0
    curr_conseq = 0
    l_sorted = sorted(L)
    last = None
    for i in l_sorted:
        if(curr_conseq == 0 and not(last)):
            curr_conseq +=1
        elif(i == (last+1)):
            curr_conseq += 1
        else:
            if(curr_conseq > max_conseq):
                max_conseq = curr_conseq
            curr_conseq = 1
        
        last = i
    return max_conseq

# This will try to be linear in time O(n)
def maxSequenceFaster(L):
    seqMap = defaultdict(int)
    for num in L:
        if(num-1 in seqMap):
            seqMap[num-1] += 1
        if (num+1 in seqMap):
            seqMap[num+1] += 1
        seqMap[num] = max(seqMap[num+1], seqMap[num-1])

    print(seqMap)

    return max(seqMap.values())

L = [62,5,2,99,61,63,3,4,1,100,56,57,58,59,60]
print(maxSequence(L))
print(maxSequenceFaster(L))