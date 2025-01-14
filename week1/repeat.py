"""
TASK
Find out how long is the shortest string that forms the given string when repeated. For example, when the input string is abcabcabcabc, the shortest repeating string is abc.

The string consists of the characters a-z and contains at most 100 characters.

Implement a function find that returns the length of the shortest repeating string.
"""


def find(s:str) -> int:
# PSEUDO 
    # iterate through string
    # build a substring based on current iteration
    # verify if substring can repeat to form complete string and return substring length
    # else return search string length

    n = len(s) 
    for i in range(1, n + 1):
        if n % i == 0 : # substring can only exist evenly within the string
            substring = s[: i]
            print('substring :', substring)
            if substring * (n // i) == s :
                print('repetition :', substring * (n // i))
                return len(substring)
    return n


if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7 edge-case
    print(find("abcabca")) # 7  edge-case
