class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = 0
        for i in reversed(range(len(num1))):
            i_digit = int(num1[i]) * (10**(len(num1) - 1 - i))
            for j in reversed(range(len(num2))):
                j_digit = int(num2[j]) * (10**(len(num2) - 1 - j))
                product += i_digit * j_digit
        return str(product)