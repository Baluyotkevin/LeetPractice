class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        curr = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] - curr > 0:
                curr += 1
        return curr