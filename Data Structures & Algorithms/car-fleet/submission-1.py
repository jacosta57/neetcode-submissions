class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        groups = 0
        cars = sorted(zip(position, speed), reverse=True)
        
        last_time = -1
        for p, s in cars:
            time = (target - p) / s
            if time > last_time:
                groups += 1
                last_time = time
        return groups