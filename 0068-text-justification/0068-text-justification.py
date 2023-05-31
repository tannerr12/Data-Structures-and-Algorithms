class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        i = 0
        res = []
        while i < len(words):
            line = ''
            size = 0
            j = i
            while i < len(words) and ((size + len(words[i]) + 1 <= maxWidth) or size == 0):
                size += len(words[i]) +1
                i+=1
            
            if i < len(words) and len(words[i]) == maxWidth - size:
                size += len(words[i])
                i+=1
            else:
                size -=1
            if i - j == 1:
                line = words[j]
                line += ' ' * (maxWidth - len(line))
                res.append(line)
                continue
            elif i >= len(words):
                while j < i:
                    line += words[j]
                    if j < i-1:
                        line += ' '
                    j +=1
                line += ' ' * (maxWidth - len(line))
                res.append(line)
                continue
            diff = maxWidth - size
            calc = diff // (i - j -1)
            if calc > 0:
                rem = diff % (i - j -1)
            else:
                rem = diff
            while j < i:
                if j == i-1:
                    line+= words[j]
                else:
                    add = calc + 1 
                    add += rem > 0
                    line += words[j] + (' ' * (add))
                    rem -=1
                j+=1
            
            res.append(line)
            
        
        return res
            
            
            
            
            