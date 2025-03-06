x = [1.2, 1.29, 1.3, 1.31, 1.4]
f = [11.59006, 13.78176, 14.04276, 14.30741, 16.86187]

f_real = 36.593535 

h1 = 0.1 
h2 = 0.01   

df_h1 = (f[4] - f[0]) / (2 * h1) 
df_h2 = (f[3] - f[1]) / (2 * h2) 

print("Aproximación de f'(1.3) con h = 0.09:", df_h1)
print("Aproximación de f'(1.3) con h = 0.01:", df_h2)

df2_h1 = (f[4] - 2*f[2] + f[0]) / (h1**2) 
df2_h2 = (f[3] - 2*f[2] + f[1]) / (h2**2)

print("\nAproximación de f''(1.3) con h = 0.09:", df2_h1)
print("Aproximación de f''(1.3) con h = 0.01:", df2_h2)

error_h1 = abs(f_real - df2_h1)
error_h2 = abs(f_real - df2_h2)

print("\nError absoluto con h = 0.09:", error_h1)
print("Error absoluto con h = 0.01:", error_h2)
