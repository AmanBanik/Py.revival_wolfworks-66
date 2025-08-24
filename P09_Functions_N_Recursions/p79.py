def f_c(f):
    c= 5*(f - 32)/9
    return c
f=int(input('Enter the temp in °F: '))
print(f'{f} °F in Celsius scale is {round(f_c(f),2)} °C')# rounded to 2 decimals