# s = "[(])"
# n = len(s)
# a = 0
# for i in range(0,n):
#     if s[i] == "(":
#         a += 1
#     elif s[i] == '[':
#         a += 2
#     elif s[i]== '{':
#         a += 3
#     elif s[i] == ')':
#         a -= 1
#     elif s[i] == "]":
#         a -= 2
#     elif s[i] == "}":
#         a -= 3
# if a == 0:
#    for i in range(0,n):
#         if s[i] == '(':
#             ch = ' '
#             count = 0
#             while ch != (")"):
#                 i = i+1
#                 if s[i] == '[' or '{':
#                     count += 1
#                 elif s[i] == ']' or '}':
#                     count -= 1
# else:
#     print('false')
# s = '([])'
# n = len(s)
# pointer_1= 0
# pointer_2 = n-1
# while pointer_1 < pointer_2:
#         if s[pointer_1] == s[pointer_2]:
#             pointer_1+=1
#             pointer_2-=1
#             print("balanced")
#             break
        # else:
        #     print("inbalenced")
        #     break
s = '([][{]})'
stack = []
b = True
if len(s) % 2 != 0:
    print('false')
else:
    for i in s:
        if i in ["(", "{", "["]:
            stack.append(i)
            print(stack)
        else:
            c = stack.pop()
            if c == '(':
                if i != ')':
                    b = False
                    break
            if c == '[':
                if i != ']':
                    b = False
                    break
            if c == '{':
                if i != '}':
                    b = False
                    break 
print(b)   