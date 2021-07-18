"""
https://leetcode.com/problems/sorting-the-sentence/

eg --> s = "is2 sentence4 This1 a3"

stp1) split --> ['is2', 'sentence4', 'This1', 'a3']
stp2) create dict
stp3) in dict put (key = number ) and ( value = word ) --using-- ( dic[i[-1]] = i[:-1] )
stp4) sort the dict keys ---> from [2,4,1,3] to [1,2,3,4]
stp5) insert all the sorted key's values accordingly into the new list
stp6) join that new list ---> ['This', 'is', 'a', 'sentence'] --to-- "This is a sentence"
"""

def sortSentence(s):

    x = s.split()
    dic = {}
    for i in x :
        dic[i[-1]] = i[:-1]
    return ' '.join([dic[j] for j in sorted(dic)])

print(sortSentence('Myself2 Me1 I4 and3'))