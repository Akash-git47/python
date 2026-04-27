from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        key = tuple(sorted(w))  # canonical key
        groups[key].append(w)
    return list(groups.values())

print(group_anagrams([
    "eat","tea","tan","ate","nat","bat"
]))
# [['eat','tea','ate'],['tan','nat'],['bat']]