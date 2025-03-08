t = [0, 2, 4, 6, 8, 10, 12, 14, 16]
p = [0, 0.7, 1.8, 3.4, 5.1, 6.3, 7.3, 8, 8.4]

h = 2
v = []
a = []


print("\nVelocidad:\n")

for i, valor in enumerate(p):
    if i == len(p)-1:
        v.append((p[i]-p[i-1])/h)
        break
    else:
        v.append((p[i+1]-p[i])/h)

for i, value in enumerate(t):
    print("Velocidad en tiempo ", value, ": ", v[i])


for i, valor in enumerate(v):
    if i == len(v)-1:
        a.append((v[i]-v[i-1])/h)
        break
    else:
        a.append((v[i+1]-v[i])/h)
        
print("\nAceleración:\n")
for i, value in enumerate(t):
    print("Aceleración en tiempo ", value, ": ", a[i])