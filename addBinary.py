class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        result = ''
        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            result += str(carry %2)
            carry //= 2
        return result[::-1]

        # or 
        # result = int(a,2) + int(b,2)
        # return bin(result)[2:]

solution = Solution()
a = '11'
b = '1'
result = solution.addBinary(a,b)
print(result)