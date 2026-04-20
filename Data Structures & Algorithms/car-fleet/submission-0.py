class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        num_fleets = 0
        pos_speed = sorted(zip(position, speed), reverse = True)
        max_time = 0

        for pos, spd in pos_speed:
            time = (target - pos) / spd

            # If this car takes longer, it can't catch up → new fleet
            if time > max_time:
                num_fleets += 1
                max_time = time

        return num_fleets