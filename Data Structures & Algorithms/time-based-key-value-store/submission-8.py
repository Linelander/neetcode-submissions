from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.tab = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tab[key].append((timestamp, value))        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.tab[key]
        i = bisect_right(arr, (timestamp, chr(127)))
        return arr[i - 1][1] if i else ""