from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = defaultdict(list)

        # For each thing in List
        for thing in strs:
            c_count = [0] * 26
            for c in thing:
                c_count[ord(c.lower()) % 26] += 1
            # lowered = str(sorted(thing.casefold()))
            # make a pair
                # K: sorted lowercase str
                # V: unedited str
            # insert pair
                # collisions go into lists
            anas[str(c_count)].append(thing)
        # return all lists

        return list(anas.values());
        
        