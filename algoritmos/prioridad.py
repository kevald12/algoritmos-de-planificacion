def prioridad(procesos):
    tiempo_actual = 0
    procesos_ordenados = sorted(procesos, key=lambda x: (x[1], x[3]))  # Ordenar por tiempo de creación y luego prioridad
    tiempos_ejecucion = []
    tiempos_entrega = []
    tiempos_espera = []
    procesos_finalizados = []

    while len(procesos_finalizados) < len(procesos):
        # Filtrar los procesos que han llegado y no están completados
        procesos_disponibles = [p for p in procesos_ordenados if p[1] <= tiempo_actual and p not in procesos_finalizados]
        
        if not procesos_disponibles:
            tiempo_actual += 1  # Avanza el tiempo si no hay procesos listos
            continue

        # Selecciona el proceso con la mayor prioridad
        proceso_actual = min(procesos_disponibles, key=lambda x: x[3])  # Selección por prioridad (menor número = mayor prioridad)
        nombre, tiempo_llegada, tiempo_cpu, prioridad = proceso_actual

        tiempo_inicio = max(tiempo_actual, tiempo_llegada)
        tiempo_actual = tiempo_inicio + tiempo_cpu

        # Calcular y almacenar los tiempos
        tiempos_ejecucion.append(tiempo_actual)  # Tiempo de ejecución final del proceso
        tiempos_entrega.append(tiempo_actual)  # Tiempo de entrega es el mismo que el tiempo de ejecución
        tiempos_espera.append(tiempo_inicio - tiempo_llegada)  # Tiempo de espera es el tiempo de inicio menos tiempo de creación
        
        # Marcar proceso como finalizado
        procesos_finalizados.append(proceso_actual)

    return tiempos_ejecucion, tiempos_entrega, tiempos_espera
