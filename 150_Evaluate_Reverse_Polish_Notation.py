
def evalRPN(tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack=[]
        char="+-*/"
        for ele in tokens:
            if ele not in char:
                stack.append(int(ele))

            else:
                if ele=="+":
                    stack[-2]=int(stack[-2])+int(stack[-1])
                    stack.pop()

                elif ele=="-":
                    stack[-2]=int(stack[-2])-int(stack[-1])
                    stack.pop()

                elif ele=="*":
                    stack[-2]=int(stack[-2])*int(stack[-1])
                    stack.pop()

                elif ele=="/":
                    stack[-2]=int(stack[-2])/int(stack[-1])
                    stack.pop()


        return stack[0]

if __name__=="__main__":
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    evalRPN(tokens)
