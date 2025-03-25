def Gauss(matriz):
    for i in range(1, len(matriz)-1):
        for j in range(0, len(matriz[i])-1):
            if matriz[0][0] == 0:
                aux = matriz[0]
                matriz[0] = matriz[1]
                matriz[1] = aux
                
            lamb = matriz[i+1][j]/matriz[i][j]
            matriz[i+1][j] = matriz[i+1][j] - lamb * matriz[i][j]
        
m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13,14,15,16]]
Gauss(m)