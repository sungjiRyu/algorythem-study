def is_correct_parenthesis(string):

    stack = []

    for char in string:
        if char == "(":
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True

# # 틀린 풀이 (중간에 닫는괄호가 먼저나와도 오류 못잡음 "))(("
# def is_correct_parenthesis(string):
#
#     check_count = 0
#
#     for char in string:
#         if char == '(':
#             check_count += 1
#         else:
#             check_count -= 1
#
#     return check_count == 0


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))