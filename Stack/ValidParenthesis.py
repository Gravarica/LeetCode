def isValid(self, s: str) -> bool:
        parenthesis = {"{": "}", "[": "]", "(": ")"}

        if len(s) % 2 != 0: 
            return False

        stack = [] 
        for c in s: 
            if c in parenthesis: 
                stack.append(c)
            else:
                if len(stack) == 0: 
                    return False 
                parent = stack.pop()
                if c != parenthesis[parent]:
                    return False

        return len(stack) == 0