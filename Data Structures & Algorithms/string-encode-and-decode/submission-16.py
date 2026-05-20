class Solution:

    def encode(self, strs: List[str]) -> str:
        msg =""
        for stringus in strs:
            msg += "/"
            msg += str(len(stringus))
            msg += "/"
            msg += stringus
        print(msg)
        return msg

    def decode(self, s: str) -> List[str]:
        chopped = []

        i = 0
        length = 0
        while i < len(s):
            if s[i] == "/":
                i += 1

                d = i
                while d < len(s) and s[d].isdigit() and s[d] != "/":
                    d += 1

                if i < len(s):
                    length = int(s[i:d])
                i = d + 1
                chopped.append(s[i:i+length])
                i += length
            else:
                i += 1
        
        return chopped

        
