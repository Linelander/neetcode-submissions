class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        fleets = 0
        slowest = float('-inf')
        
        for p, s in cars:
            time = (target - p) / s
            if time > slowest:
                slowest = time
                fleets += 1

        return fleets