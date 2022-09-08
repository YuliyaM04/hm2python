
a = "abababa"
b = "aba"
n = 0
for first in range(len(a) - len(b) + 1):
    if a[first:first+len(b)] == b:
        n += 1
print(a) 
print(b)
print(n)