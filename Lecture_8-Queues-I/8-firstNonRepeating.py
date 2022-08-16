"""
https://www.geeksforgeeks.org/find-first-non-repeating-character-stream-characters/
"""

MAX_CHAR = 26 #Assume only lowercase letters
"""
Simple solution using doubly linked list:
Declare a dll of size 256 and a repeated bool array of same size
Then while iterating through the stream, if char is not in repeated array, add it to dll if not in dll
else if it is in dll then remove from dll and add to repeated
Char from front of dll is non repeated char at any point in the iteration
"""
def findFirstNonRepeating(stream):

    # inDLL[x] contains pointer to a DLL node if x is present
    # in DLL. If x is not present, then inDLL[x] is NULL
    inDLL = [] * MAX_CHAR

    # repeated[x] is true if x is repeated two or more times.
    # If x is not seen so far or x is seen only once. then
    # repeated[x] is false
    repeated = [False] * MAX_CHAR

    # Let us consider following stream and see the process
    for i in range(len(stream)):
        x = stream[i]
        print ("Reading " + x + " from stream")

        # We process this character only if it has not occurred
        # or occurred only once. repeated[x] is true if x is
        # repeated twice or more.s
        if not repeated[ord(x) - ord('a')]:

            # If the character is not in DLL, then add this
            # at the end of DLL
            if not x in inDLL:
                inDLL.append(x)
            else:
                inDLL.remove(x)
                repeated[ord(x) - ord('a')] = True

        if len(inDLL) != 0:
            print ("First non-repeating character so far is ")
            print (str(inDLL[0]))

# Driver program
stream = "geekforgeekandgeeksandquizfor"
findFirstNonRepeating(stream)
print("-------------------------------------------")
"""
Alternate simple solution using queues
"""
from queue import Queue
def firstnonrepeating(Str):
    global MAX_CHAR
    q = Queue()
    charCount = [0] * MAX_CHAR

    # traverse whole Stream
    for i in range(len(Str)):

        # push each character in queue
        q.put(Str[i])

        # increment the frequency count
        charCount[ord(Str[i]) -
                  ord('a')] += 1 #We do this to ensure that ord falls within 26

        # check for the non pepeating
        # character
        while (not q.empty()):
            if (charCount[ord(q.queue[0]) -
                          ord('a')] > 1):
                q.get()
            else:
                print(q.queue[0], end = " ")
                break

        if (q.empty()):
            print(-1, end = " ")
    print()

Str = "aabc"
firstnonrepeating(Str)
