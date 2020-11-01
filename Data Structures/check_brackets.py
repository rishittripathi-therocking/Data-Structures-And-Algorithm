import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read().strip('\n')
    opening_brackets_stack = []
    result = True
    for i, next in enumerate(text, start=1):
        if next in ['(', '[', '{']:
            opening_brackets_stack.append(Bracket(next, i))
        elif next in [')', ']', '}']:
            if not opening_brackets_stack:
                result = i
                break
            else:
                bracket = opening_brackets_stack[-1]
                result = bracket.Match(next)
                if result:
                    del opening_brackets_stack[-1]
                else:
                    result = i
                    break
    if result == i and not opening_brackets_stack:
        print(result)
    elif result == True and not opening_brackets_stack:
        print('Success')
    elif result == True and opening_brackets_stack:
        print(opening_brackets_stack[-1].position)
    else:
        print(result)