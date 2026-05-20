from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = defaultdict(list)

        # For each thing in List
        for thing in strs:
            c_count = [0] * 26
            for c in thing:
                c_count[ord(c.lower()) % 26] += 1
            anas[str(c_count)].append(thing)

        return list(anas.values());
        
        