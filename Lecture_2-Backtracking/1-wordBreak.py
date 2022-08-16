"""
Word Break problem

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a
valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "catsanddog", wordDict = "cat","cats","and","sand","dog"

Output: "cats and dog","cat sand dog"

Example 2:

Input: s = "pineapplepenapple", wordDict = "apple","pen","applepen","pine","pineapple"

Output: "pine apple pen apple","pineapple pen apple","pine applepen apple"

Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = "cats","dog","sand","and","cat"

Output: []
"""
def wordBreak(str, ans):
    if len(str) == 0:
        print(ans)
        return
    for i in range(len(str)):
        if str[:i+1] in dict:
            ans.append(str[:i+1])
            wordBreak(str[i+1:],ans)
            ans=[]

dict={"cat","cats","and","sand","dog"}
wordBreak("catsanddog",[])