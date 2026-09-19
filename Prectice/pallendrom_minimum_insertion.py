# A Naive recursive program to find minimum
# number insertions needed to make a string
# palindrome
import sys
import time

# Recursive function to find minimum
# number of insertions
def findMinInsertions(text, l, h):
    # Base Cases
    if l > h:
        return 0
    if (l == h):
        return 0
    if (l == h - 1):
        return 0 if (text[l] == text[h]) else 1
    if (text[l] == text[h]):
        return findMinInsertions(text, l + 1, h - 1)
    else:
        return min(
            findMinInsertions(text, l, h - 1),
            findMinInsertions(text, l + 1, h),
        ) + 1
        #return (min(findMinInsertions(str, l, h - 1), findMinInsertions(str[::-1], l , h-1)) + 1)


# Driver Code
if __name__ == "__main__":
    #str = "geekdfs"
    text = "dababff"
    print(findMinInsertions(text, 0, len(text) - 1))
    #print(couner(11))

# This code is contributed by ita_c


