t = [0, 2, 4, 6, 8, 10]
v = [0, 3, 6, 9, 12, 15]
h = 2
x0 = 0
a=[]

for i in range(0, len(v)):
    if i != len(v)-1:
        a.append((v[i+1] - v[i])/h)
    else:
        a.append((v[i] - v[i-1])/h)
        break
        
print(a)
    