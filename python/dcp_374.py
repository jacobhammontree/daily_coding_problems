"""
Given a sorted array arr of distinct integers, return the lowest index i for which arr[i] == i. Return null if there is no such index.

For example, given the array [-5, -3, 2, 3], return 2 since arr[2] == 2. Even though arr[3] == 3, we return 2 since it's the lowest index.
"""


def minEqualIndexValue(L):
    count = -1
    for num in L:
        count+=1
        if(num == count):
            return count
    return -1

print(minEqualIndexValue([-5,-3,4,6]))