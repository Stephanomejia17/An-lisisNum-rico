t = [0, 25, 50, 75, 100, 125]
y = [0, 32, 58, 78, 92, 100]

h = 25

v = [0]
a = [0]

print("\nVelocidad:\n")

for i, valor in enumerate(y):
    if i == len(y)-1:
        v.append((y[i]-y[i-1])/h)
        break
    else:
        v.append((y[i+1]-y[i])/h)

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
    print("Aceleracion en tiempo ", value, ": ", a[i])
    
print("\nEn t=50 la aceleracion es igual a -0.0096")