class Solution:
    
    def isValid(self, s: str) -> bool:
        
        stack = []
        close_to_open = {')': '(',
                         '}': '{',
                         ']': '['}
        
        for ch in s:
            
            #if it a closing parenthes
            if ch in close_to_open :
                if stack and stack[-1] == close_to_open[ch]:
                    stack.pop()
                else:
                    return False
            # if it is an opening parancesses
            else:
                stack.append(ch)
        
        
        return True if not stack else False
            
                
                
        