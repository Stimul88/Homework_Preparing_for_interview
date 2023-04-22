from class_stack import Stack

def balans(balans_string):

    open_brack = ['(', '{', '[']
    close_brack = [')', '}', ']']

    stack = Stack()

    if stack.size() % 2 != 0:
        return 'Несбалансированно'
    else:

        for i, char in enumerate(balans_string):
            if char in open_brack:
                stack.push(char)
            elif char in close_brack:
                if stack.is_empty():
                    return 'Несбалансированно'
                elif open_brack.index(stack.peek()) != close_brack.index(char):
                    return 'Несбалансированно'
                else:
                    stack.pop()
                    if stack.is_empty() and i == len(balans_string) - 1:
                        return 'Сбалансированно'
