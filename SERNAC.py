import csv
import datetime
import math

def agregar(reclamo, monto, rut):
    fecha_hora = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    entrada = [rut, monto, reclamo, fecha_hora]
    return entrada

def Ver():
    with open('Reclamos.csv', 'r', newline='', encoding='utf-8') as archivo_csv:
                    lector_csv = csv.reader(archivo_csv)
                    for fila in lector_csv:
                        print(fila)

def guardar_en_csv(registros, nombre_archivo):
    try:
        with open(nombre_archivo, 'w', newline='',encoding='utf-8') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(['RUT', 'MONTO', 'RECLAMO', 'FECHA_HORA'])
            escritor_csv.writerows(registros)
        print(f"Archivo '{nombre_archivo}' guardado correctamente.")
    except Exception as e:
        print(f"Error al guardar el archivo '{nombre_archivo}': {e}")

def validar_rut(rut):
    if len(rut) != 9:
        return False
    try:
        rut_sin_dv = rut[:-1]
        dv_ingresado = rut[-1]
        multiplicadores = [3, 2, 7, 6, 5, 4, 3, 2]
        suma = sum(int(rut_sin_dv[i]) * multiplicadores[i] for i in range(8))
        resto = 11 - (suma % 11)
        dv_calculado = 'K' if resto == 10 else '0' if resto == 11 else str(resto)
        return dv_calculado == dv_ingresado
    except:
        return False

Registros = []

def menu():
    while True:
        print('###########################################')
        print("\n BIENVENIDO AL REGISTRO DE RECLAMOS!")
        print("1. Agregar un Reclamo")
        print("2. Listar Reclamos")
        print("3. Guardar/Respaldar Reclamo en CSV")
        print("4. Salir")
        print('###########################################')
        op = input("Seleccione una opcion: ")

        if op == '1':
            while True:
                Rut = input("Ingrese su Rut para el reclamo (sin puntos ni guión, con dígito verificador): ").upper()
                if validar_rut(Rut):
                    break
                else:
                    print("Ingrese un RUT válido")

            Reclamo = input("Ingrese su reclamo: ")
            while True:
                try:
                    Monto = float(input("Ingrese el monto de la compra: "))
                    if Monto > 0:
                        break
                    else:
                        print("Ingrese un monto válido.")
                except ValueError:
                    print("Ingrese un monto válido.")
           
            entrada = agregar(Reclamo, Monto, Rut)
            Registros.append(entrada)
            print("Su Reclamo ha sido registrado con éxito")

        elif op == '2':
            if Registros:
                print("\nRegistros:")
                for entrada in Registros:
                    print(entrada)
            else:
                print("No se ha encontrado ningún registro de reclamo")

        elif op == '3':
            Nombre_Archivo = input("Ingresa el nombre del archivo CSV: ")
            guardar_en_csv(Registros, Nombre_Archivo)
            print("Registro de Reclamo Guardado")

        elif op == '4':
            print("HASTA LA PROXIMA!")
            break

        else:
            print("Opción no Válida")

menu()
