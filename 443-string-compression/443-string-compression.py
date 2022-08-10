class Solution:
    def compress(self, chars: List[str]) -> int:
        
        writer = 0
        ancher = 0
        
        while (ancher < len(chars)):
            counter = ancher
            while counter < len(chars) and chars[counter] == chars[ancher]:
                counter += 1
            chars[writer] = chars[ancher]
            writer += 1
            if counter - ancher > 1:
                temp = str(counter - ancher )
                for ch in temp:
                    chars[writer] = ch
                    writer += 1
            ancher = counter
            
        return writer
            