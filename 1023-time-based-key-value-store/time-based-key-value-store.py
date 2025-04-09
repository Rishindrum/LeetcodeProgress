class TimeMap:

    def __init__(self):
        self.timeMap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if self.timeMap[key]:
            left = 0
            right = len(self.timeMap[key]) - 1

            while left <= right:
                #[(1,bar)]
                mid = (left+right)//2
                if self.timeMap[key][mid][0] > timestamp:
                    right = mid - 1
                elif mid + 1 < len(self.timeMap[key]):
                    if self.timeMap[key][mid+1][0] > timestamp:
                        return self.timeMap[key][mid][1]
                    else:
                        left = mid + 1
                else:
                    return self.timeMap[key][mid][1]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)