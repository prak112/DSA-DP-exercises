"""
TASK :
A gummy candy costs X euros and a chocolate candy costs Y euros. What is the maximum number of candies you can buy if you have Z euros?

You may assume that X, Y and Z are integers in the range 1, ... 100.

In a file candies.py, implement the function count that returns the maximum number of candies.
"""

import math

def count(x:int, y:int, z:int) -> int:
    x = math.floor(x)
    y = math.floor(y)
    z = math.floor(z)
    return max(z // x, z // y) # IDEAL solution : z // min(x, y)


if __name__ == "__main__":
    print(count(3, 4, 11)) # 3
    print(count(5, 1, 100)) # 100
    print(count(2, 3, 1)) # 0
    print(count(2, 3, 9)) # 4