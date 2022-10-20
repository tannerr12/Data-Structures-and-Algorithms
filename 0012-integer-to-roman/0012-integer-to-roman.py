class Solution:
    def intToRoman(self, num: int) -> str:

            res = ''
       
            if num >= 1000:
                for i in range(num // 1000):
                    res += 'M'
                
                num = num % 1000
           
            
            if num >=900 and num < 1000:
                res += 'CM'
                num -= 900
            if num >= 500 and num < 900:
                res += 'D'
                num -= 500
                
            if num >= 400 and num < 500:
                res += 'CD'
                num -= 400
            
            if num >= 100:
                for i in range(num // 100):
                    res += 'C'
                
                num = num % 100
            
            if num >= 90 and num < 100:
                res += 'XC'
                num -= 90
                
            if num >= 50:
                res +='L'
                num -= 50
            
            if num >= 40 and num < 50:
                res +='XL'
                num -=40
            if num >= 10:
                for i in range(num // 10):
                    res += 'X'
                
                num = num % 10
            
            if num == 9:
                res+= 'IX'
                num -= 9
            
            if num >= 5:
                res+= 'V'
                num -=5
            
            if num == 4:
                res += 'IV'
                num -= 4
            if num >= 1:
                for i in range(num // 1):
                    res += 'I'
                
                num = 0
            
            
            return res
            
                