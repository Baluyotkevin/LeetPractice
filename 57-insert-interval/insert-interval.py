class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans_list = []

        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                ans_list.append(intervals[i])
                continue
            if newInterval[1] < intervals[i][0]:
                ans_list.append(newInterval)
                ans_list = [*ans_list, *intervals[i:]]
                return ans_list
            else:
                new_start_interval = min(newInterval[0], intervals[i][0])
                new_end_interval = max(newInterval[1], intervals[i][1])
                newInterval = [new_start_interval, new_end_interval]
        ans_list.append(newInterval)
        return ans_list


            