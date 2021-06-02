class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        ban = set(banned)
        max_count = 0
        ans = ""
        word = collections.defaultdict(int)
        buffer = []
        for i,char in enumerate(paragraph):
            
            if char.isalnum():
                buffer.append(char.lower())
                if i !=len(paragraph)-1:
                    continue
            
            if len(buffer) >0:
                word1 = "".join(buffer)
                if word1 not in ban:
                    word[word1] +=1

                    if max_count < word[word1]:
                        max_count = word[word1]
                        ans = word1
                buffer = []
        return ans
                    
        