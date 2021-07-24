"""
Problem: https://www.learnbay.io/minimum-window-containing-all-words/
Approach: two-pointer
"""

def getHash(pattern):
    mapp = {}
    for item in pattern:
        mapp[item]=0
    return mapp

def getMinWindowHavingAllWords(text,pattern):
    pattern = pattern.split()
    text = text.split()
    mapp = getHash(pattern)
    left,right,res = 0,0,float('inf')
    while left<len(text) and right<len(text):
        while sum(mapp.values())<len(mapp):
            if right<len(text):
                item = text[right]
                if item in mapp:
                    mapp[item]+=1
                right+=1
            else:
                break
        while sum(mapp.values())>=len(mapp):
            res = min(res,right-left)
            if text[left] in mapp:
                mapp[text[left]]-=1
            left+=1
    return res

text = "Shopping with xyz.com is an awesome experience"
pattern = "awesome with xyz.com"
print(getMinWindowHavingAllWords(text,pattern))

print('')

text1 = "keep in mind that these are the minimum requirements"
pattern1 = "these minimum"
print(print(getMinWindowHavingAllWords(text1,pattern1)))