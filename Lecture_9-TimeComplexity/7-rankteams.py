"""
https://leetcode.com/problems/rank-teams-by-votes/

Very smart solution:

For the input ["WXYZ","XYZW"], create a Map as follows:
W:1001
X:1100
Y:0110
Z:0011

Which is simply the number of votes received by the team for each position
Then sort the letters by descending order of these values
"""
def rankTeams(votes):
    count = {v: [0] * len(votes[0]) for v in votes[0]}
    for vote in votes:
        for i, v in enumerate(vote):
            count[v][i] -= 1 #Because we need descending sort
    return ''.join(sorted(votes[0], key=count.get))

print(rankTeams(["WXYZ","XYZW"]))