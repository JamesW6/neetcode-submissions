class Solution:
    def isValid(self, s: str) -> bool:
        past=[0]
        for letter in s:
            if letter==')':
                if past[-1]!='(':
                    return False
                else:
                    past=past[:-1]
            elif letter==']':
                if past[-1]!='[':
                    return False
                else:
                    past=past[:-1]
            elif letter == '}':
                if past[-1]!='{':
                    return False
                else:
                    past=past[:-1]
            else:
                past.append(letter)
        return past[-1]==0