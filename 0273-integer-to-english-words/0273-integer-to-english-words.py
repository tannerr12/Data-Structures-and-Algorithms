class Solution:
    def numberToWords(self, num: int) -> str:
        #handle 0s (positions matter)
        #fix twenty
        #fix fifty
        #fix thirty
        if num == 0:
            return 'Zero'
        
        words = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        plural = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        custom = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 8: 'Eighty'}
        position = ["", "", "Hundred", "Thousand", "Million", "Billion", "Trillion"]
        pos = 1
        ans = []
        num1 = -1
        num2 = -1
        
        nums = str(num)
        
    
        #hundred
        
        
        if pos + 1 > len(nums):
            num1 = int(nums[-pos])
            return words[num1]
        
        elif pos + 2 > len(nums):
            num1 = int(nums[-pos])
            num2 = int(nums[-pos-1])
            if num2 == 1:
                ans.append(plural[num1])
            else:
                ans.append((words[num2] if num2 not in custom else custom[num2]) + ('ty ' if num2 > 1 and num1 > 0 and num2 not in custom else '') + ('ty' if num2 > 1 and num1 == 0 and num2 not in custom else '') + (' ' if (num2 in custom or (num2 == 0 and num3 > 0)) and num1 > 0 else '') + words[num1])
        
        else:
            num1 = int(nums[-pos])
            num2 = int(nums[-pos-1])
            num3 = int(nums[-pos-2])
            if num2 == 1:
                ans.append(words[num3] + (" Hundred " if num3 > 0 else '') + plural[num1])

            else:
                ans.append(words[num3] + (" Hundred" if num3 > 0 else '') + (' ' if num2 > 0 and num3 > 0 else '')  + (words[num2] if num2 not in custom else custom[num2]) + ('ty ' if num2 > 1 and num1 > 0 and num2 not in custom else '') + ('ty' if num2 > 1 and num1 == 0 and num2 not in custom else '') + (' ' if (num2 in custom or (num2 == 0 and num3 > 0)) and num1 > 0 else '') + words[num1])
        
        pos += 3
        if pos <= len(nums):
            #thousand
            if pos + 1 > len(nums):            
                num1 = int(nums[-pos])
                ans.append(words[num1] + " Thousand")

            elif pos + 2 > len(nums):
                num1 = int(nums[-pos])
                num2 = int(nums[-pos-1])
                if num2 == 1:
                    ans.append(plural[num1] + " Thousand")
                else:
                    ans.append((words[num2] if num2 not in custom else custom[num2]) + ('ty ' if num2 > 1 and num1 > 0 and num2 not in custom else '') + ('ty' if num2 > 1 and num1 == 0 and num2 not in custom else '') + (' ' if (num2 in custom or (num2 == 0 and num3 > 0)) and num1 > 0 else '') + words[num1] + " Thousand")

            else:
                num1 = int(nums[-pos])
                num2 = int(nums[-pos-1])
                num3 = int(nums[-pos-2])
                if num2 == 1:
                    ans.append(words[num3] + (" Hundred " if num3 > 0 else '') + plural[num1] + " Thousand")
                else:
                    ans.append(words[num3] + (" Hundred" if num3 > 0 else '') + (' ' if num2 > 0 and num3 > 0 else '')  + (words[num2] if num2 not in custom else custom[num2]) + ('ty ' if num2 > 1 and num1 > 0 and num2 not in custom else '') + ('ty' if num2 > 1 and num1 == 0 and num2 not in custom else '') + (' ' if (num2 in custom or (num2 == 0 and num3 > 0)) and num1 > 0 else '') +  words[num1] + " Thousand")

        pos += 3
        
        #million
        if pos <= len(nums):
            if pos + 1 > len(nums):            
                num1 = int(nums[-pos])
                ans.append(words[num1] + " Million")

            elif pos + 2 > len(nums):
                num1 = int(nums[-pos])
                num2 = int(nums[-pos-1])
                if num2 == 1:
                    ans.append(plural[num1] + " Million")
                else:
                    ans.append((words[num2] if num2 not in custom else custom[num2]) + ('ty ' if num2 > 1 and num1 > 0 and num2 not in custom else '') + ('ty' if num2 > 1 and num1 == 0 and num2 not in custom else '') + (' ' if (num2 in custom or (num2 == 0 and num3 > 0)) and num1 > 0 else '') + words[num1] + " Million")

            else:
                num1 = int(nums[-pos])
                num2 = int(nums[-pos-1])
                num3 = int(nums[-pos-2])
                if num2 == 1:
                    ans.append(words[num3] + (" Hundred " if num3 > 0 else '') + plural[num1] + " Million")
                else:
                    ans.append(words[num3] + (" Hundred" if num3 > 0 else '') + (' ' if num2 > 0 and num3 > 0 else '')  + (words[num2] if num2 not in custom else custom[num2]) + ('ty ' if num2 > 1 and num1 > 0 and num2 not in custom else '') + ('ty' if num2 > 1 and num1 == 0 and num2 not in custom else '') +  (' ' if (num2 in custom or (num2 == 0 and num3 > 0)) and num1 > 0 else '') + words[num1] + " Million")


        pos += 3
        
        #Billion
        if pos <= len(nums):
            num1 = int(nums[-pos])
            ans.append(words[num1] + " Billion")
            
        '''
        #Trillion
        num1 = int(nums[-pos])
        num2 = int(nums[-pos-1])
        num3 = int(nums[-pos-2])
        
        ans.append(words[num3] + " Hundred " + words[num2] + 'ty ' + words[num1] + " Trillion")
        '''
        ans = ans[::-1]
        w = ''
        for wo in ans:
            if len(wo) > 0 and wo != ' Thousand' and wo != " Million":
                if len(w) > 0:
                    w += ' '
                w += wo
        return w