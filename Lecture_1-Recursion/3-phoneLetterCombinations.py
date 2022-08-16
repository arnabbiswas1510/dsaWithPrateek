"""
Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23" Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = "" Output: []

Example 3:

Input: digits = "2" Output: ["a","b","c"]

"""
class Phone:
    phoneMap={
        0:"",
        1:"",
        2:"abc",
        3:"def",
        4:"ghi",
        5:"jkl",
        6:"mno",
        7:"pqrs",
        8:"tuv",
        9:"wxyz"
    }

    def combinations(self, input, str, idx):
        if len(input) == len(str):
            print(str)
            return
        keys = self.phoneMap[int(input[idx])]
        for i in range(len(keys)):
            str.append(keys[i]) #Note same logic here of permutations of string
            self.combinations(input,str,idx+1)
            str.pop()

ph = Phone()
ph.combinations("27",[],0)