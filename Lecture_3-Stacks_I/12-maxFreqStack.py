"""
Maximum Frequency Stack
Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

1. push(int x), which pushes an integer x onto the stack.
2. pop(), which removes and returns the most frequent element in the stack.

If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.
"""

class MaxFreqStack:
    def __init__(self): #Again, just remember the variables here
        self.freq= {}
        self.buckets= {}
        self.maxFreq= float('-inf')

    def push(self, val):
        if val in self.freq: #First add val to frequency map
            self.freq[val] = self.freq[val]+1
        else:
            self.freq[val] = 1

        currFreq = self.freq[val]
        if currFreq in self.buckets: #Then add val to currFreq bucket
            self.buckets[currFreq].append(val)
        else:
            self.buckets[currFreq]=[val]

        self.maxFreq=max(self.maxFreq, currFreq) #Adjust maxFreq

    def pop(self):
        if self.maxFreq < 0:
            print("Stack underflow")
            return
        val = self.buckets[self.maxFreq].pop() #Obtain the val from freqBucket
        self.freq[val] -= 1 #Decrement freq of val
        if len(self.buckets[self.maxFreq]) == 0: #Decrement maxFreq only if bucket is empty
            self.maxFreq -= 1
        return val

    def display(self):
        print('maxFreq:'+str(self.maxFreq))
        print('freq:'+str(self.freq))
        print('freqBuckets:'+str(self.buckets))

st=MaxFreqStack()
st.push(1)
st.push(1)
st.push(3)
st.pop()
st.push(5)
st.push(5)
st.push(5)
st.pop()
st.pop()
st.display()