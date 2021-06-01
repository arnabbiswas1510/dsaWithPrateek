"""
Next Greater Element
Given an array, print the Next Greater Element (NGE) for every element. The Next greater Element for an element x is the first greater element on the right side of x in the array. Elements for which no greater element exist, consider next greater element as -1.

Examples:

For an array, the rightmost element always has the next greater element as -1. For an array which is sorted in decreasing order, all elements have next greater element as -1. For the input array [4, 5, 2, 25}, the next greater elements for each element are as follows.

Element NGE 4 --> 5 5 --> 25 2 --> 25 25 --> -1

d) For the input array [13, 7, 6, 12}, the next greater elements for each element are as follows.

Element NGE 13 --> -1 7 --> 12 6 --> 12 12 --> -1
"""
def printNGE(arr):
    st=[]
    st.append(arr[0])
    #The trick in this problem is to print NFE only off the stack elements
    for i in range(1,len(arr)):
        while st and arr[i] > st[-1]: #Keep popping off stack as long as arr is greater
            print(str(st.pop()) + " -> " + str(arr[i]))
        st.append(arr[i]) #push arr to stack
    while st: #Everything else in stack has no NGE hence print -1
        print(str(st.pop()) + " -> -1") #TIP: You can print in order by storing indexes instead of Array elements in stack

printNGE([4, 5, 2, 25])