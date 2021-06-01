"""
N Stacks
Implement N stacks in a single array

https://www.youtube.com/watch?v=S5cYO9k1Ja8&t=375s

"""

class NStacks:
    def __init__(self, num, capacity):
        self.arr=[None]*capacity #Remember the following 4 variables, arr stores the data for all stacks
        self.top=[-1]*num #Top of each stack
        self.next=[i for i in range(1,capacity)] #Stores the next index to be pushed to and also prev after the push
        self.next.append(-1)
        self.free=0 #Next free slot in arr

    def push(self, st, val):
        if st <0 or st>len(self.top):
            print("Invalid stack")
            return
        curr=self.free
        self.arr[curr]=val #First assign the value
        self.free=self.next[self.free] #set free to the next index
        self.next[curr]=self.top[st] #set prev to next
        self.top[st]=curr #set top to curr

    def pop(self,st):
        if st <0 or st>len(self.top):
            print("Invalid stack")
            return
        curr = self.top[st] #Index of item to be returned
        self.top[st]=self.next[curr] #set top to prev index
        self.next[curr]=self.free #Set next to next free
        self.free=curr #Set free to currently popped slot
        return self.arr[curr]

    def display(self):
        print(self.arr)

st=NStacks(5,15)
st.push(0,1)
st.push(0,2)
st.push(0,3)
st.pop(0)
st.push(2,4)
st.display()
