'''
    defaultdict is used for assigning values to a specific key. this key can be anything 
    it can assign value to the same key and when it gets a new value, it uses that value 
    as a new key adds values to it. those value's type can be defined at the declaration.
'''
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c)-ord("a")] += 1
            result[tuple(chars)].append(s)
        return result.values()


'''
-traversing to each string from the list of the string 
-making a list of small letter alphabetes containing 0s in each position
-for each character of each string, increasing count as the specific character appears
-using that chars list as the key of the defaultdict, convert it to a tuple as ,
only the immutable class can be used as keys of defaultdict
-append the string list for each keys 
-return only the values of the keys as they contains the lists of similar tuple key

for, strs = ["eat", "tea", "tan", "ate", "nat", "bat"] keys and values would be

(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
['eat']
(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
['eat', 'tea']
(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0) (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
['eat', 'tea'] ['tan']
(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0) (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
['eat', 'tea', 'ate'] ['tan']
(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0) (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
['eat', 'tea', 'ate'] ['tan', 'nat']
(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0) (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0) (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
['eat', 'tea', 'ate'] ['tan', 'nat'] ['bat']
'''