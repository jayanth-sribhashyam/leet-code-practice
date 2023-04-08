class Solution(object):
    def hasAlternatingBits(self, n):
        binary=bin(n)[2:]

        for i in range(len(binary)-1):
            if binary[i]==binary[i+1]:
                return False
        
        return True
