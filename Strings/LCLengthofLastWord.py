#Problem 58 - Easy

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        cont = 0
        print(length)
        if length==1 and s != " ":
            return 1
        else:
            for i in range(length-1, -1, -1):
                if s[i] == " ":
                    if cont > 0:
                        break
                    else:
                        pass
                else:
                    cont += 1
            return cont