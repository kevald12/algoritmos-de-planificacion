def sjf(procesos):
    # Ordenar procesos primero por tiempo de llegada, luego por tiempo de CPU
    procesos = sorted(procesos, key=lambda x: (x[1], x[2]))  # x[1] es tiempo de llegada, x[2] es tiempo de CPU
    tiempo_actual = 0
    tiempo_ejecucion = []
    tiempo_entrega = []
    tiempo_espera = []
    procesos_finalizados = []

    while len(procesos_finalizados) < len(procesos):
        # Filtrar procesos que ya llegaron y no han sido finalizados
        procesos_disponibles = [p for p in procesos if p[1] <= tiempo_actual and p not in procesos_finalizados]
        
        if not procesos_disponibles:  # Si no hay procesos disponibles, avanzamos el tiempo
            tiempo_actual += 1
            continue

        # Seleccionamos el proceso con el menor tiempo de CPU
        proceso_actual = min(procesos_disponibles, key=lambda x: x[2])
        nombre, tiempo_llegada, tiempo_cpu, _ = proceso_actual  # Ignoramos el último valor (prioridad)

        # Calculamos los tiempos para el proceso seleccionado
        tiempo_inicio = max(tiempo_actual, tiempo_llegada)
        tiempo_actual = tiempo_inicio + tiempo_cpu
        tiempo_ejecucion.append(tiempo_actual)
        tiempo_entrega.append(tiempo_actual - tiempo_llegada)
        tiempo_espera.append(tiempo_entrega[-1] - tiempo_cpu)

        # Marcamos el proceso como finalizado
        procesos_finalizados.append(proceso_actual)

    return tiempo_ejecucion, tiempo_entrega, tiempo_espera
