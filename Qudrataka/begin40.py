A1 = float(input('Birinchi koeffisentni kiriting: '))
B1 = float(input('Ikkinchi koeffisentni kiriting: '))
C1 = float(input('Uchinchi koeffisentni kiriting: '))
A2 = float(input('Birinchi koeffisentni kiriting: '))
B2 = float(input('Ikkinchi koeffisentni kiriting: '))
C2 = float(input('Uchinchi koeffisentni kiriting: '))
D = A1*B2-A2*B1
print('Determinant: ', D)
print('X noma\'lum: ', (C1*B2-C2*B1)/D)
print('Y noma\'lum: ', (A1*C2-A2*C1)/D)
