"""
https://leetcode.jp/problemdetail.php?id=1772

Use two maps to store the indices of each feature in features, and the appearances of each feature in responses.
Loop over features and responses to put the value into the two maps. Then sort features first according to the
appearances in descending order next according to the indices in ascending order. Return the sorted array features.
"""
import collections

def sortFeatures(features, responses):
    features_set = set(features)
    order = {word: i for i, word in enumerate(features)}
    freq = collections.defaultdict(int)
    for r in responses:
        for word in set(r.split(' ')):
            if word in features_set:
                freq[word] += 1
    features.sort(key=lambda x: (-freq[x], order[x]))
    return features

print(sortFeatures(["cooler","lock","touch"],["i like cooler cooler","lock touch cool","locker like touch"]))