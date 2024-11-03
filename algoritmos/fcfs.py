def fcfs(procesos):
    # Inicializa el tiempo actual
    tiempo_actual = 0
    tiempo_ejecucion = []  # Lista para almacenar los tiempos de finalización
    tiempo_entrega = []  # Lista para almacenar los tiempos de entrega
    tiempo_espera = []  # Lista para almacenar los tiempos de espera

    # Iterar a través de cada proceso en la lista
    for proceso in procesos:
        tiempo_llegada = proceso[1]  # Tiempo de llegada del proceso
        tiempo_cpu = proceso[2]  # Tiempo de CPU del proceso

        # Si el tiempo actual es menor que el tiempo de llegada, avanzar el tiempo
        if tiempo_actual < tiempo_llegada:
            tiempo_actual = tiempo_llegada
        
        # Actualizar el tiempo actual sumando el tiempo de CPU del proceso
        tiempo_actual += tiempo_cpu
        
        # Almacenar el tiempo de finalización del proceso
        tiempo_ejecucion.append(tiempo_actual)
        
        # Calcular y almacenar el tiempo de entrega (turnaround time)
        tiempo_entrega.append(tiempo_actual - tiempo_llegada)
        
        # Calcular y almacenar el tiempo de espera
        tiempo_espera.append(tiempo_entrega[-1] - tiempo_cpu)

    # Retornar las listas con los resultados
    return tiempo_ejecucion, tiempo_entrega, tiempo_espera