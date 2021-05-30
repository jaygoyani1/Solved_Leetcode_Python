class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        max_letter = keysPressed[0]
        
        max_duration = releaseTimes[0]
        
        for i in range(1,len(releaseTimes)):
            curr_time = releaseTimes[i] - releaseTimes[i-1]
            
            if curr_time > max_duration:
                max_letter = keysPressed[i]
                max_duration = curr_time
            elif curr_time == max_duration:
                if keysPressed[i] > max_letter:
                    max_letter = keysPressed[i]
                    
        return max_letter
        