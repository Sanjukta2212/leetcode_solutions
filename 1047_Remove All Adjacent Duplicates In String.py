# You are given a string s consisting of lowercase English letters. 
# A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that 
# the answer is unique.

def removeDuplicates(s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            if stack:
                stack_top=stack[-1]
            else:
                stack_top=None
            if not stack_top:
                stack.append(char)
            elif stack_top==char:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
        
if __name__=="__main__":
     s = "abbaca"
     removeDuplicates(s)