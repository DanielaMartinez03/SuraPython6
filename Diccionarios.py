#Los diccionarios son variables especiales que me permiten almacenar multiples datos de diferente tipo en una sola variable

empleado={
    'Nombre':"Juan",
    'Cedula':"10017728589",
    'Cargo':"Analista de datos",
    'Salario':7000000,
    'Horas trabajadas':48,
    'SubsidioDeTransporte':False,
    'Deudas':[1500000,800000]

}
print(empleado)
print(empleado['Nombre'])
print(empleado['Deudas'][1])

#Recorriendo un diccionario:
for observadorAtributo,ObservadorValor in empleado.items():
    print(observadorAtributo)
    print(ObservadorValor)