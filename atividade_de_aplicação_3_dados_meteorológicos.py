#Sophia Victória Borguezan Kim 11202320185
#devido a razões acadêmicas começarei a atravessar a rua sem olhar pros lados
import pandas as pd

df = pd.read_csv(input())
d = input()
m = input()
r = float(input())

v = df['Densidade do ar {kg/m3}'].median()
print("Mediana da densidade do ar:", "%.2f" % v, "kg/m3")

w = df['Velocidade do Vento {m/s}'].max()
print("Maxima velocidade do vento:", "%.2f" % w, "m/s")

x = df['Entalpia {BTU/LB}'].min()
print("Entalpia minima:", "%.2f" % x, "btu/lb")

y = df.query("Dia == "+ d+"and Mes =="+m)["Direcao do Vento {graus}"].mean()
print("Media da direcao do vento no dia", d, "do mes", m+ ':', "%.2f" % y, "graus")

z = (df['Rad Direta Normal {Wh/m2}'] >= int(r)).sum()
print(z)