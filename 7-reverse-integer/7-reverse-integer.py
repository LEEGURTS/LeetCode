class Solution:
    def reverse(self, x: int) -> int:
        string = ""

        if x >= 0:
            string = str(x)[::-1]
        else:
            string = "-" + str(x)[1::][::-1]
        x = int(string)
        if x <= -2**31 or x >= (2**31)-1:
            return 0    
        return x