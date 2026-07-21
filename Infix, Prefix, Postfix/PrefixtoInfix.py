def prefixtoInfix(s):
    stack=[]
    for char in s[::-1]:
        if char.isalnum():
            stack.append(char)
        else:
            operand1=stack.pop()
            operand2=stack.pop()

            newExpr=f'({operand1}{char}{operand2})'
            stack.append(newExpr)
    return stack[-1]
print(prefixtoInfix('*d+a*ab'))