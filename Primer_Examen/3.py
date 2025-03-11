import matplotlib.pyplot as plt

P_total = 15000
P_0 = 5000
h = 0.01
P = [5000]
P_no_contagiadas = [10000]
t = [0]

i = 0
timpo_que_pasa = 0

while i < 100:
    P.append(1e-5 * P_0 *  h * (P_total-P_0)+P[-1])
    P_no_contagiadas.append(P_total - P[-1])
    t.append(i)
    
    if P[-1] - 5000 >= 5000:
        timpo_que_pasa = i
        
    if P_no_contagiadas[-1] <= 0:
        break
        
    
    i += h



print("Tiempo transcurrido para otros 5000 contagios: ", timpo_que_pasa)

plt.plot(t, P, 'b', label='$P(x)=Contagiados$')
plt.plot(t, P_no_contagiadas, 'r', label='$Pnocontagiados(x)=No Contagiados$')

plt.legend()
plt.xlabel('Tiempo')
plt.ylabel('Contagios')

plt.show()

