class Solution:
    def maxArea(self, h: int, w: int, hori: List[int], verti: List[int]) -> int:
        hori.sort()
        verti.sort()
        x = hori[0]
        for i in range(1, len(hori)):
            x = max(x, hori[i]-hori[i-1])
        x = max(x, h - hori[-1])
        y = verti[0]
        for i in range(1, len(verti)):
            y = max(y, verti[i]-verti[i-1])
        y = max(y, w - verti[-1])
        return (x*y)%1000000007
        