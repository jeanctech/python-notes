# Operadores Aritmeticos en Python

monto_bruto = 175
tasa_interes = 12
monto_interes = monto_bruto * tasa_interes / 100
tasa_bonificacion = 5
importe_bonificacion = monto_bruto * tasa_bonificacion / 100
monto_neto = (monto_bruto - importe_bonificacion) + monto_interes

print(monto_bruto)
print(tasa_interes)
print(monto_interes)
print(tasa_bonificacion)
print(importe_bonificacion)
print(monto_neto)