#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#

# @lc code=start
class Solution:
    def __init__(self):
        self.ones = {
            "0" : "",
            "1" : " One",
            "2" : " Two",
            "3" : " Three",
            "4" : " Four",
            "5" : " Five",
            "6" : " Six",
            "7" : " Seven",
            "8" : " Eight",
            "9" : " Nine",
            "10" : " Ten",
            "11" : " Eleven",
            "12" : " Twelve",
            "13" : " Thirteen",
            "14" : " Fourteen",
            "15" : " Fifteen",
            "16" : " Sixteen",
            "17" : " Seventeen",
            "18" : " Eighteen",
            "19" : " Nineteen"
        
        }
        
        self.twos = {
            
            "2" : " Twenty",
            "3" : " Thirty",
            "4" : " Forty",
            "5" : " Fifty",
            "6" : " Sixty",
            "7" : " Seventy",
            "8" : " Eighty",
            "9" : " Ninety"
            
            
        }
        
        
    
    def grp3(self,n): 
        n = "000" + n
        n = n[-3:]
        #print(n)
        f = self.ones[n[0]]
        if f != "":
            f += " Hundred"
        
        if n[1] == "0":
            s = ""    
            
        elif n[1] == "1":
            s = self.ones[n[1:]]
            return f+s

        else:
            s = self.twos[n[1]]
        
        t = self.ones[n[2]]
        
        return f+s+t
       
        
        
    def numberToWords(self, num: int) -> str:
        
        if  num == 0:
            return "Zero"
        seq = [""," Thousand"," Million"," Billion"]
        i = 0
        
        num = str(num)
        eng = ''
        
        while len(num) > 0:
            tpart = num[-3:]
            gprt = self.grp3(tpart)
            if not gprt:
                mid = ""
            else:
                mid = seq[i]
            
            eng = gprt + mid + eng 
            num = num[:-3]
            
            i+=1
            #print(eng.strip())
        return eng.strip()
            
        
# @lc code=end

