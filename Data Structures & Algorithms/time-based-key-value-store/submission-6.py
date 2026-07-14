class TimeMap:

    def __init__(self):
        self.tab = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tab[key].append((timestamp, value))        
        self.tab[key].sort()

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tab: return ""
        result = self.tab[key][0]
        i = 1
        while result[0] < timestamp and i < len(self.tab[key]):
            if self.tab[key][i][0] > timestamp: break
            result = self.tab[key][i]
            i += 1
        if result[0] <= timestamp: return result[1]
        return ""