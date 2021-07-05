"""
https://leetcode.com/problems/rearrange-words-in-a-sentence/

Basic Idea :

we will use the map to store the list of strings of same length
key will be length of string, value will be list of strings of same length;
will keep the track of length of longest string(max)
then just iterate thorugh all the lenghs from 1 to max;
get the list of current lengh, i , from map and appends the strings to answer

"""

def arrangeWords(text: str) -> str:
    return " ".join(sorted(text.split(" "), key=len)).capitalize()

print(arrangeWords('To be or not to be'))