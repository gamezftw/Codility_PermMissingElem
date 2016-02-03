A = [1, 2, 3, 4, 6, 7, 8, 9]
s = 0
t = 0
if (len(A) + 1) % 2 == 0:
    t = (len(A) + 2) * (len(A) + 1) / 2
if (len(A) + 1) % 2 == 1:
    t = (len(A) + 2) * (len(A) + 1) / 2
for a in A:
    s += a
print t - s
