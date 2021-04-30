input_data = open("input_data/day18.txt").read().splitlines()
def parse_char(x):
    try:
        return int(x)
    except:
        return x

expressions = []
for line in input_data:
    line = list(line.replace(' ',''))
    expressions.append([parse_char(x) for x in line])

ans = 0
for expression in expressions:
    token_stack = []
    token_stack.append(expression[0])
    for token in expression[1:]:
        if token in ['+','*','(']:
            token_stack.append(token)
        elif token == ')':
            value = token_stack.pop()
            assert token_stack.pop() == '('
            if len(token_stack) > 0:
                operation = token_stack.pop()
                if operation == '+':
                    token_stack.append(token_stack.pop() + value)
                elif operation == '*':
                    token_stack.append(token_stack.pop() * value)
                elif operation == '(':
                    token_stack.append(operation)
                    token_stack.append(value)
            else:
                token_stack.append(value)
 
        else:
            operation = token_stack.pop()
            if operation == '+':
                token_stack.append(token_stack.pop() + token)
            elif operation == '*':
                token_stack.append(token_stack.pop() * token)
            elif operation == '(':
                token_stack.append(operation)
                token_stack.append(token)
    ans += token_stack.pop()
print(ans)
