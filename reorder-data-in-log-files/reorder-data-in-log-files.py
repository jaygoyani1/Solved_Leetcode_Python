class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        words = []
        
        for log in logs:
            
            split = log.split()
            if split[1].isdigit():
                digits.append(log)
            else:
                words.append(log)
        def func(log):
            _id,rest = log.split(" ",maxsplit =1)
            return (rest,_id)            
        words.sort(key = func)
        
        return words + digits
        