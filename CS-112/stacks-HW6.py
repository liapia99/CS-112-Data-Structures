def check_parentheses(s):
    stack = []
    parentheses = {'(': ')', '{': '}', '[': ']'}
    for n in s:
        if n in parentheses:
            stack.append(n)
        elif n in parentheses.values():
            if not stack:
                return "Incorrect: You have a closing bracket without an opening bracket."
            if parentheses[stack.pop()] != n:
                return "Incorrect: You have mismatched brackets."
    if len(stack) > 0:
        return "Incorrect: You have unclosed brackets."
    else:
        return "Correct!"

text = input("Enter a string with parentheses: ")
print(check_parentheses(text))
