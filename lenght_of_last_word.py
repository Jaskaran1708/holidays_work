s = 'hello world '
s = s.strip()
count = 0
for i in reversed(s):
    if i != ' ':
        count += 1
    else:
        break
print(count)
# s = 'hello world'
# stack = []
# count = 0
# for i in range(0,len(s)):
#     stack.append(s[i])
# for i in range(0,len(s)):
#         c = stack.pop
#         if not(c == ' '):
#                 count += 1
#         elif c == ' ':
#             break
# print(count)

