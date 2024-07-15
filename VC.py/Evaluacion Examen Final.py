import random

import csv

import math


empleados = [

  "Juan Pérez", "María García", "Carlos López", "Ana Martínez",
  "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", 
  "Isabel Gómez", "Francisco Díaz", "Elena Fernández"

]

salarios = []


def asignar_salarios():

  global salarios

  salarios = [random.randint(300000, 2500000) for _ in empleados]

  print("Sueldos asignados aleatoriamente.")


def categorizar_salarios():

  menores_800k = [(empleados[i], salario) for i, salario in enumerate(salarios) if salario < 800000]

  entre_800k_2m = [(empleados[i], salario) for i, salario in enumerate(salarios) if 800000 <= salario <= 2000000]

  mayores_2m = [(empleados[i], salario) for i, salario in enumerate(salarios) if salario > 2000000]


  print("\nSueldos menores a $800.000")

  for empleado, salario in menores_800k:

    print(f"{empleado} - ${salario}")

  print(f"TOTAL: {len(menores_800k)}\n")


  print("Sueldos entre $800.000 y $2.000.000")

  for empleado, salario in entre_800k_2m:

    print(f"{empleado} - ${salario}")

  print(f"TOTAL: {len(entre_800k_2m)}\n")


  print("Sueldos superiores a $2.000.000")

  for empleado, salario in mayores_2m:

    print(f"{empleado} - ${salario}")

  print(f"TOTAL: {len(mayores_2m)}\n")


  total_salarios = sum(salarios)

  print(f"TOTAL SUELDOS: ${total_salarios}")


def mostrar_estadisticas():

  if not salarios:

    print("Debe asignar los sueldos primero.")

    return


  salario_mas_alto = max(salarios)

  salario_mas_bajo = min(salarios)

  promedio_salarios = sum(salarios) / len(salarios)

  media_geometrica = math.exp(sum(math.log(salario) for salario in salarios) / len(salarios))


  print(f"\nSueldo más alto: ${salario_mas_alto}")

  print(f"Sueldo más bajo: ${salario_mas_bajo}")

  print(f"Promedio de sueldos: ${promedio_salarios}")

  print(f"Media geométrica: ${media_geometrica}")


def generar_reporte_salarios():

  if not salarios:

    print("Debe asignar los sueldos primero.")

    return


  descuentos_salud = [salario * 0.07 for salario in salarios]

  descuentos_afp = [salario * 0.12 for salario in salarios]

  salarios_liquidos = [salario - salud - afp for salario, salud, afp in zip(salarios, descuentos_salud, descuentos_afp)]


  print("\nNombre empleado | Sueldo Base | Descuento Salud | Descuento AFP | Sueldo Líquido")

  for i in range(len(empleados)):

    print(f"{empleados[i]} | ${salarios[i]} | ${descuentos_salud[i]} | ${descuentos_afp[i]} | ${salarios_liquidos[i]}")


  with open("reporte_sueldos_eva.csv", mode='w', newline='') as file:

    writer = csv.writer(file)

    writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])

    for i in range(len(empleados)):

      writer.writerow([empleados[i], salarios[i], descuentos_salud[i], descuentos_afp[i], salarios_liquidos[i]])

  print("\nReporte de sueldos generado: reporte_sueldos_eva.csv")


def menu_de_sueldos():

  while True:

    print("\nMenú De Sueldos:")

    print("1. Asignar sueldos aleatorios")

    print("2. Categorizar sueldos")

    print("3. Mostrar estadísticas")

    print("4. Generar reporte de sueldos")

    print("5. Salir")


    opcion = input("Seleccione una opción: ")


    if opcion == '1':

      asignar_salarios()

    elif opcion == '2':

      categorizar_salarios()

    elif opcion == '3':

      mostrar_estadisticas()

    elif opcion == '4':

      generar_reporte_salarios()

    elif opcion == '5':

      print("\nFinalizando programa...")

      print("Desarrollado por Joaquin Tapia")

      print("RUT 22.125.935-1")

      break

    else:

      print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":

  menu_de_sueldos()

