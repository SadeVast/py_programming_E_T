#TODO

L = ['h', 'l', 'o']
M = ['e', 'l', '!']

# print(*[(L[i]) + (M[i]) for i in range(len(L))])
list_new = list(L[i] + M[i] for i in range(len(L)))
print(*list_new)
