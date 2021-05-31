class FirstUnique:

    def __init__(self, nums: List[int]):
        self.dic = {}
        self.arr = OrderedDict()
        for i in nums:
            self.add(i)
            
    def showFirstUnique(self) -> int:
        if self.arr:
            return next(iter(self.arr)) 
        return -1

    def add(self, value: int) -> None:
        if value not in self.dic:
            self.dic[value] = True
            self.arr[value] = None
        elif self.dic[value]:
            self.dic[value] = False
            self.arr.pop(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)