""""
TASK
You are given a list that consists of the numbers 1...n. A pair of indices (i,j) is an inversion if i<j and the element at index i on the list is greater than the element at index j.

You may assume that n is at most 100.

In a file inversions.py, implement a function count that returns the total number of inversions in the list.


EXPLANATION : 
The list [4,3,2,1] contains the inversions -
(0, 1) because 4 > 3
(0, 2) because 4 > 2
(0, 3) because 4 > 1
(1, 2) because 3 > 2
(1, 3) because 3 > 1
(2, 3) because 2 > 1
"""


def count(t):
    # element 'n1' at lower index 'i' > element 'n2' at higher index 'j'
    # count all index pairs that fulfill the condition
    pairs = 0
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            if t[i] > t[j]:
                pairs += 1

    return pairs


if __name__ == "__main__":
    print(count([1,3,2])) # 1
    print(count([1])) # 0
    print(count([4,3,2,1])) # 6
    print(count([1,8,2,7,3,6,4,5])) # 12