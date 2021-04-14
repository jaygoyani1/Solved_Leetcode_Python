class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = collections.defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.list[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.list[key]
        if not values: return ''
        left, right = 0, len(values) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            pre_time, value = values[mid]
            if pre_time > timestamp:
                right = mid - 1
            else:
                ans = mid
                left = mid + 1
        return values[ans][1] if ans != -1 else ''
            
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)