class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        words = []
        
        for log in logs:
            
            split = log.split()
            if not split[1].isalpha():
                digits.append(log)
            else:
                words.append(log)
        def func(log):
            _id,rest = log.split(" ",maxsplit =1)
            return (0,rest,_id)            
        words.sort(key = func)
        
        return words + digits
        