import csv
from algoritmos.fcfs import fcfs
from algoritmos.sjf import sjf
from algoritmos.prioridad import prioridad

def cargar_procesos(archivo):
    procesos = []
    with open(archivo, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar encabezado
        for row in reader:
            nombre = row[0]
            tiempo_creacion = int(row[1])
            tiempo_cpu = int(row[2])
            prioridad = int(row[3])
            procesos.append([nombre, tiempo_creacion, tiempo_cpu, prioridad])
    return procesos

def imprimir_resultados(nombre_algoritmo, procesos, tiempos_ejecucion, tiempos_entrega, tiempos_espera):
    print(f"\nResultados del algoritmo {nombre_algoritmo}:")
    print(f"{'Proceso':<10}{'Tiempo de Ejecución':<20}{'Tiempo de Entrega':<20}{'Tiempo de Espera':<20}")
    for i, (ejecucion, entrega, espera) in enumerate(zip(tiempos_ejecucion, tiempos_entrega, tiempos_espera)):
        print(f"{procesos[i][0]:<10}{ejecucion:<20}{entrega:<20}{espera:<20}")

    # Calcular y mostrar los promedios si existen tiempos de espera y de entrega
    if tiempos_espera and tiempos_entrega:
        tiempo_espera_promedio = sum(tiempos_espera) / len(tiempos_espera)
        tiempo_entrega_promedio = sum(tiempos_entrega) / len(tiempos_entrega)
        print(f"\nTiempo de espera promedio ({nombre_algoritmo}): {tiempo_espera_promedio:.2f}")
        print(f"Tiempo de entrega promedio ({nombre_algoritmo}): {tiempo_entrega_promedio:.2f}")


def main():
    # Cargar procesos desde el archivo de entrada
    procesos = cargar_procesos('data/input.txt')

    # Ejecutar y mostrar resultados para FCFS
    tiempos_ejecucion_fcfs, tiempos_entrega_fcfs, tiempos_espera_fcfs = fcfs(procesos)
    imprimir_resultados("FCFS", procesos, tiempos_ejecucion_fcfs, tiempos_entrega_fcfs, tiempos_espera_fcfs)

    # Ejecutar y mostrar resultados para SJF
    tiempos_ejecucion_sjf, tiempos_entrega_sjf, tiempos_espera_sjf = sjf(procesos)
    imprimir_resultados("SJF", procesos, tiempos_ejecucion_sjf, tiempos_entrega_sjf, tiempos_espera_sjf)

    # Ejecutar y mostrar resultados para Prioridad
    tiempos_ejecucion_prioridad, tiempos_entrega_prioridad, tiempos_espera_prioridad = prioridad(procesos)
    imprimir_resultados("Prioridad", procesos, tiempos_ejecucion_prioridad, tiempos_entrega_prioridad, tiempos_espera_prioridad)

if __name__ == "__main__":
    main()
